# Напишите функцию для транспонирования матрицы

from .error_class import TransparentError

def transparent_matrix(*a_list) -> list[tuple]:
    matrix = list(a_list)
    col = max([len(matrix[i]) for i in range(len(matrix))])
    for a in list(a_list):
        if len(a) != col:
            raise TransparentError(col, len(matrix))
    return list(zip(matrix))