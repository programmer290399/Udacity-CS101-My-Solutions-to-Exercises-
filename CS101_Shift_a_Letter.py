# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a'
# following 'z'.

def shift(letter):
    ASCII = ord(letter)
    if ASCII == 122 :
        return chr(97)
    else :
        return chr(ASCII + 1)





print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a
