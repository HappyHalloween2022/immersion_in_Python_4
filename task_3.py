# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from .error_class import TransparentError
def transparent_matrix(*a_list) -> list[tuple]:
    matrix = list(a_list)
    col = max([len(matrix[i]) for i in range(len(matrix))])
    for a in list(a_list):
        if len(a) != col:
            raise TransparentError(col, len(matrix))
    return list(zip(matrix))


if __name__ == '__main__':
    print(transparent_matrix([1, 3, 5], [2, 4, 6, 4]))