import pandas as pd
import numpy as np

rawdata = pd.read_csv(
    r"D:\Github\Projects\Belmont-OCPD\Data\2019\csv\Class of 2019 First Destination Survey Raw Data no identifiers scrubbed version 3.3.csv",
    encoding="ISO-8859-1")
print(rawdata)


def program_data_variables(major, education, rawdata):
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
                                                      (rawdata[
                                                           'Employment Category'] == 'Temporary/Contract Work Assignment')].shape[
        0]
    program_data_variables.temp_contract_pt = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                                                      (rawdata['Recipient Primary Major'] == major) &
                                                      (rawdata['Recipient Education Level'] == education) &
                                                      (rawdata[
                                                           'Employment Category'] == 'Temporary/Contract Work Assignment')].shape[
        0]
    program_data_variables.freelance_ft = rawdata[(rawdata['Employment Type'] == 'Full-Time') &
                                                  (rawdata['Recipient Primary Major'] == major) &
                                                  (rawdata['Recipient Education Level'] == education) &
                                                  (rawdata['Employment Category'] == 'Freelancer')].shape[0]
    program_data_variables.freelance_pt = rawdata[(rawdata['Employment Type'] == 'Part-Time') &
                                                  (rawdata['Recipient Primary Major'] == major) &
                                                  (rawdata['Recipient Education Level'] == education) &
                                                  (rawdata['Employment Category'] == 'Freelancer')].shape[0]

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

    program_data_variables.outcome_volunteering = rawdata[(rawdata['Recipient Primary Major'] == major) &
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
                                                               (rawdata[
                                                                    'Still Looking Option'] == 'Continuing Education')].shape[
        0]
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
                                           (rawdata['Bonus Amount'] != 0) & (pd.notna(rawdata['Bonus Amount']))].shape[
        0]

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

def masters_program_data_function():
    education = 'Masters'
    education_level = rawdata[rawdata["Recipient Education Level"].str.startswith(education, na=False)]
    majors = education_level['Recipient Primary Major'].unique()
    majors = pd.DataFrame(majors, columns=['major'])

    df = pd.DataFrame(columns=['major','Total Graduated','Full-Time','Part-Time', 'Entrepreneur Full-Time',
                               'Entrepreneur Part-Time', 'Temp/Contract FT', 'Temp/Contract PT',
                               'Freelance  FT', 'Freelance PT', 'Fellowship/Intern FT', 'Fellowship/Intern PT',
                               'service', 'Military', 'Continuing Education', 'Seeking Employment', 'Seeking Education',
                               'Not Seek','no info', '# of Salaries (Full-time Employed)', 'Salary Mean', 'Median Salary',
                               'Salary Low', 'Salary High', 'Bonus Numbers', 'Bonus Mean', 'Bonus Median', 'Bonus Low', 'Bonus High'])
    for i in majors['major']:
        data_list = []
        df_list=[i, program_data_variables.total_graduated, program_data_variables.full_time, program_data_variables.part_time,
                 program_data_variables.entrepreneur_ft]
        program_data_variables(i, education, rawdata=rawdata)
        data_list.append(program_data_variables.total_graduated)
        for var in df_list:
            data_list.append(var)

#masters_program_data_function()