import re


'Overall Logic Pathway'
# 1)  Find out each matrix is:
#     - empty
#     - has line separator(s)
#     - no multiple line separators in a row
#     - no erroneous input
#     - has elements filled into each row vector
#     - non-matching lengths of each row vector
# 2) Construct the matrix using the create matrices function
# 3) Now verify there isn't any alphabetic and alphanumeric elements in each row vector. So:
#     - [[1,2,3]     [[1,2,c]]       [[1,2,c3]]
#        [4,5,6]  != [[4,b,5]]  and   [[4,b2,6]] 
#        [7,8,9]]    [[a,7,8]]       [[a1,8,9]]
# 4) Then check if each matrix is of matching dimensions
# 5) Once the matrices are of acceptable form, throw them each into display_resultant_matrix
# 6) Throw display_resultant_matrix into final game loop function that has an error detection system 


'Test Cases'

def check_empty(matrix_string: str) -> bool:
    if len(matrix_string) == 0:
        return True
    return False


# If there is no line separator, it will return True
def check_no_line_separator(matrix_string: str) -> bool:
    if '|' not in matrix_string:
        return True
    return False

# If there is an erroneous input, function will return True
def check_erroneous_input(matrix_string: str) -> bool:
    prog = re.compile(r'^\w+$')
    result = prog.match(matrix_string)
    if result != None:
        return True
    return False

# If there are no elements in between line separators, function will return True
def check_no_row_vector_inputs(matrix_string: str) -> bool:
    true_check_list = []
    split_lines = matrix_string.split('|')
    for row_vectors in split_lines:
        if row_vectors == '':
            true_check_list.append('True')
        elif row_vectors != '':
            true_check_list.append('False')
    if 'False' in true_check_list:
        return False
    else:
        return True

#If there are no multiple line separators consecurtively, function returns True
def check_multiple_line_separators_consecutively(matrix_string: str) -> bool:
    split_lines = matrix_string.split('|')
    split_elements = split_lines[0].split(';')
    if len(split_elements) != len(split_lines):
        return True
    else:
        return False

'Both functions I need to finish'

# If the row vectors are uneven, function returns True
def check_no_uneven_row_vectors(matrix_string: str) -> bool:
    split_lines = matrix_string.split('|')
    length_of_row_vectors_list = [len(i.split(';')) for i in split_lines]
    boolean = all(lens == length_of_row_vectors_list[0] for lens in length_of_row_vectors_list)
    if boolean == 'True':
        return False
    else:
        return True


# If the dimensions of the matrices match, function returns True
def check_matching_dimensions(first_matrix: str, second_matrix: str) -> bool:
    if len(first_matrix.split('|')) == len(second_matrix.split('|')):
        return True
    else:
        return False

# print(check_no_line_separator('hfjdhshdhfsdj'))
# print(check_erroneous_input('jfhsjdhfsj')) 
# print(check_no_row_vector_inputs('|'))
# print(check_multiple_line_separators_consecutively('1;2;3||4;5;6|7;8;9|'))
# print(check_no_uneven_row_vectors('1;2;3|4;5|6;7;8'))



'Creating Matrices Logic'

# If an element in the row vectors has any alphabetical letters or symbolic characters, that element will
# be replaced with 0 instead
def create_matrices(matrix_string: str, dimension: int) -> list:

    unorganized_matrix = []
    split_lines = matrix_string.split('|')

    for i in split_lines:
        for j in i.split(';'):
            element = j.replace(',','')

            if '.' in element:
                rounded_element = round(float(element))
                unorganized_matrix.append(rounded_element)

            elif element.isdigit() != True:
                unorganized_matrix.append(0)
                
            else:
                unorganized_matrix.append(int(element))
    

    matrix = [unorganized_matrix[x:x+dimension]
                for x in range(0, len(unorganized_matrix), dimension)]

    return matrix




# line = '12;32;45|56;100;1|19;13;4'
# dimension = dimension_of_matrix(line)
# print(create_matrices(line, dimension))
# print(create_matrix('12;32;45|56;100;1|19;13;4'))









    
# check_no_line_separator('hfjdhshdhfsdj')
# check_erroneous_input('|')
# check_no_row_vector_inputs('|')
# check_multiple_line_separators_consecutively('1;2;3||4;5;6|7;8;9|')
# ##check_alphanumeric_inputs_mixed_in('Ahmed121')
# check_non_filled_cell('1;2;3|3;4;5|6;7;8')
# check_matching_dimensions('2;3|4;5','7;8|9;0')
















'''Multiplication & Resultant Matrix Compilation Logic'''
def invert(second_matrix: list) -> list:
    return list(zip(*second_matrix))

def multiply(first_row_vector, second_row_vector) -> list:
    paired_elements_list = list(zip(first_row_vector,second_row_vector))
    multiplied_results = [element_a*element_b for element_a, element_b in paired_elements_list]
    return sum(multiplied_results)

