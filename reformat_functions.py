import tkinter as tk
import pandas as pd
import numpy as np
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfilename

rawdata = pd.read_csv(
    r"D:\Github\Projects\Belmont-OCPD\Data\2019\csv\Class of 2019 First Destination Survey Raw Data no identifiers scrubbed version 3.3.csv",
    encoding="ISO-8859-1")
global cip
cip = pd.read_csv(
    r"D:\Github\Projects\Belmont-OCPD\Data\2019\CIP codes\Argos Report.csv", encoding="ISO-8859-1"
)


def load_data_handshake():  # Loads the handshake data
    filename = askopenfilename()
    global rawdata
    rawdata = pd.read_csv(filename, encoding="ISO-8859-1")
    canvas1.create_window(350, 250, window=cip_button)
    button_import.destroy()


def load_cip_data():  # Loads the CIP data (typically from argos report)
    filename = askopenfilename()
    global cip
    cip = pd.read_csv(filename, encoding="ISO-8859-1")
    canvas1.create_window(350, 250, window=program_data_undergrad_button)
    canvas1.create_window(350, 200, window=program_data_masters_button)
    canvas1.create_window(350, 150, window=program_data_doctorate_button)
    canvas1.create_window(600, 250, window=overall_data_undergrad_button)
    canvas1.create_window(600, 200, window=overall_data_masters_button)
    canvas1.create_window(600, 150, window=overall_data_doctorate_button)
    cip_button.destroy()


