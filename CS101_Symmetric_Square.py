# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.
def symmetric(list):
    # Your code here
    def get_list(i,p) :
        new = []
        for e in p :
            new.append(e[i])
        return new
    for e in list :
        check = get_list(list.index(e),list)
        if check != e :
            return False
            break
    return True

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False