def compile_resultant_matrix(first_matrix, second_matrix, dimension) -> list:

    unorganized_resultant_matrix = []
    first_vector_shifts = 0
    second_vector_shifts = 0

    while second_vector_shifts != dimension:
        if first_vector_shifts == dimension:
            first_vector_shifts = 0
            second_vector_shifts +=1
        else:
            summed_result = multiply(first_matrix[first_vector_shifts],second_matrix[second_vector_shifts])
            unorganized_resultant_matrix.append(summed_result)
            first_vector_shifts += 1

    segmented_lists = [unorganized_resultant_matrix[x:x+dimension]
                    for x in range(0, len(unorganized_resultant_matrix), dimension)]
    resultant_matrix = list(zip(*segmented_lists))
    return resultant_matrix

def convert_to_tuple_elements(first_matrix) -> list:
    return [tuple(elements) for elements in first_matrix]

def dimensions_of_the_matrices(matrix: list) -> int:
    return len(matrix)

# first_matrix = [[10,20,70,500],[30,40,70,600], [100,200,300,1200], [10,20,30,7000]]
# second_matrix=[[50,60,70,2300],[70,80,70,1700], [400,500,600,3200], [10,20,30,5600]]
# first_row_vector = [1,2]
# second_row_vector = [9,10]
# resultant_matrix = [31,34,71,78]

# dimension = dimensions_of_the_matrices(second_matrix)
# tupled_first_matrix = convert_to_tuple_elements(first_matrix)
# inverted_second_matrix = invert(second_matrix)
# resultant_matrix = compile_resultant_matrix(tupled_first_matrix, inverted_second_matrix, dimension)

def display_resultant_matrix(initial_matrix: list, following_matrix: list):
    dimension = dimensions_of_the_matrices(initial_matrix)
    tupled_first_matrix = convert_to_tuple_elements(initial_matrix)
    inverted_second_matrix = invert(following_matrix)
    resultant_matrix = compile_resultant_matrix(tupled_first_matrix, inverted_second_matrix, dimension)
    for rows in resultant_matrix:
        print(rows)

# display_resultant_matrix(first_matrix, second_matrix)

# Needs to be in the matrix user input needs to be in the format of: 12;32;45|56;100;1|19;13;4
# Decimal inputs will be rounded to the nearest whole number.

def final_loop():
    first_matrix = str(input("Enter your first matrix in the format specified above: "))
    second_matrix = str(input("Enter your second matrix in the format specified above: "))
    dimension = int(input("Specify the dimension of these respective n x n matrix as a single number: "))
    print(check_empty(second_matrix))
    print('Erroneous Inputs?')
    print(check_erroneous_input(first_matrix))
    print(check_erroneous_input(second_matrix))
    print("No line separators")
    print(check_no_line_separator(first_matrix))
    print(check_no_line_separator(second_matrix))
    print("Multiple line separators")
    print(check_multiple_line_separators_consecutively(first_matrix))
    print(check_multiple_line_separators_consecutively(second_matrix))
    print ('No row vector inputs')
    print(check_no_row_vector_inputs(first_matrix))
    print(check_no_row_vector_inputs(second_matrix))
    print('No uneven row vectors')
    print(check_no_uneven_row_vectors(first_matrix))
    print(check_no_uneven_row_vectors(second_matrix))
    print('Checking matching dimensions')
    print(check_matching_dimensions(first_matrix,second_matrix))
    actual_1matrix = create_matrices(first_matrix, dimension)
    actual_2matrix = create_matrices(second_matrix, dimension)
    print("Alpha matrix")
    print(actual_1matrix)

    print("Final Result")
    display_resultant_matrix(actual_1matrix, actual_2matrix)


##def final_loop():
##    first_matrix = str(input("Enter your first matrix in the format specified above: "))
##    second_matrix = str(input("Enter your second matrix in the format specified above: "))
##    dimension = int(input("Specify the dimension of these respective n x n matrix as a single number: "))
##    print('Empty?')
##    print(check_empty(first_matrix))
##    print(check_empty(second_matrix))
##    print('Erroneous Inputs?')
##    print(check_erroneous_input(first_matrix))
##    print(check_erroneous_input(second_matrix))
##    print("No line separators")
##    print(check_no_line_separator(first_matrix))
##    print(check_no_line_separator(second_matrix))
##    print("Multiple line separators")
##    print(check_multiple_line_separators_consecutively(first_matrix))
##    print(check_multiple_line_separators_consecutively(second_matrix))
##    print ('No row vector inputs')
##    print(check_no_row_vector_inputs(first_matrix))
##    print(check_no_row_vector_inputs(second_matrix))
##    print('No uneven row vectors')
##    print(check_no_uneven_row_vectors(first_matrix))
##    print(check_no_uneven_row_vectors(second_matrix))
##    print('Checking matching dimensions')
##    print(check_matching_dimensions(first_matrix,second_matrix))
##    actual_1matrix = create_matrices(first_matrix, dimension)
##    actual_2matrix = create_matrices(second_matrix, dimension)
##    print("Alpha matrix")
##    print(actual_1matrix)
##
##    print("Final Result")
##    display_resultant_matrix(actual_1matrix, actual_2matrix)
##    
##
##final_loop()


    
