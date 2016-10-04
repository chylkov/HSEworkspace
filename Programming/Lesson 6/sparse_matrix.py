def read_big_matrix(matrix_file_path="C:\\Users\\user.SPB\\Desktop\\sparse_matrix_huge.csv",
                    write_file_path="C:\\Users\\user.SPB\\Desktop\\myformat.txt"):
    matrix_file = open(matrix_file_path, 'r')
    write_file = open(write_file_path, 'w')

    m_dict = {}
    row = 0
    columns = 0

    for line in matrix_file:
        ints = [float(strnumber) for strnumber in line.strip().split(',')]
        for column in range(len(ints)):
            if ints[column] != 0:
                columns = len(ints)
                m_dict[(row, column)] = ints[column]
                write_file.write('{0} {1} {2}\n'.format(row, column, ints[column]))
        row += 1

    write_file.close()

    # дозапись в начало количества строк и столбцов
    with open(write_file_path, 'r+', encoding='utf-8') as fio:
        data = fio.read()
        fio.seek(0)
        fio.write('{0} {1}\n'.format(row-1, columns) + data)

    return m_dict


def read_my_big_matrix(path="C:\\Users\\user.SPB\\Desktop\\myformat.txt"):
    file = open(path, 'r')
    m_dict = {}

    st = file.readline().strip().split(' ')
    rows, columns = int(st[0]), int(st[1])

    for line in file:
        values = [sn for sn in line.strip().split(' ')]
        m_dict[int(values[0]), int(values[1])] = float(values[2])

    # add writing big matrix from this representation

    return rows, columns, m_dict


def access(row, column, mdict):
    if (row, column) in mdict.keys():
        return mdict[(row, column)]
    else:
        return 0

#TODO:
# new representation for  multiplication matrix
# read/write/access
# multiplication


#read_big_matrix()
matrix = read_my_big_matrix()
print(access(9920, 7976, matrix))