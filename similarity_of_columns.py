from create_random_2darray import *
from numpy import average, around


def similarity_of_columns(table_1, table_2):
    percentages_table = [[0.0 for x in range(len(table_1))] for y in range(len(table_2))]
    for i in range(len(table_1)):
        for j in range(len(table_2)):
            percentage = around(100 * (abs(average(table_1[:, i] - table_2[:, j]))), 2)
            percentages_table[i][j] = percentage

    return percentages_table


if __name__ == '__main__':
    table_a = create_2d_array()
    table_b = create_2d_array()

    per_table = similarity_of_columns(table_a, table_b)

    print("Similarity in percentages: ")
    for x in range(len(per_table)):
        print(per_table[x])
