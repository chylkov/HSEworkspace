def read_big_matrix(matrix_file_path="C:\\Users\\TEMP.SPB.003\\Downloads\\sparse_matrix_huge.csv",
                    write_file_path="C:\\Users\\TEMP.SPB.003\\Downloads\\myformat.txt"):
    matrix_file = open(matrix_file_path, 'r')
    write_file = open(write_file_path, 'w')

    m_dict = {}
    row = 0

    for line in matrix_file:
        ints = [float(strnumber) for strnumber in line.strip().split(',')]
        for column in range(len(ints)):
            if ints[column] != 0:
                m_dict[(row, column)] = ints[column]
                write_file.write('{0} {1} {2}\n'.format(row, column, ints[column]))
        row += 1

    write_file.close()
    return m_dict

def read_my_big_matrix(path="C:\\Users\\TEMP.SPB.003\\Downloads\\myformat.txt"):
    file = open(path, 'r')
    m_dict = {}

    for line in file:
        values = [sn for sn in line.strip().split(' ')]
        m_dict[int(values[0]), int(values[1])] = float(values[2])

    return m_dict

def access(row, column, mdict):
    if (row, column) in mdict.keys():
        return mdict[(row, column)]
    else:
        return None

# TODO: get representation by row FROM FILE!
def get_representation_by_row_from_dict(matrix):
    repr_dict = {}
    for key in matrix.keys():
        if key[0] not in repr_dict:
            repr_dict[key[0]] = []
        repr_dict[key[0]].append((key[1], matrix[key]))
    return repr_dict
    #print(repr_dict)

def get_representation_by_column_from_dict(matrix):
    repr_dict = {}
    for key in matrix.keys():
        if key[1] not in repr_dict:
            repr_dict[key[1]] = []
        repr_dict[key[1]].append((key[0], matrix[key]))
    return repr_dict
    #print(repr_dict)

def multiply(_m1, _m2):
    m1 = get_representation_by_row_from_dict(_m1)
    m2 = get_representation_by_column_from_dict(_m2)
    print(m1)
    print()
    print(m2)
    print()
    result = {}
    for i in range(len(m1)):
        for j in range(len(m2)):
            res = 0
            for sub_i in m1[i]:
                for sub_j in m2[j]:
                    if (sub_i[0] == sub_j[0]):
                        res += sub_i[1] * sub_j[1]
            if res > 0:
                result[(i,j)] = res
    return result


def add1(m1, m2): # for representation as dict[coord] = value
    result = m1.copy()
    for key in m2.keys():
        if key in result:
            result[key]+= m2[key]
        else:
            result[key] = m2[key]
    return result

#for special sparse representation
def add2(_m1, _m2):
    result = _m1.copy()
    m1 = get_representation_by_row_from_dict(_m1)
    m2 = get_representation_by_row_from_dict(_m2)
    #TODO


matrix1 = read_my_big_matrix()
matrix2 = read_my_big_matrix()
print(matrix1)
print('*'*9)
print(matrix2)
mul = multiply(matrix1, matrix2)
print(mul)

#TODO: class, checking, another operations