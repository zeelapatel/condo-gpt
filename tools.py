import ast
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.agents.agent_toolkits import create_retriever_tool
from langchain_community.agent_toolkits import SQLDatabaseToolkit
def query_as_list(query, db):
    res = db.run(query)
    return ast.literal_eval(res)[0]

def setup_tools(db, llm):
    addresses = query_as_list("SELECT address from core_condobuilding", db)
    alt_names = query_as_list("SELECT alt_name from core_condobuilding", db)
    vector_db = FAISS.from_texts(alt_names + addresses, OpenAIEmbeddings())
    retriever = vector_db.as_retriever(search_kwargs={"k": 5})
    description = "This is a vector database for retrieving similar addresses and alternative names."
    retriever_tool = create_retriever_tool(retriever, name = "search_proper_nouns",description=description)
    
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    tools = toolkit.get_tools()
    tools.append(retriever_tool)
    return tools