import os
from flask import Flask, render_template, render_template, request, session
from main import process_question 

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET")

MAX_CONTENT_LENGTH = 3

def get_conversation_history():
    if "conversation_history" not in session:
        session["conversation_history"] = []
    return session.get("conversation_history", [])

def add_to_conversation_history(question, answer):
    conversation_history = get_conversation_history()
    conversation_history.append({"question": question, "answer": answer})
    if len(conversation_history) > MAX_CONTENT_LENGTH:
        conversation_history.pop(0)
    session["conversation_history"] = conversation_history
    
    
@app.route('/', methods = ["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        if request.form.get("sign_out",None):
            session.clear()
            return render_template('index.html', result = result)
        question = request.form["question"]
        conversation_history = get_conversation_history()
        result = process_question(question, conversation_history)
        add_to_conversation_history(question, result)
    return render_template('index.html', result = result)


if __name__ == '__main__':
    app.run(debug=True)