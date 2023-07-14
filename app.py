from flask import Flask, render_template, request, json
from chatGPT import generateHTML, generateJSON, generateSuggestion
from database import createDatabase, updateDatabase
import openai
import glob
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/page2")
def displaythis():
    return "This is page 2"

@app.route("/user/<username>", methods=['GET', 'POST'])
def userFunction(username):
    return "Hi I am " + str(username)

@app.route("/generate")
def displayTryt():
    return render_template("tryt.html")

# @app.route("/suggestions")
# def suggestionRoute():
#     json_body = json.loads(request.data)
#     question = json_body['question']
#     response = generateSuggestion(question)
#     return json.dumps(response)

@app.route("/chatgpt", methods=['GET', 'POST'])
def sendQuestion():

    print("button clicked!")

    json_body = json.loads(request.data)
    question = json_body['question']
    questionNum = json_body['questionNum']

    result_json = generateJSON(question, questionNum) 
    print(result_json)

    

    filename = f"{result_json['title']}.json"
    file = open(f"static/survey/{filename}", "w")
    file.write(json.dumps(result_json))
    file.close()

    createDatabase(result_json)

    return result_json

@app.route("/surveyList")
def getSurveyList():
    files = glob.glob("static/survey/*")
    print(files)
    surveyList = []
    for file in files:
        rindex = file.rfind("\\")
        lindex = file.index(".")
        title = file[rindex+1:lindex]
        url = f'http://127.0.0.1:5000/jinja_temp/{title}.json'
        surveyList.append({'title': title, 'url': url})

    return json.dumps(surveyList)

@app.route("/database", methods=['POST'])
def getData():
    print(request.json)
    json_content = request.json
    updateDatabase(json_content)
    return "Success"

@app.route("/jinja_temp/<name>", methods = ["GET", "POST"])
def getRender(name):

    a = open(f'static/survey/{name}.json')
    value = a.read()
    a.close()

    return render_template("master_survey.html", input=eval(value))

@app.route("/user_survey/<name>", methods = ["GET", "POST"])
def getUserSurvey(name):

    a = open(f'static/survey/{name}.json')
    value = a.read()
    a.close()

    return render_template("user_survey.html", input=eval(value))

@app.route("/result/<name>")
def getResult(name):

    a = open(f'static/database/{name} Database.json')
    value = a.read()
    a.close()
    
    print(value)

    return render_template("result.html", input=eval(value), name_input=name)

@app.route("/analysis/<name>")
def getAnalysis(name):

    a = open(f'static/database/{name} Database.json')
    value = a.read()
    a.close()
    
    print(value)

    return render_template("analysis.html", input=eval(value), name_input=name)



if __name__ == "__main__":
    app.run(debug=True)
