import pandas as pd
from datetime import datetime
import re

REG_DRUG_DESC = r'[A-z]|[!-/]|1X'
## ex. CIPRALEX 10MG 28TAB


def add_sum(df):
    sum_list = []
    for _, row in df.iterrows():
        q = row['Quantity']
        tmp_srt = re.sub(REG_DRUG_DESC, '', row['Drug_Desc']).strip()
        # print(tmp_srt)
        a,b = tmp_srt.split(' ')
        # print(f"Calculation: {a} * {b} * {q}")
        sum = eval(f"{a} * {b} * {q}")
        sum_list.append(sum)
        # print(row['sum'])
    df['Quantity_Sum'] = sum_list

def daily_avg_per_person_per_atc_code(df):
    df = df.sort_values(['Customer_Full_ID_Dll','Atc5_Code','Sale_Date'])
    df_group = df.groupby(['Customer_Full_ID_Dll','Atc5_Code'], sort=False, as_index=False)

    # Cal days
    for name, group in df_group:
        group_sum = group.sum()['Quantity_Sum'] #.reset_index(name='Total_By_Id_Atc_Code')
        # print(group_sum)

        f_date = group.iloc[0]['Sale_Date']
        l_date = group.iloc[-1]['Sale_Date']
        # print(f_date)
        # print(l_date)

        if (f_date != l_date):    
            f_d = datetime.strptime(f_date, "%Y-%m-%d")
            l_d = datetime.strptime(l_date, "%Y-%m-%d")
            days_diff = abs((l_d - f_d).days)
        else:
            days_diff = 1
        # print(f"diff between {f_date} and {f_date} is {days_diff} days") ## not including the last day

        group['Total_By_Id_Atc_Code'] = group_sum
        # print(f"{group_sum} / {days_diff}")
        group['Atc_Sum_Per_Day'] = (group_sum / days_diff) ## round with: group['Atc_Sum_Per_Day'] = round(group_sum / days_diff, 3)
        # print(group)

        # pd.merge(df, df_group, on=['Customer_Full_ID_Dll','Atc5_Code'], how='inner',suffixes=('_123','_456'))
        df = pd.concat([df, group]).drop_duplicates(subset=['Customer_Full_ID_Dll','Atc5_Code'], keep='last')
        # df = pd.merge(df, group, on='ID')

    return df

    # Copy of df:
    
    # df_group_by = df_group_by['sum'].sum().reset_index(name='Total_By_Id_Atc_Code')

    # devide
    
    # with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #     print(df_days)
    # print(df_group_by)





if __name__ == "__main__":
    path = 'example-data.xlsx'
    new_path = 'formated.csv'
    df = pd.read_excel(path)
    add_sum(df) # edit original df
    df = daily_avg_per_person_per_atc_code(df)
    # print(df)
    df = df.drop_duplicates(subset=['Customer_Full_ID_Dll','Atc5_Code'], keep='first')

    with open(new_path, 'w') as f:
        df.to_csv(f)


