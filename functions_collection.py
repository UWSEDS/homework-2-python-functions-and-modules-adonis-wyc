import pandas as pd
import types

# Write a python reads creates a dataframe from a URL that points to a CSV file such as the pronto data or
# CSVs in data.gov.


def read_function(url):
    df = pd.read_csv(url)
    return df


url = 'https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD'
df = read_function(url)
column_names = ['trip_id',
                'starttime',
                'stoptime',
                'bikeid',
                'tripduration',
                'from_station_name',
                'to_station_name',
                'from_station_id',
                'to_station_id',
                'usertype',
                'gender',
                'birthyear']


def test_create_dataframe(df, column_names):

    # The DataFrame contains only the columns that you specified as the second argument.
    df_column_names = df.columns.tolist()
    set_df_column = set(df_column_names)
    set_column = set(column_names)
    if set_df_column != set_column:
        return False
    # 2 same type in each column
    for i in range(len(list(df.dtypes))):
        # print(i)
        for j in range(list(df.count())[i]):
            if (type(df.iloc[j,i]) != type(df.iloc[0,i])):
                # print(str(type(df.iloc[j,i]))+'vs'+str(type(df.iloc[0,i])))
                return False
            # else: continue
            
    # There are at least 10 rows in the DataFrame.
    if df.shape[0] < 10:
        return False
    return True


print(test_create_dataframe(df, column_names))
