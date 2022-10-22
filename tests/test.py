import json
import pandas as pd
import numpy as np

def main():
    rawdata = pd.read_csv('C:/Users/User/Documents/GitHub/NACE-From-Handshake/test.csv', encoding="ISO-8859-1")
    Bachelors = "Bachelors"
    Masters = "Masters"
    rawdata = rawdata[(rawdata['Recipient Education Level'] == Bachelors)]
    global data
    global shape
    global compiled
    data = rawdata
    compiled = rawdata

    f = open('C:/Users/User/Documents/GitHub/NACE-From-Handshake/test.json')
    json_data = json.load(f)
    #print(json_data)
    for tab_name in json_data:
        data = rawdata
        conditional = False
        shape = True
        for tab_key in json_data[tab_name]:
            if (tab_key == 'Conditional'):
                conditional = True
                conditional_string = json_data[tab_name]['Conditional']
                shape = checkShape(conditional_string)
                continue
            
            if(conditional == True & shape == True):
                if(json_data[tab_name][tab_key] == ""):
                    statement = "data = data[("+ conditional_string +"(data['"+tab_key+"']))]"
                    exec(statement, globals(), globals())
                    continue
                else:
                    statement = "data = data[("+ conditional_string +"(data[json_data[tab_name] == json_data[tab_name][tab_key]))]"
                    exec(statement, globals(), globals())
                    continue
            if((conditional == True) & (shape == False)):
                if(json_data[tab_name][tab_key] == ""):
                    statement = "data = "+ conditional_string +"(compiled['"+tab_key+"'])"
                    exec(statement, globals(), globals())
                    continue
                else:
                    compiled = compiled[compiled[tab_key] == json_data[tab_name][tab_key]]
                    continue
            data = data[data[tab_key] == json_data[tab_name][tab_key]]
        name = tab_name.replace(' ', '_').replace('-', '_').replace('/', '_')
        if (shape == False):
            exec(name + " = data")
        else:
            exec(name + " = data.shape[0]")
        print(name + ": "+ str(locals()[name]))
    f.close() #Close Json File

def checkShape(conditional):
    #print(conditional)
    shapelist = ["pd.isna"]
    if (conditional in shapelist):
        return True
    else: 
        return False

main()