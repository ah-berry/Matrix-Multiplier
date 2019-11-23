import re



'Creating Matrices Logic'
# Converting the matrix_string into a two-dimensional list
#If an element in the row vectors has any alphabetical letters or symbolic characters, that element will
# be replaced with a 0 instead
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


'''Multiplication & Resultant Matrix Compilation Logic'''
def invert(second_matrix: list) -> list:
    return list(zip(*second_matrix))

#Multiplying each element of the first matrix with its corresponding element from the second matrix
def multiply(first_row_vector, second_row_vector) -> list:
    paired_elements_list = list(zip(first_row_vector,second_row_vector))
    multiplied_results = [element_a*element_b for element_a, element_b in paired_elements_list]
    return sum(multiplied_results)

# Compiling the multiplication of both matrices into one unorganized two-dimensional list then organizing it in the proper form with segmented_lists 
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

# Assorting elements of the first matrix into tuples to assist with the display_resultant_matrix
def convert_to_tuple_elements(first_matrix) -> list:
    return [tuple(elements) for elements in first_matrix]

def dimensions_of_the_matrices(matrix: list) -> int:
    return len(matrix)

def display_resultant_matrix(initial_matrix: list, following_matrix: list):
    dimension = dimensions_of_the_matrices(initial_matrix)
    tupled_first_matrix = convert_to_tuple_elements(initial_matrix)
    inverted_second_matrix = invert(following_matrix)
    resultant_matrix = compile_resultant_matrix(tupled_first_matrix, inverted_second_matrix, dimension)
    for rows in resultant_matrix:
        print(rows)


#If nothing is inputted as a character, function returns True
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

# If there are no elements in certain row vectors, function will return True
def check_no_row_vector_inputs(matrix_string: str) -> bool:
    true_check_list = []
    split_lines = matrix_string.split('|')
    truth_check_list= [True for row_vectors in split_lines if row_vectors == '']
    
    if len(truth_check_list) == 0:
        return False
    
    else:
        return True
    
# If there are multiple line separators consecutively in a given matrix string, function will return True
def check_multiple_line_separators_consecutively(matrix_string: str) -> bool:
    split_lines = matrix_string.split('|')
    split_elements = split_lines[0].split(';')
    consecutive_line_count = matrix_string.count('|')
    if consecutive_line_count != len(split_elements) - 1:
        return True
    else:
        return False


#If there are uneven numbered row vectors relative to others in the same matrix, function will return True 
def check_uneven_row_vectors(matrix_string: str) -> bool:
    split_lines = matrix_string.split('|')
    length_of_row_vectors_list = [len(i.split(';')) for i in split_lines]
    boolean = all(lens == length_of_row_vectors_list[0] for lens in length_of_row_vectors_list)
    if boolean == True:
        return False
    else:
        return True


# If the dimensions of the matrices do not match, function returns True
def check_no_matching_dimensions(first_matrix: str, second_matrix: str) -> bool:
    if len(first_matrix.split('|')) != len(second_matrix.split('|')):
        return True
    else:
        return False

# If the dimensions input does not equal the dimensions of the matrices' strings previously, function returns True
def check_incorrect_dimensions_input(first_matrix: str, second_matrix: str, dimensions: int) -> bool:
    dimensions_of_first_matrix = len(first_matrix.split('|'))
    dimensions_of_second_matrix = len(second_matrix.split('|'))
    if dimensions_of_first_matrix != dimensions or dimensions_of_second_matrix != dimensions:
        return True
    else:
        return False

# Going through all the checks for each matrix input and the dimension input
def all_checks (first_matrix: str, second_matrix: str, dimensions: int) -> bool:
    if check_empty(first_matrix) == True or check_empty(second_matrix) == True:
        print("Error: At least one of your matrices is empty.")
        return False

    if check_erroneous_input(first_matrix) == True or check_erroneous_input(second_matrix) == True:
        print("Error: At least one of your matrices is nonsensical.") 
        return False

    if check_no_line_separator(first_matrix) == True or check_no_line_separator(second_matrix) == True:
        print("Error: At least one of your matrices doesn't have a line separator.")
        return False

    if check_no_row_vector_inputs(first_matrix) == True or check_no_row_vector_inputs(second_matrix) == True:
        print("Error: At least one of your matrices does not have elements in one of its row vectors.")
        return False

    if check_multiple_line_separators_consecutively(first_matrix) == True or check_multiple_line_separators_consecutively(second_matrix) == True:
        print("Error: At least one of your matrices has multiple line separators consecutively.")
        return False
    
    if check_uneven_row_vectors(first_matrix) == True or check_uneven_row_vectors(second_matrix) == True:
        print("Error: At least one of your matrices has an uneven amount of elements in its row vector to abide by n x n dimensions.")
        return False


    if check_no_matching_dimensions(first_matrix,second_matrix) == True:
        print("Error: Your matrices do not have matching n x n dimensions.")
        return False

    if check_incorrect_dimensions_input(first_matrix, second_matrix, dimensions) == True:
        print("Error: Your dimensions input does not correspond to the dimensions of the matrices' strings previously inputted.")
        return False
    
    else:
        return True



def final_loop():

    print("Welcome to the Matrix Multiplier!")
    print()
    print("Please refer to the README.md file of this github project for information in regards to usage and rules to abide by for this project.")
    print()

    flag = False
    while flag != True:
        try:
            print()
            first_matrix = str(input("Enter your first matrix: "))
            print()
            second_matrix = str(input("Enter your second matrix: "))
            print()
            dimensions = int(input("Specify the dimension of these respective n x n matrices as a single number: "))
            print()
            flag = all_checks(first_matrix, second_matrix, dimensions)
        except ValueError:
            print("Make sure the dimensions input strictly adheres to a single positive integer and not a decimal number, negative number, or consisting of alphabetical/symbolic character(s)") 
            
        
    formatted_first_matrix = create_matrices(first_matrix, dimensions)
    formatted_second_matrix = create_matrices(second_matrix, dimensions)
    
    print("Final Result")
    print()
    display_resultant_matrix(formatted_first_matrix, formatted_second_matrix)
    print()

final_loop()


    
