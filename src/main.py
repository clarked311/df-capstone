from etl.load.load import load_HoF
from etl.transform.transform import transform_HoF
from etl.extract.extract import extract_HoF_data


# a function to run the overarching etl process
def etl_process():
    try:
        # extracting the raw data into a tuple
        dfs = extract_HoF_data()

        # assigning variables to each dataframe in the tuple
        HoF = dfs[1]
        People = dfs[0]
        Apps = dfs[2]
        Teams = dfs[3]

        # sending the data to be transformed
        trans_data = transform_HoF(HoF, People, Apps, Teams)

        # loading the transformed data in to the output
        load_HoF(trans_data[0], trans_data[1], trans_data[2])
    except Exception as e:
        print(f"An error occurred: {e}")


# calling the function
etl_process()
