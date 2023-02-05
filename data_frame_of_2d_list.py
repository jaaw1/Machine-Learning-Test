from create_random_2darray import create_2d_array
from similarity_of_columns import similarity_of_columns
from pandas import DataFrame


def create_DF_from_2d_list(two_d_list):

    return DataFrame(two_d_list, columns = [i for i in range(1, len(two_d_list[0]) + 1)], index=[i for i in range(1, len(two_d_list[0]) + 1)] )


if __name__ == '__main__':
    table_a = create_2d_array()
    table_b = create_2d_array()

    per_table = similarity_of_columns(table_a, table_b)

    df_test = create_DF_from_2d_list(per_table)

    print("\nSimilarity of columns (%)")
    print(df_test)

