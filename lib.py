
def name(man):
    return str(man.name)


def load():
    import json
    with open('data.json', "r") as jsonFile:
        return json.load(jsonFile)


def save(data):
    import json
    with open('data.json', "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)

def rules():
    return '''#1 - Be nice to one another, respect each other's opinions.
# 2 - Dont send hateful messages.
# 3 - No nsfw or inappropriate messages should be sent.
# 4 - If anyone encounters any issue, Ping the @Admin they will address the issue.
# 5 - suggestions can be given in #suggestions 
# 6 - No spamming please or pinging of @everyone 
# 7 - No racist or homophobic messages, photos ,videos etc
# 8 - This is an English speaking server so speak in English to the best of your ability
People who do not abide with these rules will be banned or muted from the server
Have a good time at this server!'''
