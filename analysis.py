import pandas as pd
import matplotlib.pyplot as plt


def diagnosis_share(df: pd.DataFrame, ind: int, diagnosis: str, hospitals: list):
    return df.loc[df['hospital'] == hospitals[ind]]['diagnosis'].\
        value_counts(normalize=True)[diagnosis]


def median_age(df, hospital: list, ind: int):
    return df.loc[df['hospital'] == hospital[ind]]['age'].median()


def main():
    pd.set_option('display.max_columns', 8)
    tables = ['general', 'prenatal', 'sports']
    nan_columns = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound',
                   'mri', 'xray', 'children', 'months']
    a, b, c = list(map(lambda j: pd.read_csv(f'test/{j}.csv'), tables))
    c.columns = b.columns = a.columns
    df_merged = pd.concat([a, b, c], ignore_index=True)
    df_merged.drop('Unnamed: 0', axis=1, inplace=True)
    df_merged.dropna(inplace=True, how='all')
    df_merged.replace(to_replace={'man': 'm', 'male': 'm', 'woman': 'f', 'female': 'f'},
                      inplace=True)
    df_merged.loc[:, 'gender'].fillna('f', inplace=True)
    df_merged[nan_columns] = df_merged[nan_columns].fillna(0)

    #  stage_4
    # num_patients = [len(df_merged[df_merged['hospital'] == i]) for i in tables]
    # max_patients = tables[(num_patients.index(max(num_patients)))]
    # stomach_share = df_merged.loc[df_merged['hospital'] == tables[0]]['diagnosis'].\
    #     value_counts(normalize=True)['stomach']
    # dislocation_share = df_merged.loc[df_merged['hospital'] == tables[2]]['diagnosis'].\
    #     value_counts(normalize=True)['dislocation']
    # median_gen = median_age(df_merged, tables, 0)
    # median_sports = median_age(df_merged, tables, 2)
    # hosp_test = df_merged[df_merged.blood_test == 't'].\
    #     pivot_table(index='hospital', values='blood_test', aggfunc='count')
    # max_hosp = hosp_test[hosp_test.blood_test == hosp_test.blood_test.max()]

    # print(f"The answer to the 1st question is {max_patients}\n"
    #       f"The answer to the 2nd question is {round(stomach_share, 3)}\n"
    #       f"The answer to the 3rd question is {round(dislocation_share, 3)}\n"
    #       f"The answer to the 4th question is {median_gen - median_sports}\n"
    #       f"The answer to the 5th question is {max_hosp.index[0]}, {max_hosp.iloc[0, 0]} blood tests")

    #  stage 5 (visualisation)

    # print(df_merged.columns, df_merged[df_merged['hospital'] == 'general']['height'], sep='\n')

    # histogram
    bins = [0, 15, 35, 55, 70, 80]
    plt.hist(df_merged['age'], color="orange", edgecolor="grey", bins=bins)
    plt.title("Age distribution")
    plt.ylabel("Number of people")
    plt.xlabel("Age")
    plt.show()

    # pie
    diagnosis_pie = df_merged['diagnosis'].value_counts()
    labels = list(diagnosis_pie.index)
    plt.pie(diagnosis_pie, labels=labels, autopct='%.1f%%', shadow=True)
    plt.show()

    # violin plot
    plt.violinplot(df_merged['height'])
    plt.show()

    print("The answer to the 1st question: 15-35\n"
          "The answer to the 2nd question: pregnancy\n"
          "The answer to the 3rd question: It's because the 'height' value in the 'sports' hospital is in feet, "
          "while in the 'general' and 'prenatal' ones is in meters")

if __name__ == '__main__':
    main()
