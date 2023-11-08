from pathvalidate import is_valid_filename
import re

filename = "Barclays PLC : American Depositary Receipts"
words=[]

for word in filename.split(" "):
    test_str = ''.join(letter for letter in word if letter.isalnum())
    words.append(test_str)
print(words)
filename=' '.join(words)
print(filename)
is_valid = is_valid_filename(filename)
print(is_valid)