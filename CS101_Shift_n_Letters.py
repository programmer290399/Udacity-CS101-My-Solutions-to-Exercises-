# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
  code = ord(letter)
  final = code + n
  if final>=97 and final<=122 :
    return chr(final)
  elif final > 122 :
      return chr( ( (final % 122) + 96 ) )
  elif final < 97 :
      return chr((122 - (96 - final)))






print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('s', -10)
#>>> i
