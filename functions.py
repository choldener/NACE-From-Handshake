import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)


rawdata = pd.read_csv(r'D:\GitHub\Projects\NACE-Belmont\data\2019\csv\Class of 2019 First Destination Survey Raw Data no identifiers scrubbed version 3.3.csv', encoding = "ISO-8859-1")
graduate_cip = pd.read_csv(r'D:\GitHub\Projects\NACE-Belmont\data\2019\CIP codes\Belmont Universtity Graduate CIP codes 2020.csv')
undergraduate_cip = pd.read_csv(r'D:\GitHub\Projects\NACE-Belmont\data\2019\CIP codes\Belmont Universtity Undergraduate CIP codes 2020.csv')
cip = pd.read_csv(r'D:\GitHub\Projects\NACE-Belmont\data\2019\CIP codes\Argos Report.csv')


undergrad = rawdata[['Recipient Primary Major']]
undergrad = undergrad.join(rawdata[['Recipient Education Level']])
indexNames = undergrad[ undergrad['Recipient Education Level'] != 'Bachelors' ].index
undergrad.drop(indexNames, inplace=True)
majors = undergrad['Recipient Primary Major'].unique()

filled_undergrad = pd.DataFrame(majors, columns = ['major'])

graduate = rawdata[['Recipient Primary Major']]
graduate = graduate.join(rawdata[['Recipient Education Level']])
indexNames = graduate[ graduate['Recipient Education Level'] == 'Bachelors' ].index
graduate.drop(indexNames, inplace =True)
majors = graduate['Recipient Primary Major'].unique()

filled_graduate = pd.DataFrame(majors, columns = ['major'])


def Bachelors (rawdata):
    df = pd.DataFrame(columns=['major','Total Graduated','Full-Time','Part-Time', 'Entrepreneur Full-Time',
                           'Entrepreneur Part-Time', 'Temp/Contract FT', 'Temp/Contract PT',
                           'Freelance  FT', 'Freelance PT', 'Fellowship/Intern FT', 'Fellowship/Intern PT',
                           'service', 'Military', 'Continuing Education', 'Seeking Employment', 'Seeking Education',
                           'Not Seek','no info', '# of Salaries (Full-time Employed)', 'Salary Mean', 'Median Salary',
                           'Salary Low', 'Salary High', 'Bonus Numbers', 'Bonus Mean', 'Bonus   Median', 'Bonus Low', 'Bonus High'])
    
    for i in filled_undergrad['major']:
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
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Annual Salary'])].shape[0]
        data_list.append(data) ## of Salaries (Full-time Employed)^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = np.mean(data['Annual Salary']) 
        data_list.append(data) # Mean Salary^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = np.median(data['Annual Salary']) 
        data_list.append(data) # Median Salary^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = (data['Annual Salary'].min()) 
        data_list.append(data) # Salary Low^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data =  (data['Annual Salary'].max()) 
        data_list.append(data) # Salary high^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))].shape[0]
        data_list.append(data) # Bonus number^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = np.mean(data['Bonus Amount'])
        data_list.append(data) # Bonus Mean^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = np.median(data['Bonus Amount'])
        data_list.append(data) # Bonus Median^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = data['Bonus Amount'].min()
        data_list.append(data) # Bonus Low^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = data['Bonus Amount'].max()
        data_list.append(data) # Bonus High^
        s = pd.Series(data_list, index=df.columns)
        df = df.append(s, ignore_index=True)
    df.to_csv(r'D:\GitHub\Projects\NACE-Belmont\data\2019\export\bach.csv')
    Bachelors_by_major = df 
    return (Bachelors_by_major)
    



def Masters (rawdata):
    df = pd.DataFrame(columns=['major','Total Graduated','Full-Time','Part-Time','Faculty Tenure Track','Faculty Non-Tenure Track',
                           'Entrepreneur Full-Time', 'Entrepreneur Part-Time', 'Temp/Contract FT', 'Temp/Contract PT',
                           'Freelance  FT', 'Freelance PT', 'Fellowship/Intern FT', 'Fellowship/Intern PT',
                           'service', 'Military', 'Continuing Education', 'Seeking Employment', 'Seeking Education',
                           'Not Seek','no info', '# of Salaries (Full-time Employed)', 'Salary Mean', 'Median Salary',
                           'Salary Low', 'Salary High', 'Bonus Numbers', 'Bonus Mean', 'Bonus Median', 'Bonus Low', 'Bonus High'])

    for i in filled_graduate['major']:
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
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Annual Salary'])].shape[0]
        data_list.append(data) ## of Salaries (Full-time Employed)^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = np.mean(data['Annual Salary']) 
        data_list.append(data) # Mean Salary^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = np.median(data['Annual Salary']) 
        data_list.append(data) # Median Salary^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data = (data['Annual Salary'].min()) 
        data_list.append(data) # Salary Low^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education) & 
                       (rawdata['Annual Salary'])]
        data =  (data['Annual Salary'].max()) 
        data_list.append(data) # Salary high^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))].shape[0]
        data_list.append(data) # Bonus number^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = np.mean(data['Bonus Amount'])
        data_list.append(data) # Bonus Mean^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = np.median(data['Bonus Amount'])
        data_list.append(data) # Bonus Median^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = data['Bonus Amount'].min()
        data_list.append(data) # Bonus Low^
        data = rawdata[(rawdata['Recipient Primary Major'] == i) & 
                       (rawdata['Recipient Education Level'] == education)&
                       (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
        data = data['Bonus Amount'].max()
        data_list.append(data) # Bonus High^
        s = pd.Series(data_list, index=df.columns)
        df = df.append(s, ignore_index=True)
    df.to_csv(r'D:\GitHub\Projects\NACE-Belmont\data\2019\export\master.csv')
    df
    
    