# from openai import OpenAI
# import getpass
# import os
# from langchain_openai import ChatOpenAI

# if not os.getenv("OPENROUTER_API_KEY"):
#     print("Please set the OPENROUTER_API_KEY environment variable.")
#     os.environ["OPENROUTER_API_KEY"] = getpass.getpass("Enter your OpenRouter API key: ")
    
# llm = ChatOpenAI(
#     model="openai/gpt-4o-2024-11-20",
#     temperature=0.0,
#     max_tokens=1000,
#     max_retries=2,
#     openai_api_key=os.getenv("OPENROUTER_API_KEY"),
#     openai_api_base="https://openrouter.ai/api/v1",
#     default_headers={
#         "HTTP-Referer": "https://your-site.com",  # Optional: Replace with your site URL
#         "X-Title": "Condo-GPT",  # Optional: Replace with your app name
#     }
# )


# messages = [("system", "You are a helpful assistant that translate english to hindi."),
#             ("human","hello, how are you?"),]

# ai_message = llm.invoke(messages)
# print(ai_message)

import os
import re
import markdown
from markupsafe import Markup
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_openai import ChatOpenAI
from prefix import SQL_PREFIX
from boilerplate import marker_boilerplate, holding_period_boilerplate, two_bed_holding_period_boilerplate, javascript_map_boilerplate,building_marker_format_boilerplate,school_marker_format_boilerplate
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.prebuilt import create_react_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from tools import setup_tools

POSTGRES_USER = os.getenv("PG_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("PG_PASSWORD", "postgres")
POSTGRES_HOST = os.getenv("PG_HOST", "localhost")
POSTGRES_PORT = os.getenv("PG_PORT", "5432")
POSTGRES_DB = os.getenv("PG_DB", "condo_gpt")

connection_string = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

db = SQLDatabase.from_uri(connection_string)
llm = ChatOpenAI(model="gpt-4o-mini")


prefix = SQL_PREFIX.format(
    table_names = db.get_usable_table_names(),
    holding_period_boilerplate = holding_period_boilerplate,
    two_bed_holding_period_boilerplate = two_bed_holding_period_boilerplate,
    marker_boilerplate = marker_boilerplate,
    javascript_map_boilerplate = javascript_map_boilerplate,
    building_marker_format_boilerplate = building_marker_format_boilerplate,
    school_marker_format_boilerplate = school_marker_format_boilerplate
)

system_message = SystemMessage(content=prefix)
tools = setup_tools(db, llm)
agent_executer = create_react_agent(llm,tools,state_modifier=system_message)

def print_sql(sql):
    print("""
          The SQL query  is:
          {}
          """.format(sql))

setuptools = setup_tools(db, llm)

def extract_and_remove_html(text):
    html_pattern = r"```html\s*([\s\S]*?)\s*```"
    match = re.search(html_pattern, text, re.IGNORECASE)
    if match:
        html_content = match.group(1).strip()
        
        stripped_text = re.sub(html_pattern, "", text, flags=re.IGNORECASE).strip()
        return Markup(html_content), stripped_text
    return None, text

def process_markdown(text):
    html = markdown.markdown(text, extensions=['extra', 'codehilite'])
    return Markup(html)
def process_question(prompted_question, conversation_history):
    context = "\n".join([f"Q:{entry['question']}\nA:{entry['answer']}" for entry in conversation_history])
    
    consolidated_prompt = f"""
    
    previous conversation history:{context}
    
    new question: {prompted_question}
    
    please answer new question taking into account the context from the previous conversation.
    """
    prompt = consolidated_prompt if conversation_history else prompted_question
    content = []

    for s in agent_executer.stream({"messages":[HumanMessage(content=prompt)]}):
        for msg in s.get("agent",{}).get("messages",[]):
            for call in msg.tool_calls:
                if sql := call.get("args",{} ).get("query", None):
                    print(print_sql(sql))

            print(msg.content)
            html, stripped_text = extract_and_remove_html(msg.content)

            content.append(process_markdown(msg.content))
            if html:
                content.append(html)
            else:
                content.append(stripped_text)
    return content