def program_data_variables(major, education, rawdata, cip):
    try:
        program_data_variables.CIP_code = cip.loc[cip.MajorDesc == major, 'CIPCode'].values[0]
    except:
        program_data_variables.CIP_code = np.nan

    program_data_variables.total_graduated = rawdata[(rawdata['Recipient Primary Major'] == major) &
                                                     (rawdata['Recipient Education Level'] == education)].shape[0]

    program_data_variables.full_time = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                                               (rawdata['Recipient Primary Major'] == major) &
                                               (rawdata['Recipient Education Level'] == education)].shape[0]

    program_data_variables.part_time = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                                               (rawdata['Recipient Primary Major'] == major) &
                                               (rawdata['Recipient Education Level'] == education)].shape[0]

    program_data_variables.entrepreneur_ft = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                                                     (rawdata['Recipient Primary Major'] == major) &
                                                     (rawdata['Recipient Education Level'] == education) &
                                                     (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]

    program_data_variables.entrepreneur_pt = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                                                     (rawdata['Recipient Primary Major'] == major) &
                                                     (rawdata['Recipient Education Level'] == education) &
                                                     (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]

    program_data_variables.temp_contract_ft = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                                                      (rawdata['Recipient Primary Major'] == major) &
                                                      (rawdata['Recipient Education Level'] == education) &
                                                      (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]

    program_data_variables.temp_contract_pt = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                                                      (rawdata['Recipient Primary Major'] == major) &
                                                      (rawdata['Recipient Education Level'] == education) &
                                                      (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]

    program_data_variables.freelance_ft = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                                                  (rawdata['Recipient Primary Major'] == major) &
                                                  (rawdata['Recipient Education Level'] == education) &
                                                  (rawdata['Employment Category'] == 'Freelancer')].shape[0]

    program_data_variables.freelance_pt = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                                                  (rawdata['Recipient Primary Major'] == major) &
                                                  (rawdata['Recipient Education Level'] == education) &
                                                  (rawdata['Employment Category'] == 'Freelancer')].shape[0]

    program_data_variables.faculty_tenure = rawdata[(rawdata['Recipient Education Level'] == education) &
                                                    (rawdata['Recipient Primary Major'] == major) &
                                                    (rawdata['Employment Category'] == 'Faculty Tenure')].shape[0]

    program_data_variables.faculty_nontenure = rawdata[(rawdata['Recipient Education Level'] == education) &
                                                       (rawdata['Recipient Primary Major'] == major) &
                                                       (rawdata['Employment Category'] == 'Faculty Non-Tenure')].shape[0]

    data1 = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Internship'] == 'Yes')].shape[0]
    data2 = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
    program_data_variables.fellowship_intern_ft = data1 + data2

    data1 = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                    (rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Internship'] == 'Yes')].shape[0]
    data2 = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                    (rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
    program_data_variables.fellowship_intern_pt = data1 + data2

    program_data_variables.outcome_service = rawdata[(rawdata['Recipient Primary Major'] == major) &
                                                     (rawdata['Recipient Education Level'] == education) &
                                                     (rawdata['Outcome'] == 'Volunteering')].shape[0]

    program_data_variables.outcome_military = rawdata[(rawdata['Recipient Primary Major'] == major) &
                                                      (rawdata['Recipient Education Level'] == education) &
                                                      (rawdata['Outcome'] == 'Military')].shape[0]

    program_data_variables.outcome_continue_education = rawdata[(rawdata['Recipient Primary Major'] == major) &
                                                                (rawdata['Recipient Education Level'] == education) &
                                                                (rawdata['Outcome'] == 'Continuing Education')].shape[0]

    program_data_variables.outcome_still_looking = rawdata[(rawdata['Recipient Primary Major'] == major) &
                                                           (rawdata['Recipient Education Level'] == education) &
                                                           (rawdata['Still Looking Option'] == 'Employment')].shape[0]

    program_data_variables.outcome_seeking_education = rawdata[(rawdata['Recipient Primary Major'] == major) &
                                                               (rawdata['Recipient Education Level'] == education) &
                                                               (rawdata['Still Looking Option'] == 'Continuing Education')].shape[0]

    program_data_variables.outcome_not_seeking = rawdata[(rawdata['Recipient Primary Major'] == major) &
                                                         (rawdata['Recipient Education Level'] == education) &
                                                         (rawdata['Outcome'] == 'Not Seeking')].shape[0]

    program_data_variables.no_info = rawdata[(rawdata['Recipient Primary Major'] == major) &
                                             (rawdata['Recipient Education Level'] == education) &
                                             (pd.isna(rawdata['Outcome']))].shape[0]

    program_data_variables.salaries_ft = rawdata[(rawdata['Recipient Primary Major'] == major) &
                                                 (rawdata['Employment Type'] == 'Full-Time') &
                                                 (rawdata['Recipient Education Level'] == education) &
                                                 (rawdata['Annual Salary'])].shape[0]

    data1 = rawdata[(rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Annual Salary'])]
    program_data_variables.salaries_mean = np.mean(data1['Annual Salary'])

    data1 = rawdata[(rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Annual Salary'])]
    program_data_variables.salaries_median = np.median(data1['Annual Salary'])

    data1 = rawdata[(rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Annual Salary'])]
    program_data_variables.salaries_low = (data1['Annual Salary'].min())

    data1 = rawdata[(rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Annual Salary'])]
    program_data_variables.salaries_high = (data1['Annual Salary'].max())

    program_data_variables.bonus = rawdata[(rawdata['Recipient Primary Major'] == major) &
                                           (rawdata['Employment Type'] == 'Full-Time') &
                                           (rawdata['Recipient Education Level'] == education) &
                                           (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))].shape[0]

    data1 = rawdata[(rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
    program_data_variables.bonus_mean = np.mean(data1['Bonus Amount'])

    data1 = rawdata[(rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
    program_data_variables.bonus_median = np.median(data1['Bonus Amount'])

    data1 = rawdata[(rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
    program_data_variables.bonus_low = data1['Bonus Amount'].min()

    data1 = rawdata[(rawdata['Recipient Primary Major'] == major) &
                    (rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))]
    program_data_variables.bonus_high = data1['Bonus Amount'].max()
    return ()


def overall_data_variables(education, rawdata):
    overall_data_variables.total_graduated = rawdata[(rawdata['Recipient Education Level'] == education)].shape[0]

    overall_data_variables.ft = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                                        (rawdata['Recipient Education Level'] == education)].shape[0]

    overall_data_variables.pt = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                                        (rawdata['Recipient Education Level'] == education)].shape[0]

    overall_data_variables.entrepreneur_ft = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                                                     (rawdata['Recipient Education Level'] == education) &
                                                     (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]

    overall_data_variables.entrepreneur_pt = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                                                     (rawdata['Recipient Education Level'] == education) &
                                                     (rawdata['Employment Category'] == 'Entrepreneur')].shape[0]

    overall_data_variables.temp_contract_ft = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                                                      (rawdata['Recipient Education Level'] == education) &
                                                      (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]

    overall_data_variables.temp_contract_pt = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                                                      (rawdata['Recipient Education Level'] == education) &
                                                      (rawdata['Employment Category'] == 'Temporary/Contract Work Assignment')].shape[0]

    overall_data_variables.freelance_ft = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                                                  (rawdata['Recipient Education Level'] == education) &
                                                  (rawdata['Employment Category'] == 'Freelancer')].shape[0]

    overall_data_variables.freelance_pt = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                                                  (rawdata['Recipient Education Level'] == education) &
                                                  (rawdata['Employment Category'] == 'Freelancer')].shape[0]

    data1 = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Internship'] == 'Yes')].shape[0]
    data2 = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
    overall_data_variables.fellowship_intern_ft = data1 + data2

    data1 = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Internship'] == 'Yes')].shape[0]
    data2 = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                    (rawdata['Recipient Education Level'] == education) &
                    (rawdata['Is Fellowship?'] == 'Yes')].shape[0]
    overall_data_variables.fellowship_intern_pt = data1 + data2

    overall_data_variables.outcome_service = rawdata[(rawdata['Recipient Education Level'] == education) &
                                                     (rawdata['Outcome'] == 'Volunteering')].shape[0]

    overall_data_variables.outcome_military = rawdata[(rawdata['Recipient Education Level'] == education) &
                                                      (rawdata['Outcome'] == 'Military')].shape[0]

    overall_data_variables.outcome_continue_education = rawdata[(rawdata['Recipient Education Level'] == education) &
                                                                (rawdata['Outcome'] == 'Continuing Education')].shape[0]

    overall_data_variables.outcome_still_looking = rawdata[(rawdata['Recipient Education Level'] == education) &
                                                           (rawdata['Still Looking Option'] == 'Employment')].shape[0]

    overall_data_variables.outcome_seeking_education = rawdata[(rawdata['Recipient Education Level'] == education) &
                                                               (rawdata['Still Looking Option'] == 'Continuing Education')].shape[0]

    overall_data_variables.outcome_not_seeking = rawdata[(rawdata['Recipient Education Level'] == education) &
                                                         (rawdata['Outcome'] == 'Not Seeking')].shape[0]

    overall_data_variables.no_info = rawdata[(rawdata['Recipient Education Level'] == education) &
                                             (pd.isna(rawdata['Outcome']))].shape[0]

    overall_data_variables.salaries_ft = rawdata[(rawdata['Recipient Education Level'] == education) &
                                                 (rawdata['Employment Type'] == 'Full-Time') &
                                                 (rawdata['Annual Salary'])].shape[0]

    data = rawdata[(rawdata['Recipient Education Level'] == education) &
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Annual Salary'])]
    overall_data_variables.salaries_mean = np.mean(data['Annual Salary'])

    data = rawdata[(rawdata['Recipient Education Level'] == education) &
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Annual Salary'])]
    overall_data_variables.salaries_median = np.median(data['Annual Salary'])

    overall_data_variables.bonus = rawdata[(rawdata['Recipient Education Level'] == education) &
                                           (rawdata['Employment Type'] == 'Full-Time') &
                                           (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))].shape[0]

    data = rawdata[(rawdata['Recipient Education Level'] == education) &
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Bonus Amount'] != 0) &
                   (pd.notna(rawdata['Bonus Amount']))]
    overall_data_variables.bonus_mean = np.mean(data['Bonus Amount'])

    data = rawdata[(rawdata['Recipient Education Level'] == education) &
                   (rawdata['Employment Type'] == 'Full-Time') &
                   (rawdata['Bonus Amount'] != 0) &
                   (pd.notna(rawdata['Bonus Amount']))]
    overall_data_variables.bonus_median = np.median(data['Bonus Amount'])
    return ()


def associate_program_data_function():
    education = 'Associate'
    education_level = rawdata[rawdata["Recipient Education Level"].str.startswith(education, na=False)]
    majors = education_level['Recipient Primary Major'].unique()
    majors = pd.DataFrame(majors, columns=['major'])
    df = pd.DataFrame(columns=['Academic Program Name',
                               'CIP Code',
                               'Total Graduated',
                               'Full-Time',
                               'Part-Time',
                               'Entrepreneur Full-Time',
                               'Entrepreneur Part-Time',
                               'Temp/Contract FT',
                               'Temp/Contract PT',
                               'Freelance  FT',
                               'Freelance PT',
                               'Fellowship/Intern FT',
                               'Fellowship/Intern PT',
                               'service',
                               'Military',
                               'Continuing Education',
                               'Seeking Employment',
                               'Seeking Education',
                               'Not Seek',
                               'no info',
                               '# of Salaries (Full-time Employed)',
                               'Salary Mean',
                               'Median Salary',
                               'Salary Low',
                               'Salary High',
                               'Bonus Numbers',
                               'Bonus Mean',
                               'Bonus Median',
                               'Bonus Low',
                               'Bonus High'])
    for i in majors['major']:
        program_data_variables(i, education, rawdata=rawdata, cip=cip)
        print(cip)
        data_list = []
        df_list = [i,
                   program_data_variables.CIP_code,
                   program_data_variables.total_graduated,
                   program_data_variables.full_time,
                   program_data_variables.part_time,
                   program_data_variables.entrepreneur_ft,
                   program_data_variables.entrepreneur_pt,
                   program_data_variables.temp_contract_ft,
                   program_data_variables.temp_contract_pt,
                   program_data_variables.freelance_ft,
                   program_data_variables.freelance_pt,
                   program_data_variables.fellowship_intern_ft,
                   program_data_variables.fellowship_intern_pt,
                   program_data_variables.outcome_service,
                   program_data_variables.outcome_military,
                   program_data_variables.outcome_continue_education,
                   program_data_variables.outcome_still_looking,
                   program_data_variables.outcome_seeking_education,
                   program_data_variables.outcome_not_seeking,
                   program_data_variables.no_info,
                   program_data_variables.salaries_ft,
                   program_data_variables.salaries_mean,
                   program_data_variables.salaries_median,
                   program_data_variables.salaries_low,
                   program_data_variables.salaries_high,
                   program_data_variables.bonus,
                   program_data_variables.bonus_mean,
                   program_data_variables.bonus_median,
                   program_data_variables.bonus_low,
                   program_data_variables.bonus_high
                   ]
        for var in df_list:
            data_list.append(var)
        s = pd.Series(data_list, index=df.columns)
        df = df.append(s, ignore_index=True)
        print(df)
    filename = asksaveasfile(defaultextension=".csv",
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*")))
    df.to_csv(filename, line_terminator='\n')
    return df


def associate_overall_data_function():
    return df


def bachelors_program_data_function():
    education = 'Bachelors'
    education_level = rawdata[rawdata["Recipient Education Level"].str.startswith(education, na=False)]
    majors = education_level['Recipient Primary Major'].unique()
    majors = pd.DataFrame(majors, columns=['major'])
    df = pd.DataFrame(columns=['Academic Program Name',
                               'CIP Code',
                               'Total Graduated',
                               'Full-Time',
                               'Part-Time',
                               'Entrepreneur Full-Time',
                               'Entrepreneur Part-Time',
                               'Temp/Contract FT',
                               'Temp/Contract PT',
                               'Freelance  FT',
                               'Freelance PT',
                               'Fellowship/Intern FT',
                               'Fellowship/Intern PT',
                               'service',
                               'Military',
                               'Continuing Education',
                               'Seeking Employment',
                               'Seeking Education',
                               'Not Seek',
                               'no info',
                               '# of Salaries (Full-time Employed)',
                               'Salary Mean',
                               'Median Salary',
                               'Salary Low',
                               'Salary High',
                               'Bonus Numbers',
                               'Bonus Mean',
                               'Bonus Median',
                               'Bonus Low',
                               'Bonus High'])
    for i in majors['major']:
        program_data_variables(i, education, rawdata=rawdata, cip=cip)
        print(cip)
        data_list = []
        df_list = [i,
                   program_data_variables.CIP_code,
                   program_data_variables.total_graduated,
                   program_data_variables.full_time,
                   program_data_variables.part_time,
                   program_data_variables.entrepreneur_ft,
                   program_data_variables.entrepreneur_pt,
                   program_data_variables.temp_contract_ft,
                   program_data_variables.temp_contract_pt,
                   program_data_variables.freelance_ft,
                   program_data_variables.freelance_pt,
                   program_data_variables.fellowship_intern_ft,
                   program_data_variables.fellowship_intern_pt,
                   program_data_variables.outcome_service,
                   program_data_variables.outcome_military,
                   program_data_variables.outcome_continue_education,
                   program_data_variables.outcome_still_looking,
                   program_data_variables.outcome_seeking_education,
                   program_data_variables.outcome_not_seeking,
                   program_data_variables.no_info,
                   program_data_variables.salaries_ft,
                   program_data_variables.salaries_mean,
                   program_data_variables.salaries_median,
                   program_data_variables.salaries_low,
                   program_data_variables.salaries_high,
                   program_data_variables.bonus,
                   program_data_variables.bonus_mean,
                   program_data_variables.bonus_median,
                   program_data_variables.bonus_low,
                   program_data_variables.bonus_high
                   ]
        for var in df_list:
            data_list.append(var)
        s = pd.Series(data_list, index=df.columns)
        df = df.append(s, ignore_index=True)
    filename = asksaveasfile(defaultextension=".csv",
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*")))
    df.to_csv(filename, line_terminator='\n')
    return df


def bachelors_overall_data_function():
    df = pd.DataFrame(columns=['Total Graduated', 'Full-Time', 'Part-Time', 'Entrepreneur Full-Time',
                               'Entrepreneur Part-Time', 'Temp/Contract FT', 'Temp/Contract PT', 'Freelance  FT', 'Freelance PT',
                               'Fellowship/Intern FT', 'Fellowship/Intern PT',
                               'Service', 'Military', 'Continuing Education', 'Seeking Employment', 'Seeking Education',
                               'Not Seek', 'no info', '# of Salaries (Full-time Employed)', 'Salary Mean', 'Median Salary',
                               'Recieving Bonus', 'Bonus Mean', 'Bonus Median'])
    data_list = []
    education = 'Bachelors'
    df_list = [overall_data_variables.total_graduated,
               overall_data_variables.ft,
               overall_data_variables.pt]
    for i in df_list:
        data_list.append(i)

    return df


def masters_program_data_function():
    education = 'Masters'
    education_level = rawdata[rawdata["Recipient Education Level"].str.startswith(education, na=False)]
    majors = education_level['Recipient Primary Major'].unique()
    majors = pd.DataFrame(majors, columns=['major'])
    df = pd.DataFrame(columns=['Academic Program Name',
                               'CIP Code',
                               'Total Graduated',
                               'Full-Time',
                               'Part-Time',
                               'Faculty Tenure Track',
                               'Faculty Non-Tenure Track',
                               'Entrepreneur Full-Time',
                               'Entrepreneur Part-Time',
                               'Temp/Contract FT',
                               'Temp/Contract PT',
                               'Freelance  FT',
                               'Freelance PT',
                               'Fellowship/Intern FT',
                               'Fellowship/Intern PT',
                               'service',
                               'Military',
                               'Continuing Education',
                               'Seeking Employment',
                               'Seeking Education',
                               'Not Seek',
                               'no info',
                               '# of Salaries (Full-time Employed)',
                               'Salary Mean',
                               'Median Salary',
                               'Salary Low',
                               'Salary High',
                               'Bonus Numbers',
                               'Bonus Mean',
                               'Bonus Median',
                               ])
    for i in majors['major']:
        program_data_variables(i, education, rawdata=rawdata)
        data_list = []
        df_list = [i,
                   program_data_variables.total_graduated,
                   program_data_variables.full_time,
                   program_data_variables.part_time,
                   program_data_variables.faulty_tenure,
                   program_data_variables.faculty_nontenure,
                   program_data_variables.entrepreneur_ft,
                   program_data_variables.entrepreneur_pt,
                   program_data_variables.temp_contract_ft,
                   program_data_variables.temp_contract_pt,
                   program_data_variables.freelance_ft,
                   program_data_variables.freelance_pt,
                   program_data_variables.fellowship_intern_ft,
                   program_data_variables.fellowship_intern_pt,
                   program_data_variables.outcome_service,
                   program_data_variables.outcome_military,
                   program_data_variables.outcome_continue_education,
                   program_data_variables.outcome_still_looking,
                   program_data_variables.outcome_seeking_education,
                   program_data_variables.outcome_not_seeking,
                   program_data_variables.no_info,
                   program_data_variables.salaries_ft,
                   program_data_variables.salaries_mean,
                   program_data_variables.salaries_median,
                   program_data_variables.salaries_low,
                   program_data_variables.salaries_high,
                   program_data_variables.bonus,
                   program_data_variables.bonus_mean,
                   program_data_variables.bonus_median,
                   ]
        for var in df_list:
            data_list.append(var)
            # print(var)
            # print (data_list)
        # print(data_list)
        s = pd.Series(data_list, index=df.columns)
        # print(s)
        df = df.append(s, ignore_index=True)
        # print(df)
    filename = asksaveasfile(defaultextension=".csv",
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*")))
    df.to_csv(filename, line_terminator='\n')
    return df


def masters_overall_data_function():
    return df


def doctorate_program_data_function():
    education = 'Doctorate'
    education_level = rawdata[rawdata["Recipient Education Level"].str.startswith(education, na=False)]
    majors = education_level['Recipient Primary Major'].unique()
    majors = pd.DataFrame(majors, columns=['major'])
    df = pd.DataFrame(columns=['Academic Program Name',
                               'CIP Code',
                               'Total Graduated',
                               'Full-Time',
                               'Part-Time',
                               'Faculty Tenure Track',
                               'Faculty Non-Tenure Track',
                               'Entrepreneur Full-Time',
                               'Entrepreneur Part-Time',
                               'Temp/Contract FT',
                               'Temp/Contract PT',
                               'Freelance  FT',
                               'Freelance PT',
                               'Fellowship/Intern FT',
                               'Fellowship/Intern PT',
                               'service',
                               'Military',
                               'Continuing Education',
                               'Seeking Employment',
                               'Seeking Education',
                               'Not Seek',
                               'no info',
                               '# of Salaries (Full-time Employed)',
                               'Salary Mean',
                               'Median Salary',
                               'Salary Low',
                               'Salary High',
                               'Bonus Numbers',
                               'Bonus Mean',
                               'Bonus Median',
                               'Bonus Low',
                               'Bonus High'
                               ])
    for i in majors['major']:
        program_data_variables(i, education, rawdata=rawdata)
        data_list = []
        df_list = [i,
                   program_data_variables.CIP_code,
                   program_data_variables.total_graduated,
                   program_data_variables.full_time,
                   program_data_variables.part_time,
                   program_data_variables.faulty_tenure,
                   program_data_variables.faculty_nontenure,
                   program_data_variables.entrepreneur_ft,
                   program_data_variables.entrepreneur_pt,
                   program_data_variables.temp_contract_ft,
                   program_data_variables.temp_contract_pt,
                   program_data_variables.freelance_ft,
                   program_data_variables.freelance_pt,
                   program_data_variables.fellowship_intern_ft,
                   program_data_variables.fellowship_intern_pt,
                   program_data_variables.outcome_service,
                   program_data_variables.outcome_military,
                   program_data_variables.outcome_continue_education,
                   program_data_variables.outcome_still_looking,
                   program_data_variables.outcome_seeking_education,
                   program_data_variables.outcome_not_seeking,
                   program_data_variables.no_info,
                   program_data_variables.salaries_ft,
                   program_data_variables.salaries_mean,
                   program_data_variables.salaries_median,
                   program_data_variables.salaries_low,
                   program_data_variables.salaries_high,
                   program_data_variables.bonus,
                   program_data_variables.bonus_mean,
                   program_data_variables.bonus_median,
                   program_data_variables.bonus_low,
                   program_data_variables.bonus_high
                   ]
        for var in df_list:
            data_list.append(var)
            # print(var)
            # print (data_list)
        # print(data_list)
        s = pd.Series(data_list, index=df.columns)
        # print(s)
        df = df.append(s, ignore_index=True)
        # print(df)
    filename = asksaveasfile(defaultextension=".csv",
                             filetypes=(("Comma-separated values file", "*.csv"),
                                        ("All Files", "*.*")))
    df.to_csv(filename, line_terminator='\n')
    return df


def doctorate_overall_data_function():
    return df


bachelors_program_data_function()

root = tk.Tk()
canvas1 = tk.Canvas(root, width=700, height=500)
canvas1.pack()
button_import = tk.Button(root, text='Select .CSV Handshake Data', command=load_data_handshake)
canvas1.create_window(350, 250, window=button_import)

cip_button = tk.Button(root, text='Select .CSV CIP Data (argos report)', command=load_cip_data)

program_data_undergrad_button = tk.Button(root, text='Save Undergraduate program data', command=bachelors_program_data_function)
program_data_masters_button = tk.Button(root, text='Save Masters program data', command=masters_program_data_function)
program_data_doctorate_button = tk.Button(root, text='Save Doctorate program data', command=doctorate_program_data_function)

overall_data_undergrad_button = tk.Button(root, text='Save Undergraduate overall data', command=bachelors_overall_data_function)
overall_data_masters_button = tk.Button(root, text='Save Masters overall data', command=masters_overall_data_function)
overall_data_doctorate_button = tk.Button(root, text='Save Doctorate overall data', command=doctorate_overall_data_function)

root.mainloop()
