import pandas as pd

# Part One
def load_data():
    employees = pd.read_csv('../data/employees.csv')
    sys_access = pd.read_csv('../data/system_access.csv')
    return employees, sys_access

# Part Two
def clean_data():
    sys_access = pd.read_csv('../data/system_access.csv')
    sys_access['id'] = 'EMP' + sys_access['id'].astype(str).str.zfill(6)
    return sys_access.head()

# Part Three
def combine_data(employees, sysaccess):
    employees = pd.read_csv('../data/employees.csv')
    sys_access = pd.read_csv('../data/system_access.csv')
    sys_access['id'] = 'EMP' + sys_access['id'].astype(str).str.zfill(6)
    sys_access.rename(columns={'id':'employee_number'}, inplace=True)
    sys_access.set_index('employee_number', inplace=True)
    employees.set_index('employee_number', inplace=True)
    df = employees.join(sys_access, how='left')
    return df

# Part Four
# Code: df_filter = df_combine.sort_values(by='access_level', ascending=True, na_position='first')

# Part Five
# Code: df_subset = df_clean['access_level'].isna()

