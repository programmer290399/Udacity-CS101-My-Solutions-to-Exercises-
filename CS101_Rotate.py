# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def shift_n_letters(letter, n):
  code = ord(letter)
  final = code + n
  if final>=97 and final<=122 :
    return chr(final)
  elif final > 122 :
      return chr( ( (final % 122) + 96 ) )
  elif final < 97 :
      return chr((122 - (96 - final)))

def rotate(str , n):
    # Your code here
    final = ''
    for i in range(0,len(str)):
        if str[i] != " " :
            final = final + shift_n_letters(str[i],n)
        else :
            final = final + " "

    return final


print rotate ('sarah', 13)
#>>> 'fnenu'
print rotate('fnenu',13)
#>>> 'sarah'
print rotate('dave',5)
#>>>'ifaj'
print rotate('ifaj',-5)
#>>>'dave'
print rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17)
#>>> ???
