import tkinter as tk
import pandas as pd
import numpy as np
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)

def load_data_handshake(): #Loads the handshake data
    filename = askopenfilename()
    global rawdata
    rawdata = pd.read_csv(filename, encoding = "ISO-8859-1")
    canvas1.create_window(350, 250, window=cip_button)
    button_import.destroy()

def load_cip_data(): #Loads the CIP data (typically from argos report)
    filename = askopenfilename()
    global cip
    cip = pd.read_csv(filename, encoding = "ISO-8859-1")
    canvas1.create_window(100, 150, window=grad_cip_button)
    canvas1.create_window(100, 200, window=under_cip_button)
    canvas1.create_window(350, 250, window= program_data_undergrad_button)
    canvas1.create_window(350, 200, window= program_data_masters_button)
    canvas1.create_window(350, 150, window= program_data_doctorate_button)
    canvas1.create_window(600, 250, window= overall_data_undergrad_button)
    canvas1.create_window(600, 200, window= overall_data_masters_button)
    canvas1.create_window(600, 150, window= overall_data_doctorate_button)
    cip_button.destroy()


def graduate_CIP_codes(): #outputs CIP codes for graduate courses (masters, PHD)
    graduate = rawdata[['Recipient Primary Major']]
    graduate = graduate.join(rawdata[['Recipient Education Level']])
    indexNames = graduate[ graduate['Recipient Education Level'] == 'Bachelors' ].index
    graduate.drop(indexNames, inplace =True)
    majors = graduate['Recipient Primary Major'].unique()
    filled_graduate = pd.DataFrame(majors, columns = ['major'])
    df = pd.DataFrame(columns=['major','CIP Code'])
    for i in filled_graduate['major']:
        data_list = []
        data_list.append(i)
        try:
            data = cip.loc[cip.MajorDesc ==  i, 'CIPCode'].values[0]
        except:
            data = np.nan
        data_list.append(data)
        s = pd.Series(data_list, index=df.columns)
        df = df.append(s, ignore_index=True)
    graduate_major_cip = df
    filename = asksaveasfile(defaultextension=".csv", 
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*") ))
    df.to_csv(filename, line_terminator='\n')
    
def under_CIP_codes(): #Outputs CIP codes for undergrad courses
    underdf = pd.DataFrame(columns=['major','CIP Code'])
    
    undergrad = rawdata[['Recipient Primary Major']]
    undergrad = undergrad.join(rawdata[['Recipient Education Level']])
    indexNames = undergrad[ undergrad['Recipient Education Level'] != 'Bachelors' ].index
    undergrad.drop(indexNames, inplace=True)
    majors = undergrad['Recipient Primary Major'].unique()
    filled_undergrad = pd.DataFrame(majors, columns = ['major'])
    df = pd.DataFrame(columns=['major','CIP Code'])
    for i in filled_undergrad['major']:
        data_list = []
        data_list.append(i)
        try:
            data = cip.loc[cip.MajorDesc ==  i, 'CIPCode'].values[0]
        except:
            data = np.nan
        data_list.append(data)
        s = pd.Series(data_list, index=df.columns)
        underdf = underdf.append(s, ignore_index=True)
    undergrad_major_cip = underdf
    filename = asksaveasfile(defaultextension=".csv", 
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*") ))
    underdf.to_csv(filename, line_terminator='\n')


def program_data_undergrad():
    undergrad = rawdata[['Recipient Primary Major']]
    undergrad = undergrad.join(rawdata[['Recipient Education Level']])
    indexNames = undergrad[ undergrad['Recipient Education Level'] != 'Bachelors' ].index
    undergrad.drop(indexNames, inplace=True)
    majors = undergrad['Recipient Primary Major'].unique()
    filled_undergrad = pd.DataFrame(majors, columns = ['major'])
    df = pd.DataFrame(columns=['major','Total Graduated','Full-Time','Part-Time', 'Entrepreneur Full-Time',
                           'Entrepreneur Part-Time', 'Temp/Contract FT', 'Temp/Contract PT',
                           'Freelance  FT', 'Freelance PT', 'Fellowship/Intern FT', 'Fellowship/Intern PT',
                           'service', 'Military', 'Continuing Education', 'Seeking Employment', 'Seeking Education',
                           'Not Seek','no info', '# of Salaries (Full-time Employed)', 'Salary Mean', 'Median Salary',
                           'Salary Low', 'Salary High', 'Bonus Numbers', 'Bonus Mean', 'Bonus Median', 'Bonus Low', 'Bonus High'])
    for i in filled_undergrad['major']: #Goes through each major and fills a list which gets added to a DF of all majors
        data_list = []
        education = 'Bachelors'
        data_list.append(i) # major
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)].shape[0] 
        data_list.append(data) # Total Graduated^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)].shape[0] 
        data_list.append(data) # Full-Time^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)].shape[0]
        data_list.append(data) # Part-Time^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
        data_list.append(data) # Entrepreneur Full-Time^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
        data_list.append(data) # Entrepreneur Part-Time^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
        data_list.append(data) #Temp/Contract FT^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
        data_list.append(data) #Temp/Contract PT^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Freelancer')].shape[0]
        data_list.append(data) #Freelance FT^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Freelancer')].shape[0]
        data_list.append(data) #Freelance PT^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Internship'] == 'Yes')].shape[0]
        data2 = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                        (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
        data = data + data2
        data_list.append(data) #Fellowshio/Intern FT^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Internship'] == 'Yes')].shape[0]
        data2 = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                        (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
        data = data + data2
        data_list.append(data) #Fellowship/Intern PT^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Volunteering')].shape[0]
        data_list.append(data) #Service^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Military')].shape[0]
        data_list.append(data) #Military^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Continuing Education')].shape[0]
        data_list.append(data) #Continuing Education^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Still Looking Option'] == 'Employment')].shape[0]
        data_list.append(data) #Seeking Employment^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Still Looking Option'] == 'Continuing Education')].shape[0]
        data_list.append(data) #Seeking Education^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Not Seeking')].shape[0]
        data_list.append(data) #Not Seeking^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (pd.isna(rawdata['Outcome']))].shape[0]
        data_list.append(data) #No Info^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Annual Salary'])].shape[0]
        data_list.append(data) ## of Salaries (Full-time Employed)^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = np.mean(data['Annual Salary']) 
        data_list.append(data) # Mean Salary^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = np.median(data['Annual Salary']) 
        data_list.append(data) # Median Salary^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = (data['Annual Salary'].min()) 
        data_list.append(data) # Salary Low^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data =  (data['Annual Salary'].max()) 
        data_list.append(data) # Salary high^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))].shape[0]
        data_list.append(data) # Bonus number^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = np.mean(data['Bonus Amount'])
        data_list.append(data) # Bonus Mean^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = np.median(data['Bonus Amount'])
        data_list.append(data) # Bonus Median^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = data['Bonus Amount'].min()
        data_list.append(data) # Bonus Low^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = data['Bonus Amount'].max()
        data_list.append(data) # Bonus High^
        s = pd.Series(data_list, index=df.columns)
        df = df.append(s, ignore_index=True)
    filename = asksaveasfile(defaultextension=".csv", 
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*") ))
    df.to_csv(filename, line_terminator='\n')
    
def program_data_masters():
    graduate = rawdata[['Recipient Primary Major']]
    graduate = graduate.join(rawdata[['Recipient Education Level']])
    indexNames = graduate[ graduate['Recipient Education Level'] == 'Bachelors' ].index
    graduate.drop(indexNames, inplace =True)
    majors = graduate['Recipient Primary Major'].unique()
    filled_graduate = pd.DataFrame(majors, columns = ['major'])
    
    df = pd.DataFrame(columns=['major','Total Graduated','Full-Time','Part-Time','Faculty Tenure Track','Faculty Non-Tenure Track',
                               'Entrepreneur Full-Time', 'Entrepreneur Part-Time', 'Temp/Contract FT', 'Temp/Contract PT',
                               'Freelance  FT', 'Freelance PT', 'Fellowship/Intern FT', 'Fellowship/Intern PT',
                               'service', 'Military', 'Continuing Education', 'Seeking Employment', 'Seeking Education',
                               'Not Seek','no info', '# of Salaries (Full-time Employed)', 'Salary Mean', 'Median Salary',
                               'Salary Low', 'Salary High', 'Bonus Numbers', 'Bonus Mean', 'Bonus Median', 'Bonus Low', 'Bonus High'])
    
    for i in filled_graduate['major']: #Goes through each major and fills a list which gets added to a DF of all majors
        data_list = []
        education = 'Masters'
        data_list.append(i) # major
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)].shape[0] 
        data_list.append(data) # Total Graduated^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)].shape[0] 
        data_list.append(data) # Full-Time^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)].shape[0]
        data_list.append(data) # Part-Time^
        data = rawdata[(rawdata['Recipient Education Level'] == education) &
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Category'] == 'Faculty Tenure')].shape[0]
        data_list.append(data) # Faculty Tenure Track
        data = rawdata[(rawdata['Recipient Education Level'] == education) &
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Category'] == 'Faculty Non-Tenure')].shape[0]
        data_list.append(data) # Faculty Non-Tenure Track
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
        data_list.append(data) # Entrepreneur Full-Time^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
        data_list.append(data) # Entrepreneur Part-Time^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
        data_list.append(data) #Temp/Contract FT^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
        data_list.append(data) #Temp/Contract PT^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Freelancer')].shape[0]
        data_list.append(data) #Freelance FT^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Freelancer')].shape[0]
        data_list.append(data) #Freelance PT^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Internship'] == 'Yes')].shape[0]
        data2 = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                        (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
        data = data + data2
        data_list.append(data) #Fellowshio/Intern FT^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Internship'] == 'Yes')].shape[0]
        data2 = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                        (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
        data = data + data2
        data_list.append(data) #Fellowship/Intern PT^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Volunteering')].shape[0]
        data_list.append(data) #Service^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Military')].shape[0]
        data_list.append(data) #Military^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Continuing Education')].shape[0]
        data_list.append(data) #Continuing Education^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Still Looking Option'] == 'Employment')].shape[0]
        data_list.append(data) #Seeking Employment^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Still Looking Option'] == 'Continuing Education')].shape[0]
        data_list.append(data) #Seeking Education^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Not Seeking')].shape[0]
        data_list.append(data) #Not Seeking^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (pd.isna(rawdata['Outcome']))].shape[0]
        data_list.append(data) #No Info^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Annual Salary'])].shape[0]
        data_list.append(data) ## of Salaries (Full-time Employed)^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = np.mean(data['Annual Salary']) 
        data_list.append(data) # Mean Salary^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = np.median(data['Annual Salary']) 
        data_list.append(data) # Median Salary^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = (data['Annual Salary'].min()) 
        data_list.append(data) # Salary Low^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data =  (data['Annual Salary'].max()) 
        data_list.append(data) # Salary high^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))].shape[0]
        data_list.append(data) # Bonus number^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = np.mean(data['Bonus Amount'])
        data_list.append(data) # Bonus Mean^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = np.median(data['Bonus Amount'])
        data_list.append(data) # Bonus Median^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = data['Bonus Amount'].min()
        data_list.append(data) # Bonus Low^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = data['Bonus Amount'].max()
        data_list.append(data) # Bonus High^
        s = pd.Series(data_list, index=df.columns)
        df = df.append(s, ignore_index=True)
    filename = asksaveasfile(defaultextension=".csv", 
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*") ))
    df.to_csv(filename, line_terminator='\n')

def program_data_doctorate():
    graduate = rawdata[['Recipient Primary Major']]
    graduate = graduate.join(rawdata[['Recipient Education Level']])
    indexNames = graduate[ graduate['Recipient Education Level'] == 'Bachelors' ].index
    graduate.drop(indexNames, inplace =True)
    majors = graduate['Recipient Primary Major'].unique()
    filled_graduate = pd.DataFrame(majors, columns = ['major'])
    df = pd.DataFrame(columns=['major','Total Graduated','Full-Time','Part-Time','Faculty Tenure Track','Faculty Non-Tenure Track',
                           'Entrepreneur Full-Time', 'Entrepreneur Part-Time', 'Temp/Contract FT', 'Temp/Contract PT',
                           'Freelance  FT', 'Freelance PT', 'Fellowship/Intern FT', 'Fellowship/Intern PT',
                           'service', 'Military', 'Continuing Education', 'Seeking Employment', 'Seeking Education',
                           'Not Seek','no info', '# of Salaries (Full-time Employed)', 'Salary Mean', 'Median Salary',
                           'Salary Low', 'Salary High', 'Bonus Numbers', 'Bonus Mean', 'Bonus Median', 'Bonus Low', 'Bonus High'])
    for i in filled_graduate['major']: #Goes through each major and fills a list which gets added to a DF of all majors
        data_list = []
        education = 'Doctorate'
        data_list.append(i) # major
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)].shape[0] 
        data_list.append(data) # Total Graduated^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)].shape[0] 
        data_list.append(data) # Full-Time^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)].shape[0]
        data_list.append(data) # Part-Time^
        data = rawdata[(rawdata['Recipient Education Level'] == education) &
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Category'] == 'Faculty Tenure')].shape[0]
        data_list.append(data) # Faculty Tenure Track
        data = rawdata[(rawdata['Recipient Education Level'] == education) &
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Category'] == 'Faculty Non-Tenure')].shape[0]
        data_list.append(data) # Faculty Non-Tenure Track
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
        data_list.append(data) # Entrepreneur Full-Time^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
        data_list.append(data) # Entrepreneur Part-Time^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
        data_list.append(data) #Temp/Contract FT^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
        data_list.append(data) #Temp/Contract PT^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Freelancer')].shape[0]
        data_list.append(data) #Freelance FT^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Employment Category'] == 'Freelancer')].shape[0]
        data_list.append(data) #Freelance PT^
        data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Internship'] == 'Yes')].shape[0]
        data2 = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                        (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
        data = data + data2
        data_list.append(data) #Fellowshio/Intern FT^
        data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                       (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Internship'] == 'Yes')].shape[0]
        data2 = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                        (rawdata['Recipient Primary Major'] == i) &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
        data = data + data2
        data_list.append(data) #Fellowship/Intern PT^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Volunteering')].shape[0]
        data_list.append(data) #Service^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Military')].shape[0]
        data_list.append(data) #Military^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Continuing Education')].shape[0]
        data_list.append(data) #Continuing Education^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Still Looking Option'] == 'Employment')].shape[0]
        data_list.append(data) #Seeking Employment^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Still Looking Option'] == 'Continuing Education')].shape[0]
        data_list.append(data) #Seeking Education^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Outcome'] == 'Not Seeking')].shape[0]
        data_list.append(data) #Not Seeking^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (pd.isna(rawdata['Outcome']))].shape[0]
        data_list.append(data) #No Info^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Annual Salary'])].shape[0]
        data_list.append(data) ## of Salaries (Full-time Employed)^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = np.mean(data['Annual Salary']) 
        data_list.append(data) # Mean Salary^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = np.median(data['Annual Salary']) 
        data_list.append(data) # Median Salary^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = (data['Annual Salary'].min()) 
        data_list.append(data) # Salary Low^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data =  (data['Annual Salary'].max()) 
        data_list.append(data) # Salary high^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))].shape[0]
        data_list.append(data) # Bonus number^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = np.mean(data['Bonus Amount'])
        data_list.append(data) # Bonus Mean^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = np.median(data['Bonus Amount'])
        data_list.append(data) # Bonus Median^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = data['Bonus Amount'].min()
        data_list.append(data) # Bonus Low^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Employment Type'] == 'Full-Time') &
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = data['Bonus Amount'].max()
        data_list.append(data) # Bonus High^
        s = pd.Series(data_list, index=df.columns)
        df = df.append(s, ignore_index=True)
    filename = asksaveasfile(defaultextension=".csv", 
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*") ))
    df.to_csv(filename, line_terminator='\n')


def overall_data_undergrad():
    df = pd.DataFrame(columns=['Total Graduated','Full-Time','Part-Time', 'Entrepreneur Full-Time',
                           'Entrepreneur Part-Time', 'Temp/Contract FT','Temp/Contract PT', 'Freelance  FT', 'Freelance PT',
                           'Fellowship/Intern FT','Fellowship/Intern PT',
                           'Service', 'Military', 'Continuing Education', 'Seeking Employment', 'Seeking Education',
                           'Not Seek','no info', '# of Salaries (Full-time Employed)', 'Salary Mean', 'Median Salary',
                           'Recieving Bonus', 'Bonus Mean', 'Bonus Median'])

    data_list = []
    education = 'Bachelors'
    
    data = rawdata[(rawdata['Recipient Education Level'] == education)].shape[0] 
    data_list.append(data) # Total Graduated^
        
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)].shape[0] 
    data_list.append(data) # Full-Time^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)].shape[0]
    data_list.append(data) # Part-Time^
        
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
    data_list.append(data) # Entrepreneur Full-Time^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
    data_list.append(data) # Entrepreneur Part-Time^
        
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
    data_list.append(data) #Temp/Contract FT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
    data_list.append(data) #Temp/Contract PT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Freelancer')].shape[0]
    data_list.append(data) #Freelance FT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Freelancer')].shape[0]
    data_list.append(data) #Freelance PT^
    
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Internship'] == 'Yes')].shape[0]
    data2 = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
    data = data + data2
    data_list.append(data) #Fellowshio/Intern FT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Internship'] == 'Yes')].shape[0]
    data2 = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
    data = data + data2
    data_list.append(data) #Fellowship/Intern PT^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Volunteering')].shape[0]
    data_list.append(data) #Service^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Military')].shape[0]
    data_list.append(data) #Military^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Continuing Education')].shape[0]
    data_list.append(data) #Continuing Education^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Still Looking Option'] == 'Employment')].shape[0]
    data_list.append(data) #Seeking^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Still Looking Option'] == 'Continuing Education')].shape[0]
    data_list.append(data) #Seeking Education^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Not Seeking')].shape[0]
    data_list.append(data) #Not Seeking^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (pd.isna(rawdata['Outcome']))].shape[0]
    data_list.append(data) #No Info^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Annual Salary'])].shape[0]
    data_list.append(data) ## of Salaries (Full-time Employed)^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education) & 
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Annual Salary'])]
    data = np.mean(data['Annual Salary']) 
    data_list.append(data) # Mean Salary^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education) & 
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Annual Salary'])]
    data = np.median(data['Annual Salary']) 
    data_list.append(data) # Median Salary^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))].shape[0]
    data_list.append(data) # Bonus number^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Bonus Amount'] != 0) & 
                   (pd.notna(rawdata['Bonus Amount']))]
    data = np.mean(data['Bonus Amount'])
    data_list.append(data) # Bonus Mean^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Bonus Amount'] != 0) & 
                   (pd.notna(rawdata['Bonus Amount']))]
    data = np.median(data['Bonus Amount'])
    data_list.append(data) # Bonus Median^
    
     
    s = pd.Series(data_list, index=df.columns)
    df = df.append(s, ignore_index=True)
    filename = asksaveasfile(defaultextension=".csv", 
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*") ))
    df.to_csv(filename, line_terminator='\n')

def overall_data_masters():
    df = pd.DataFrame(columns=['Total Graduated','Full-Time','Part-Time', 'Faculty Tenure Track','Faculty Non-Tenure Track',
                           'Entrepreneur Full-Time',
                           'Entrepreneur Part-Time', 'Temp/Contract FT','Temp/Contract PT', 'Freelance  FT', 'Freelance PT',
                           'Fellowship/Intern FT','Fellowship/Intern PT',
                           'Service', 'Military', 'Continuing Education', 'Seeking Employment', 'Seeking Education',
                           'Not Seek','no info', '# of Salaries (Full-time Employed)', 'Salary Mean', 'Median Salary',
                           'Recieving Bonus', 'Bonus Mean', 'Bonus Median'])

    data_list = []
    education = 'Masters'
    
    data = rawdata[(rawdata['Recipient Education Level'] == education)].shape[0] 
    data_list.append(data) # Total Graduated^
        
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)].shape[0] 
    data_list.append(data) # Full-Time^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)].shape[0]
    data_list.append(data) # Part-Time^
    
    data = rawdata[(rawdata['Recipient Education Level'] == education) &
                   (rawdata['Employment Category'] == 'Faculty Tenure')].shape[0]
    data_list.append(data) # Faculty Tenure Track
    
    data = rawdata[(rawdata['Recipient Education Level'] == education) &
                   (rawdata['Employment Category'] == 'Faculty Non-Tenure')].shape[0]
    data_list.append(data) # Faculty Non-Tenure Track
    
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
    data_list.append(data) # Entrepreneur Full-Time^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
    data_list.append(data) # Entrepreneur Part-Time^
        
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
    data_list.append(data) # Temp/Contract FT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
    data_list.append(data) # Temp/Contract PT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Freelancer')].shape[0]
    data_list.append(data) # Freelance FT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Freelancer')].shape[0]
    data_list.append(data) # Freelance PT^
    
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Internship'] == 'Yes')].shape[0]
    data2 = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
    data = data + data2
    data_list.append(data) # Fellowshio/Intern FT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Internship'] == 'Yes')].shape[0]
    data2 = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
    data = data + data2
    data_list.append(data) # Fellowship/Intern PT^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Volunteering')].shape[0]
    data_list.append(data) # Service^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Military')].shape[0]
    data_list.append(data) # Military^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Continuing Education')].shape[0]
    data_list.append(data) # Continuing Education^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Still Looking Option'] == 'Employment')].shape[0]
    data_list.append(data) # Seeking^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Still Looking Option'] == 'Continuing Education')].shape[0]
    data_list.append(data) # Seeking Education^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Not Seeking')].shape[0]
    data_list.append(data) # Not Seeking^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (pd.isna(rawdata['Outcome']))].shape[0]
    data_list.append(data) # No Info^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Annual Salary'])].shape[0]
    data_list.append(data) ## of Salaries (Full-time Employed)^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education) & 
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Annual Salary'])]
    data = np.mean(data['Annual Salary']) 
    data_list.append(data) # Mean Salary^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education) & 
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Annual Salary'])]
    data = np.median(data['Annual Salary']) 
    data_list.append(data) # Median Salary^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))].shape[0]
    data_list.append(data) # Bonus number^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Bonus Amount'] != 0) & 
                   (pd.notna(rawdata['Bonus Amount']))]
    data = np.mean(data['Bonus Amount'])
    data_list.append(data) # Bonus Mean^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Bonus Amount'] != 0) & 
                   (pd.notna(rawdata['Bonus Amount']))]
    data = np.median(data['Bonus Amount'])
    data_list.append(data) # Bonus Median^
    
        
    s = pd.Series(data_list, index=df.columns)
    df = df.append(s, ignore_index=True)
    filename = asksaveasfile(defaultextension=".csv", 
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*") ))
    df.to_csv(filename, line_terminator='\n')

def overall_data_doctorate():
    df = pd.DataFrame(columns=['Total Graduated','Full-Time','Part-Time', 'Faculty Tenure Track','Faculty Non-Tenure Track',
                           'Entrepreneur Full-Time',
                           'Entrepreneur Part-Time', 'Temp/Contract FT','Temp/Contract PT', 'Freelance  FT', 'Freelance PT',
                           'Fellowship/Intern FT','Fellowship/Intern PT',
                           'Service', 'Military', 'Continuing Education', 'Seeking Employment', 'Seeking Education',
                           'Not Seek','no info', '# of Salaries (Full-time Employed)', 'Salary Mean', 'Median Salary',
                           'Recieving Bonus', 'Bonus Mean', 'Bonus Median'])

    data_list = []
    education = 'Doctorate'
    
    data = rawdata[(rawdata['Recipient Education Level'] == education)].shape[0] 
    data_list.append(data) # Total Graduated^
        
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)].shape[0] 
    data_list.append(data) # Full-Time^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)].shape[0]
    data_list.append(data) # Part-Time^
    
    data = rawdata[(rawdata['Recipient Education Level'] == education) &
                   (rawdata['Employment Category'] == 'Faculty Tenure')].shape[0]
    data_list.append(data) # Faculty Tenure Track
    
    data = rawdata[(rawdata['Recipient Education Level'] == education) &
                   (rawdata['Employment Category'] == 'Faculty Non-Tenure')].shape[0]
    data_list.append(data) # Faculty Non-Tenure Track
    
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
    data_list.append(data) # Entrepreneur Full-Time^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]
    data_list.append(data) # Entrepreneur Part-Time^
        
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
    data_list.append(data) #Temp/Contract FT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]
    data_list.append(data) #Temp/Contract PT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Freelancer')].shape[0]
    data_list.append(data) #Freelance FT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Category'] == 'Freelancer')].shape[0]
    data_list.append(data) #Freelance PT^
    
    data = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Internship'] == 'Yes')].shape[0]
    data2 = rawdata[(rawdata['Employment Type'] == 'Full-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
    data = data + data2
    data_list.append(data) #Fellowshio/Intern FT^
        
    data = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Internship'] == 'Yes')].shape[0]
    data2 = rawdata[(rawdata['Employment Type'] == 'Part-Time') & 
                   (rawdata['Recipient Education Level'] == education)&
                   (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
    data = data + data2
    data_list.append(data) #Fellowship/Intern PT^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Volunteering')].shape[0]
    data_list.append(data) #Service^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Military')].shape[0]
    data_list.append(data) #Military^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Continuing Education')].shape[0]
    data_list.append(data) #Continuing Education^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Still Looking Option'] == 'Employment')].shape[0]
    data_list.append(data) #Seeking^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Still Looking Option'] == 'Continuing Education')].shape[0]
    data_list.append(data) #Seeking Education^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Outcome'] == 'Not Seeking')].shape[0]
    data_list.append(data) #Not Seeking^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (pd.isna(rawdata['Outcome']))].shape[0]
    data_list.append(data) #No Info^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Annual Salary'])].shape[0]
    data_list.append(data) ## of Salaries (Full-time Employed)^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education) & 
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Annual Salary'])]
    data = np.mean(data['Annual Salary']) 
    data_list.append(data) # Mean Salary^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education) & 
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Annual Salary'])]
    data = np.median(data['Annual Salary']) 
    data_list.append(data) # Median Salary^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))].shape[0]
    data_list.append(data) # Bonus number^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Bonus Amount'] != 0) & 
                   (pd.notna(rawdata['Bonus Amount']))]
    data = np.mean(data['Bonus Amount'])
    data_list.append(data) # Bonus Mean^
        
    data = rawdata[(rawdata['Recipient Education Level'] == education)&
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Bonus Amount'] != 0) & 
                   (pd.notna(rawdata['Bonus Amount']))]
    data = np.median(data['Bonus Amount'])
    data_list.append(data) # Bonus Median^
    s = pd.Series(data_list, index=df.columns)
    df = df.append(s, ignore_index=True)
    filename = asksaveasfile(defaultextension=".csv", 
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*") ))
    df.to_csv(filename, line_terminator='\n')

root= tk.Tk()
canvas1 = tk.Canvas(root, width = 700, height = 500)
canvas1.pack()  
button_import = tk.Button(root, text='Select .CSV Handshake Data', command = load_data_handshake)
canvas1.create_window(350, 250, window=button_import)

cip_button =tk.Button(root, text='Select .CSV CIP Data (argos report)', command = load_cip_data)
grad_cip_button = tk.Button(root, text='Save Graduate CIP Codes', command = graduate_CIP_codes)
under_cip_button = tk.Button(root, text='Save undergraduate CIP Codes', command = under_CIP_codes)

program_data_undergrad_button = tk.Button(root, text = 'Save Undergraduate program data', command = program_data_undergrad)
program_data_masters_button = tk.Button(root, text = 'Save Masters program data', command = program_data_masters)
program_data_doctorate_button = tk.Button(root, text = 'Save Doctorate program data', command = program_data_doctorate)

overall_data_undergrad_button = tk.Button(root, text = 'Save Undergraduate overall data', command = overall_data_undergrad)
overall_data_masters_button = tk.Button(root, text = 'Save Masters overall data', command = overall_data_masters)
overall_data_doctorate_button = tk.Button(root, text = 'Save Doctorate overall data', command = overall_data_doctorate)

root.mainloop()