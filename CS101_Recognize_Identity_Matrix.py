# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input,
# define a  procedure that returns True if the input is an identity matrix
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements
# on the principal/main diagonal are 1 and all the elements outside
# the principal diagonal are 0.
# (A square matrix is a matrix in which the number of rows
# is equal to the number of columns)

def is_identity_matrix(matrix):
    #Write your code here
    def is_square(p):
        for e in p :
            if len(e) != len(p) :
                return False
                break
        return True
    if is_square(matrix):
        j = 0
        for i in range(0,len(matrix)):
            if matrix[i][i] != 1  :
                return False
                break
        for i in range(0,len(matrix)):
            if matrix[i][j]!=0 and i != j  :
                return False
                break
            j = j + 1

        for e in matrix :
            j = matrix.index(e)
            for i in range(0,len(e)):
               if e[i]!= 0 and i != j :
                   return False
                   break



        return True
    else :
        return False




# Test Cases:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
print is_identity_matrix(matrix1)
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

print is_identity_matrix(matrix2)
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

print is_identity_matrix(matrix3)
#>>>False

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix4)
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

print is_identity_matrix(matrix5)
#>>>False

matrix6 = [[1,0,0,0],
           [0,1,0,1],
           [0,0,1,0],
           [0,0,0,1]]

print is_identity_matrix(matrix6)
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
print is_identity_matrix(matrix7)
#>>>False

           
