from logging import exception
import re
from tkinter.tix import COLUMN
import pandas as pd
import numpy as np
from datetime import datetime
from pyxlsb import open_workbook as open_xlsb

# 'Customer_Full_ID_Dll': int, , 'Sale_Date': 'datetime64[ns]'
DATA_DTYPE = {'Drug_Code': float, 'Drug_Desc': 'string', 'Atc5_Code': 'string', 'Quantity': float}
# ,Customer_Full_ID_Dll,Drug_Code,Drug_Desc,Atc5_Code,Sale_Date,Quantity
# 3284,0021013128,66817.0,STELARA PREFILL. 90MG 1PR,L04AC05,2018-06-27,1.0

DRUG_DESC_REG = r'[\u0590-\u05fe]|[0-9]+(\.[0-9]+)?ML? |\d{1,2}C\ |[A-z]\.?|[0-9]+X|[!-\-]|[\/]'


def load_data_to_df(data_path):
    print('starting load_data_to_df')
    path_suffix = re.sub(r'.*\.', '', data_path)
    df = []
    print(f"Formating file .{path_suffix}")

    if path_suffix == 'xlsb':
        for i in range(2,4): # number of sheets
            with open_xlsb(data_path) as wb:
                with wb.get_sheet(i) as sheet:
                    for row in sheet.rows():
                        df.append([item.v for item in row])
        df = pd.DataFrame(df[1:], columns=df[0])
    elif path_suffix == 'csv':
        df = pd.read_csv(data_path)
    elif path_suffix == 'xlsx':
        df = pd.read_excel(data_path)
    else:
        print(f'cannot recognize path suffix {path_suffix}')
        exit()
    return df

def add_sum(df):
    print('Starting add_sum')
    sum_list = []
    for _, row in df.iterrows():
        try:
            q = row['Quantity']
            # print(row['Drug_Desc'])
            tmp_srt = re.sub(DRUG_DESC_REG, ' ', row['Drug_Desc']).strip()
            a,b = tmp_srt.split()
            # print(f"Calculation: {a} * {b} * {q}")
            sum = eval(f"{a} * {b} * {q}")
            sum_list.append(sum)
            # print(row['sum'])
        except:
            print(f"Error in index ID: {_}, \n{tmp_srt}")
            print(row)
            exit()
    df['Quantity_Sum'] = sum_list

