import json

def createDatabase(json_file):

    questionsList = []
    for i in json_file["questions"]:

        counter = {}
        for x in i["options"]:
            counter[x] = 0

        option = {
            "questions": i["question"],
            "options": counter
        }


        questionsList.append(option)

    entry = {json_file["title"] : questionsList}

    
    
    
    name = f"{json_file['title']} Database.json"
    database = open(f"static/database/{name}", "w")
    database.write(json.dumps(entry))
    database.close()


def updateDatabase(result):
    
    # Accessing the database
    file = open(f"static/database/{result['title']} Database.json", "r")
    database = file.read()
    file.close()

    # Covert database from string to JSON obj (dictionary)
    database = eval(database)

    counterList = database[result['title']]
    
    # Modify the database
    for index, answer in enumerate(result['options']):
        counterList[index]['options'][answer] += 1

    database[result['title']] = counterList

    # Write updated database back to file
    file = open(f"static/database/{result['title']} Database.json", "w")
    file.write(json.dumps(database))
    file.close()