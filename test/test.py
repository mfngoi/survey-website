import openai

openai.api_key = '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'

def generateJSON(topic, questionnum):
    
    instruction_prompt = f"create a survey form of the survey (the survey should include {questionnum} questions) as a json format and use question and options for the label" \
                         " of the list of questions. Use title for the label of the title. Give me some suggestions about which people to send the survey (make the suggestions about 100-200 words long) to and then store it in the json with a label of suggestion. Please give me only the " \
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
    print(result)
    print()
    print('=================================================================')
    print()
    result_json = eval(result)
    print(result_json)


def generateHTML(database):
    sys_msg = "Make the UI colorful and creative"
    message = f'Write a html file presenting data from this json object: {database}. Display the data in an interesting and colorful layout. Do not use "IF-ELSE" condition inside the html body. Do not write anything before or after the html file.'

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        max_tokens=2000,
        messages=[
            {"role":"system", "content": sys_msg},
            {"role": "user", "content": message},
        ]
    )

    htmlContent = response['choices'][0]['message']['content']  # HTML doc of survey
    print(htmlContent)

print("message sent")
# generateJSON('mushrooms', '6')

database = {
    "Sports Survey": [
        {
            "questions": "Which sport do you enjoy the most?",
            "options": {
                "Football": 0,
                "Basketball": 2,
                "Soccer": 1,
                "Tennis": 1,
                "Other": 0
            }
        },
        {
            "questions": "How often do you participate in sports activities?",
            "options": {
                "Every day": 0,
                "Few times a week": 1,
                "Once a week": 0,
                "Few times a month": 3,
                "Rarely": 0
            }
        },
        {
            "questions": "What motivates you to play sports?",
            "options": {
                "Fitness and health benefits": 0,
                "Competition and winning": 0,
                "Teamwork and camaraderie": 3,
                "Stress relief": 1,
                "Fun and enjoyment": 0
            }
        },
        {
            "questions": "Do you prefer watching sports events or playing them?",
            "options": {
                "Watching": 3,
                "Playing": 1
            }
        },
        {
            "questions": "How do sports contribute to your overall well-being?",
            "options": {
                "Physical fitness": 1,
                "Mental well-being": 2,
                "Social connections": 1,
                "Discipline and self-motivation": 0,
                "All of the above": 0
            }
        }
    ]
}

generateHTML(database)