def daily_avg_per_person_per_atc_code(df):
    ## edit original df
    add_sum(df) 
    print('Starting daily_avg_per_person_per_atc_code')
    df.sort_values(['Customer_Full_ID_Dll','Atc5_Code','Sale_Date'], inplace=True)
    df_group = df.groupby(['Customer_Full_ID_Dll','Atc5_Code'], sort=False, as_index=False)
    # df_group_last = df.groupby(['Customer_Full_ID_Dll','Atc5_Code'], sort=False, as_index=False).last()

    # Cal days
    for _, group in df_group:
        ## Subtract last purchase
        group_sum = group.sum()['Quantity_Sum'] - group.iloc[-1]['Quantity_Sum'] #.reset_index(name='Total_By_Id_Atc_Code')
        
        if group_sum < 0:
            print(group_sum)

        f_date = group.iloc[0]['Sale_Date']
        l_date = group.iloc[-1]['Sale_Date']

        if (f_date != l_date):    
            f_d = datetime.strptime(f_date, "%Y-%m-%d")
            l_d = datetime.strptime(l_date, "%Y-%m-%d")
            days_diff = abs((l_d - f_d).days)
        else:
            days_diff = 1
        # print(f"diff between {f_date} and {f_date} is {days_diff} days")

        group['Sale_Date'] = days_diff
        group['Total_By_Id_Atc_Code'] = group_sum
        # print(f"{group_sum} / {days_diff}")
        group['Atc_Sum_Per_Day'] = round(group_sum / days_diff, 3) ## round with: group['Atc_Sum_Per_Day'] = round(group_sum / days_diff, 3)

        df = pd.concat([df, group]).drop_duplicates(subset=['Customer_Full_ID_Dll','Atc5_Code'], keep='last')

    df.rename(columns = {'Sale_Date':'Days'}, inplace=True)
    df.drop_duplicates(subset=['Customer_Full_ID_Dll','Atc5_Code'], keep='first', inplace=True)
    df.drop(columns=['Drug_Desc','Quantity','Quantity_Sum','Total_By_Id_Atc_Code'], inplace=True)
    df.sort_values(['Atc5_Code'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


def group_by_atc_code(df):
    print('Starting group_by_atc_code')
    ## Creates a new  df grouping by atc code and avging (mean) between the customers.
    ## Remove rows with 0 take per day
    df = df[df['Atc_Sum_Per_Day'] != 0.0]
    df['Customer_Full_ID_Dll'] = df['Customer_Full_ID_Dll'].astype(str)
    df_group = df.groupby(['Atc5_Code']).agg({'Customer_Full_ID_Dll': ','.join,
                                              'Atc_Sum_Per_Day': 'mean'})
    df_group['Atc_Sum_Per_Day'] = df_group['Atc_Sum_Per_Day'].apply(lambda x: round(x, 3))
    df_group.reset_index(inplace=True)
    return df_group


def single_row_per_customer(df):
    print('Starting single_row_per_customer')

    ## Remove rows with 0 take per day
    # df = df[df['Atc_Sum_Per_Day'] != 0.0]
    
    for index, row in df.iterrows():
        drug_column_name = row['Atc5_Code']
        days_column_name = 'Days_' + row['Atc5_Code']
        df.loc[index,days_column_name] = row['Days']
        df.loc[index,drug_column_name] = row['Atc_Sum_Per_Day']

    df = df.fillna(np.nan).groupby(['Customer_Full_ID_Dll']).first()
    df.drop(columns=['Unnamed: 0', 'Drug_Code', 'Atc5_Code', 'Days', 'Atc_Sum_Per_Day'], inplace=True)
    return df
-

if __name__ == "__main__":
    workdir = 'data/'
    data_path = f"{workdir}Psoriasis_Meuhedet_Data_drugs_formated.csv"
    # data_path = f"{workdir}example-data.xlsx"
    daily_avg_file = f"{workdir}daily_avg_file.csv"
    group_by_atc_file = f"{workdir}avg_by_atc_file.csv"
    group_by_id_file = f"{workdir}avg_by_id_file.csv"
    merge_df_file = f"{workdir}merged_df_file.csv"

    df = load_data_to_df(data_path)

    df_daily_avg = daily_avg_per_person_per_atc_code(df)
    with open(daily_avg_file, 'w') as daily_avg_file:
        df_daily_avg.to_csv(daily_avg_file)
    
    df_group_by_atc = group_by_atc_code(df_daily_avg)
    with open(group_by_atc_file, 'w') as group_by_atc_file:
        df_group_by_atc.to_csv(group_by_atc_file)


    df_customer_single_row = single_row_per_customer(df_daily_avg)
    with open(group_by_id_file, 'w') as group_by_id_file:
        df_customer_single_row.to_csv(group_by_id_file)


    df_patiants = load_data_to_df(f'{workdir}Psoriasis_Meuhedet_Data_patients.csv')

    heb = r'^[\u0590-\u05fe]+$'
    df_patiants.drop(columns=['Customer_Full_ID_Dll_test'], inplace=True)
    df_patiants.rename(columns={'Gender':'Gender (M)'}, inplace=True)
    df_patiants['Gender (M)'] = df_patiants['Gender (M)'].apply(lambda gender: re.sub(heb, '1', gender) if gender == 'זכר' else re.sub(heb, '0', gender))
    df_patiants['Birth_Year_Month'] = df_patiants['Birth_Year_Month'].apply(lambda birth: re.sub(heb, '', birth) if birth == 'אין מידע' else birth)
    df_patiants['Sector'] = df_patiants['Sector'].apply(lambda sector: re.sub(heb, 'General', sector) if sector == 'כללי'
                                            else ( re.sub(heb, 'Arabic', sector) if sector == 'ערבי'
                                                else re.sub(heb, 'Orthodox', sector))
                                        )
    with open(f'{workdir}Psoriasis_Meuhedet_Data_patients_formated.csv', 'w') as f:
        df_patiants.to_csv(f)

    df_patiants = pd.read_csv(f'{workdir}Psoriasis_Meuhedet_Data_patients_formated.csv', index_col=0)
    df_customer_single_row = pd.read_csv(group_by_id_file, index_col=0)
    
    merged_df = df_patiants.merge(df_customer_single_row, how='left', on='Customer_Full_ID_Dll')
    
    with open(merge_df_file, 'w'):
        # merged_df.sort_values(['Customer_Full_ID_Dll'], inplace=True) # .reset_index()
        # merged_df.drop(columns=['Unnamed: 0'])
        merged_df.to_csv(merge_df_file)