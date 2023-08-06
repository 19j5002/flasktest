import json

def rtnTFR(to, fromc, fromh, requirement):
    temp = data['TFR']
    temp = temp.replace('{TO}', to)
    temp = temp.replace('{FROM}', f'{fromc}の{fromh}')
    temp = temp.replace('{REQUIREMENT}', requirement)
    return temp

def rtnTF():
    temp = data['TF']
    return temp

def rtnT():
    temp = data['T']
    return temp

def rtnF():
    temp = data['F']
    return temp


data = {}
with open('./data/data.json', encoding="UTF_8") as f:
    data = json.load(f)