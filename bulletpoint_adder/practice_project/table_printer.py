def column_width(tabel):
    columnWidths = [0] * len(tabel)
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if len(tabel[i][j]) > columnWidths[i]:
                columnWidths[i] = len(tabel[i][j])
    return columnWidths

def print_table(table, columnWidths):
    for i in range(len(table[0])):  # i = 4 meansing the output has 4 rows
        #print (i)
        for j in range(len(table)):  # j = 3 to output each column
            print(table[j][i].rjust(columnWidths[j]), end=' ')
        print()

if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    columnWidths = column_width(tableData)
    print_table(tableData, columnWidths)
