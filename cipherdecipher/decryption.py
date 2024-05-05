import numpy as np
import math
import itertools
import string
import random
import regex as re
# import Encryption as e
class Decryption:
   
    def __init__(self):
        pass
    
    def kk_cipher_decrypt(self,ciphertext, kk):
        """Decrypt the ciphertext using the kk_cipher"""
        plaintext = ''
        i = 0
        while i < len(ciphertext):
            if ciphertext[i] != ' ':
                row = int(ciphertext[i])
                col = int(ciphertext[i + 1])
                for char, (r, c) in kk.items():
#                     print(char)
#                     print(r,c)
                    if r == row and c == col:
                        plaintext += char
                        break
                i += 2
            else:
                plaintext += ' '
                i += 1
        return plaintext.strip()
    
    def substitutionDecrypt(self, ciphertext):
        """Decrypt the ciphertext using the substitution_cipher."""
        decrypted_text = ''
        for char in ciphertext:
            if char in self.decrypt_dict:
                decrypted_text += self.decrypt_dict[char.lower()]
            else:
                decrypted_text += char
        return decrypted_text
    
    #
    def prep_ciphertext(self,ciphertext):
        """Remove whitespace."""
        message = "".join(ciphertext.split())
#         print("\nciphertext = {}".format(ciphertext))
        return message


    def split_rails(self,message):
        """Split message in two, always rounding UP for 1st row."""
        row_1_len = math.ceil(len(message)/2)
        row1 = (message[:row_1_len])
        row2 = (message[row_1_len:])
        return row1, row2


    def railFenceDecrypt(self,row1, row2):
        """Build list with every other letter in 2 strings & print."""
        plaintext = []
        for r1, r2 in itertools.zip_longest(row1, row2, fillvalue=''): 
            plaintext.append(r1)
            plaintext.append(r2)
        return ''.join(plaintext)

    
    def routeCipherDecrypt(self,r_f_d,p):
        """Decrypt the Rail Fence Cipher."""
        # Reverse even-indexed rows
        reversed_even_rows_matrix = r_f_d.copy()
#         print('asdfg',reversed_even_rows_matrix)
        reversed_even_rows_matrix[1::2] = reversed_even_rows_matrix[1::2, ::-1]
        plaintext = ''
        for i in range(1, p+1):
            for row in reversed_even_rows_matrix:
                plaintext += row[-i] + ' '
        return plaintext
