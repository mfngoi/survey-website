import openai

openai.api_key = '{personal API Key}'

def generateJSON(topic, questionnum):
    
    instruction_prompt = f"create a survey form of the survey (the survey should include {questionnum} questions) as a json format and use question and options for the label" \
                         " of the list of questions. Use title for the label of the title. Please give me only the " \
                         "json format as an output and do not write anything before or after the json format"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=2000,
        messages=[
            {"role": "system", "content": instruction_prompt},
            {"role": "user", "content": topic},
        ]
    )

    result = response['choices'][0]['message']['content']
    result_json = eval(result)
    return result_json


def generateHTML(json_survey):
    f = open('templates/survey/basketball.html', 'r')
    example = f.read()
    f.close()
    sample_code = {'title': 'School Survey', 'options': ['Science', '1-3 hours', 'Bike', 'Music', '4 - Very satisfied']}
    message = f'write a html file with questions from this survey {json_survey} with the title of the survey and a list of the selected options from the survey as a json. For the title, use "title" as a label, for the options use "options" as a label. Example: {sample_code} .Do not use "IF-ELSE" condition inside the html body. Do not write anything before or after the html file. Create a select-one system for the answer choices of each question. Use this {example} as an example.'


    

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=2000,
        messages=[
            {"role": "user", "content": message},
        ]
    )
    
    htmlfile = response['choices'][0]['message']['content']
    return htmlfile

def generateSuggestion(question):

    message = "Give some sample selection suggestions for the survey of this research question(only show the suggestions): " + question
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.8,
        max_tokens=2000,
        messages=[ 
            {"role": "user","content": message},
        ]
    )

    return response['choices'][0]['message']['content']
