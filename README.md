# Matrix-Multiplier
An n x n matrix multiplier where users input two matrices as formatted strings and receive a printed output of the resultant matrix.

# Overview

The logic behind this program is simple. You input two equivalent n x n dimension matrices as formatted strings along with the corresponding dimensions of said matrices as a single integer. These matrix strings are then converted to two-dimensional lists that become matrix multiplied. Finally, the resultant matrix of these two multiplied matrices is printed.

# Usage

To utilize this program properly, the matrices must be inputted in a specific format. Each element within the row vector must be separated by a semicolon, ";". 
Decimal numbers will be rounded to the nearest whole number. If you want to transition to the next row vector, you must accompany the last element of the current row with the pipe symbol,"|". For example, a 3 x 3 matrix such as this:

[1,2,3]  
[4,5,6]  
[7,8,9]  
  
would be inputted like this:

"1;2;3|4;5;6|7;8;9"

```bash
Enter your first matrix: 1;2;3|4;5;6|7;8;9 
Enter your second matrix: 1;2;3|4;5;6|7;8;9
```
The integer you input for dimensions will need to correspond to the dimensions of the matrices you previously inputted. In the case, the dimensions input would be 3 representing the 3 x 3 matrices above.

```bash
Specify the dimension of these respective n x n matrix as a single number: 3
```

# Rules

While the logic behind the program is simple, there are a few rules that you must abide by for this to work.

1. The matrix strings must not empty.

2. The matrix strings must not be erroneous/nonsensical and must be formatted as specified above.

3. The matrix strings must have at least one pipe to signal the transition into a different row vector.
For example, this input is unacceptable for a matrix string: 1;2;3;4;5

4. The matrix strings must not have multiple pipes in a row. For example, this input is unacceptable for a matrix string: 1;2;3|||4;5;6

5. The matrix strings must have each of their rows filled with elements. For example, this input is unacceptable for a matrix string: 1;2;3||4;5;6

6. The matrix strings must not have an unequal number of elements per row vectors. For example, this input is unacceptable for a matrix string: 1|2;3|4;5;6

7. The matrix strings must be matching dimensions.

8. The dimensions input must be a positive integer. It cannot be a decimal number, negative number, or a string consisting of alphabetical/symbolic character(s).

# Software Used

* Python version - 3.6.5

