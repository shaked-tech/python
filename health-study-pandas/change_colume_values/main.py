from pickletools import read_long1
import pandas as pd
import re
# def change_date(df):


# [19-20][0-9]{2}
# RE = r'^[0-9]{4}-(0[1-9]|[10-12])-(0[1-9]|[10-31])'
if __name__ == "__main__":
    re_year = '(19|20)[0-9]{2}'
    re_month = '(0[1-9]|1[0-2])'
    re_day = '([012][0-9]|3[0-1])'
    RE1 = rf'^{re_year}-{re_month}-{re_day}' # 2008-12-31
    RE2 = rf'^{re_day}/{re_month}/{re_year}' # 31/12/2008

    df = pd.read_csv('Summarized_Psoriasis.csv')
    # df = pd.read_csv('test.csv', index_col=0)
    # change_date(df)
    for column_name, column_values in df.iteritems():
        for i, value in enumerate(column_values):
            try:
                if re.match(RE1, value) or re.match(RE2, value):
                    # print(f"{column_name}: '{value}'")
                    df[column_name][i] = 1
                    # df.loc[:, (column_name,i)] = 1 # ERRORED, turned some none date values into 1 :P
            except:
                pass

    df.to_csv('Summarized_Psoriasis_Refactored.csv')
