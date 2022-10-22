import json
import pandas as pd
import numpy as np

def processJson(json_data, rawdata, education, major):
    rawdata = pd.read_csv('C:/Users/User/Documents/GitHub/NACE-From-Handshake/test.csv', encoding="ISO-8859-1")
    rawdata = rawdata[(rawdata['Recipient Education Level'] == education)]
    if(major != ""):
        rawdata = rawdata[rawdata['Recipient Primary Major'] == major]
    global data
    global shape
    global compiled
    data = rawdata
    compiled = rawdata
    raw_size = rawdata.shape[0]

    #print(json_data)

    for tab_name in json_data:
        data = rawdata
        py_function_bool = False
        shape = True
        for tab_key in json_data[tab_name]:
            if (tab_key == 'Py Function'):
                py_function_bool = True
                py_function_string = json_data[tab_name]['Py Function']
                shape = checkShape(py_function_string)
                continue
            
            if(py_function_bool == True & shape == True):
                if(json_data[tab_name][tab_key] == ""):
                    statement = "data = data[("+ py_function_string +"(data['"+tab_key+"']))]"
                    exec(statement, globals(), globals())
                    continue
                else:
                    statement = "data = data[("+ py_function_string +"(data[json_data[tab_name] == json_data[tab_name][tab_key]))]"
                    exec(statement, globals(), globals())
                    continue
            if((py_function_bool == True) & (shape == False)):
                if(json_data[tab_name][tab_key] == ""):
                    statement = "data = "+ py_function_string +"(compiled['"+tab_key+"'])"
                    exec(statement, globals(), globals())
                    continue
                else:
                    compiled = compiled[compiled[tab_key] == json_data[tab_name][tab_key]]
                    continue
            data = data[data[tab_key] == json_data[tab_name][tab_key]]
        name = tab_name.replace(' ', '_').replace('-', '_').replace('/', '_').replace('#', 'num').replace('(', '').replace(')', '')
        if (shape == False):
            exec("processJson."+name + " = data")
        else:
            #if(raw_size == data.shape[0]):
                #print("original data matches transformed data, error likely")
            exec("processJson."+name + " = data.shape[0]")
        statment = 'print(tab_name + ": "+ str(processJson.'+name+'))'
        #exec(statment)
        #print(tab_name + ": "+ str(locals()[processJson.name]))



def main():
    rawdata = pd.read_csv('C:/Users/User/Documents/GitHub/NACE-From-Handshake/test.csv', encoding="ISO-8859-1")
    f = open('C:/Users/User/Documents/GitHub/NACE-From-Handshake/test.json')
    json_data = json.load(f)
    df = create_df_overall(json_data, rawdata, "Bachelors")
    print(df)
    df = create_df_majors(json_data, rawdata, "Bachelors")
    f.close()
    print(df)

def create_df_overall(json_data, rawdata, education):
    processJson(json_data, rawdata, education, "")
    df_columns = []
    df_list = []
    for tab_name in json_data:
        df_columns.append(tab_name)
        name = tab_name.replace(' ', '_').replace('-', '_').replace('/', '_').replace('#', 'num').replace('(', '').replace(')', '')
        exec('df_list.append(processJson.'+name+')')

    df = pd.DataFrame(columns=df_columns)
    data_list = []
    for i in df_list:
        data_list.append(i)
    s = pd.Series(data_list, index=df.columns)
    df = df.append(s, ignore_index=True)
    return df

def create_df_majors(json_data, rawdata, education):
    education_level = rawdata[rawdata["Recipient Education Level"].str.startswith(education, na=False)]
    majors = education_level['Recipient Primary Major'].unique()
    df_columns = []
    
    df_columns.append("Academic Program Name")
    for tab_name in json_data:
        df_columns.append(tab_name)
    df = pd.DataFrame(columns=df_columns)
    print(df)
    for major in majors:
        processJson(json_data, rawdata, education, major)
        data_list = []
        df_list = []
        df_list.append(major)
        for tab_name in json_data:
            #df_columns.append(tab_name)
            name = tab_name.replace(' ', '_').replace('-', '_').replace('/', '_').replace('#', 'num').replace('(', '').replace(')', '')
            exec('df_list.append(processJson.'+name+')')
        for var in df_list:
            data_list.append(var)
        print(data_list)
        s = pd.Series(data_list, index=df.columns)
        df = df.append(s, ignore_index=True)
    return df

def main1():
    rawdata = pd.read_csv('C:/Users/User/Documents/GitHub/NACE-From-Handshake/test.csv', encoding="ISO-8859-1")
    Bachelors = "Bachelors"
    Masters = "Masters"
    rawdata = rawdata[(rawdata['Recipient Education Level'] == Bachelors)]
    global data
    global shape
    global compiled
    data = rawdata
    compiled = rawdata
    raw_size = rawdata.shape[0]

    f = open('C:/Users/User/Documents/GitHub/NACE-From-Handshake/test.json')
    json_data = json.load(f)
    #print(json_data)

    testlist = []
    for tab_name in json_data:
        testlist.append(tab_name)
    print(testlist)

    for tab_name in json_data:
        data = rawdata
        py_function_bool = False
        shape = True
        for tab_key in json_data[tab_name]:
            if (tab_key == 'Py Function'):
                py_function_bool = True
                py_function_string = json_data[tab_name]['Py Function']
                shape = checkShape(py_function_string)
                continue
            
            if(py_function_bool == True & shape == True):
                if(json_data[tab_name][tab_key] == ""):
                    statement = "data = data[("+ py_function_string +"(data['"+tab_key+"']))]"
                    exec(statement, globals(), globals())
                    continue
                else:
                    statement = "data = data[("+ py_function_string +"(data[json_data[tab_name] == json_data[tab_name][tab_key]))]"
                    exec(statement, globals(), globals())
                    continue
            if((py_function_bool == True) & (shape == False)):
                if(json_data[tab_name][tab_key] == ""):
                    statement = "data = "+ py_function_string +"(compiled['"+tab_key+"'])"
                    exec(statement, globals(), globals())
                    continue
                else:
                    compiled = compiled[compiled[tab_key] == json_data[tab_name][tab_key]]
                    continue
            data = data[data[tab_key] == json_data[tab_name][tab_key]]
        name = tab_name.replace(' ', '_').replace('-', '_').replace('/', '_').replace('#', 'num').replace('(', '').replace(')', '')
        if (shape == False):
            exec(name + " = data")
        else:
            if(raw_size == data.shape[0]):
                print("original data matches transformed data, error likely")
            exec(name + " = data.shape[0]")
        print(tab_name + ": "+ str(locals()[name]))
    f.close() #Close Json File

def checkShape(py_function):
    shapelist = ["pd.isna"]
    if (py_function in shapelist):
        return True
    else: 
        return False

main()