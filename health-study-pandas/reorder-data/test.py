from dataclasses import replace
import re
import pandas as pd
import re
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Get a formated string containing two space seperated numbers.
# 1- {} - amount of active matirial (usually in mg).
# 2- {} - number of pills/syringes.
# [\u0590-\u05fe] all hebrew letters

global DRUG_DESC_REG
DRUG_DESC_REG = r'[\u0590-\u05fe]|[0-9]+(\.[0-9]+)?ML? |\d{1,2}C\ |[A-z]\.?|[0-9]+X|[!-\-]|[\/]'
global result_regex
result_regex = r'^\d{1,3}(\.?\d{1,})?[\ ]{1,}\d{1,3}(\.\d{1,})?$'


def test_regex_test(string):
    formated_string = re.sub(DRUG_DESC_REG, '', string).strip()
    return formated_string

def test_regex():
    string_list = [
        "CIPRALEX 10MG 28TAB",
        "FLUTINE 20MG 30CAP",
        "HUMIRA 40MG/0.8ML 2PRS",
        "HUMIRA 40MG/0.85ML 2PRS",
        "SIMPONI 1X 50MG 1SYRINGE",
        "SIMPONI 15X 50MG 1SYRINGE",
        "LUSTRAL 29C 50MG 28TAB",
        "STELARA PREFILL. 90MG 1PR",
        "REMICADE 100MG/VIA 1VIAL",
        "METHOTREXAT EBE.PFS 10MG/",
        "METHOTREXAT 7.5MG/0.375ML",
        "METHOTREXAT 12.5MG/0.625M",
        "FLUOXETINE הכנות SYR 10MG",

        "1 ",
        "1 2",
        "10 28",
        "100 28",
        "10 280",
        "100 280",
        "1000 280",
        # "100 2800",

        "1.5 2",
        "10.5 28",
        "100.5 28",
        "10.5 280",
        "100.5 280",
        # "1000.5 280",
        # "100.5 2800",

        "1 2.5",
        "10 28.5",
        "100 28.5",
        # "10 280.5",
        # "100 280.5",
        # "1000 280.5",
        # "100 2800.5",
    ]
    for test_string in string_list:
        string = test_regex_test(test_string)
        if not re.match(result_regex, string):
            print(f"{bcolors.WARNING} ERROR: '{test_string}': ({string}), Does not match regex {bcolors.ENDC}")
        # else:
        #     print(f"{bcolors.OKGREEN} '{string}' {bcolors.ENDC}")

def edit_drugs_file_add_1(df, regex_match):
    df['Drug_Desc'] = df['Drug_Desc'].apply(lambda desc: (desc + ' 1') if re.match(regex_match, desc) else desc)
    return df

def edit_drugs_file_remove_ml_add_one(df, regex_match):
    df['Drug_Desc'] = df['Drug_Desc'].apply(lambda desc: (desc.replace('ML', '') + ' 1') if re.match(regex_match, desc) else desc)
    return df

def edit_drugs_file_remove_ints_add_zero_zero(df, regex_match):
    df['Drug_Desc'] = df['Drug_Desc'].apply(lambda desc: (re.sub(r'[0-9]+', '', desc) + ' 0 0') if re.match(regex_match, desc) else desc)
    return df

def print_regex_rejects(df):
    # df['Drug_Desc'].apply(lambda desc: print(f"{re.sub(DRUG_DESC_REG, ' ', desc).strip()}\n{desc}") if not re.match(result_regex, re.sub(DRUG_DESC_REG, ' ', desc).strip()) else desc)
    # df.apply(lambda row: print(f"{re.sub(DRUG_DESC_REG, ' ', row['Drug_Desc']).strip()}\n{row['Drug_Desc']}") if not re.match(result_regex, re.sub(DRUG_DESC_REG, ' ', row['Drug_Desc']).strip()) else row)
    for index, row in df.iterrows():
        formated = re.sub(DRUG_DESC_REG, ' ', row['Drug_Desc']).strip()
        if not re.match(result_regex, formated):
            print(f"{row['Drug_Desc']}, {formated}")

if __name__ == '__main__':
    # test_regex()
    # path = 'data/Psoriasis_Meuhedet_Data_drugs_formated.csv'
    path = 'data/daily_avg_file copy.csv'
    
    with open(path):
        df = pd.read_csv(path, index_col=0)

    # print_regex_rejects(df)

    # regex_match_1 = r'^METHOTREXAT .*?MG\/?$'
    # df = edit_drugs_file_add_1(df, regex_match_1)
    # regex_match_2 = r'^METHOTREXAT .*?ML?$'
    # df = edit_drugs_file_add_1(df, regex_match_2)
    # regex_match_3 = r'^FLUOXETINE .*?ML'
    # df = edit_drugs_file_remove_ml_add_one(df, regex_match_3)
    # regex_match_4 = r'^SULFASALAZINE .*?ML'
    # df = edit_drugs_file_remove_ml_add_one(df, regex_match_4)
    # regex_match_5 = r'^METHOTREXATE MAYAN SOL 2.$'
    # df = edit_drugs_file_remove_ints_add_zero_zero(df, regex_match_5)
    # regex_match_6 = r'^SULFASALAZINE S-PHARM.*?$'
    # df = edit_drugs_file_remove_ints_add_zero_zero(df, regex_match_6)
    
    # df.drop(columns=['Drug_Code', 'Atc5_Code', 'Unnamed: 0', 'Days', 'Atc_Sum_Per_Day'], inplace=True)
    df.drop(columns=['Unnamed: 0'], inplace=True)
    path_2 = 'data/daily_avg_file.csv'
    with open(path_2, 'w') as f:
        df.to_csv(f)