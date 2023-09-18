# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]

# len(matrix) = number of rows
# len(matrix[0]) = number of columns
print(matrix)
print("Rows: ",len(matrix),"Columns: ", len(matrix[0]))

# Solution
matrix_t = [[row[i] for row in matrix] for i in range(2)]
print(matrix_t)