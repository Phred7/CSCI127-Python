# --------------------------------------
# CSCI 127, Lab 9
# October 29, 2018
# Walker Ward
# --------------------------------------

# --------------------------------------
# Do not change anything below this line
# --------------------------------------

def print_header(columns):
    line = "+"
    for i in range(columns):
        line += "---+"
    print(line)

# --------------------------------------

def read_matrix(input_file):
    matrix = {}
    line = input_file.readline().split()
    while line[0] != "stop":
        row = int(line[0])
        column = int(line[1])
        value = int(line[2])
        matrix[(row, column)] = value
        line = input_file.readline().split()
    return matrix

# --------------------------------------

def main (file_name):
    input_file = open(file_name, "r")
    
    line = input_file.readline().split()
    rows = int(line[0])
    columns = int(line[1])

    matrix_1 = read_matrix(input_file)
    print_matrix(matrix_1, rows, columns, "Matrix 1")
    
    matrix_2 = read_matrix(input_file)
    print_matrix(matrix_2, rows, columns, "Matrix 2")

    matrix_3 = subtract_matrices(matrix_1, matrix_2, rows, columns)
    print_matrix(matrix_3, rows, columns, "Matrix 1 - Matrix 2")
    print("Matrix 3 =", matrix_3)

# --------------------------------------

main ("sparse-matrix.txt")
