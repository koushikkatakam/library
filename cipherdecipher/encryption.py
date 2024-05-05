import numpy as np
import math
import itertools
import string
import random
import regex as re

class Encryption:
    
    def __init__(self):
        plaintext_alphabet = list(string.ascii_lowercase)
        ciphertext_alphabet = list(string.ascii_lowercase)
        random.shuffle(ciphertext_alphabet)
        self.encrypt_dict = dict(zip(plaintext_alphabet, ciphertext_alphabet))
        self.decrypt_dict = dict(zip(ciphertext_alphabet, plaintext_alphabet))
    
    
    def capitalize_first_letter(self,sentence):
        "Capatilizing the entered string"
        words = sentence.split()
        modified_words = [word[0].upper() + word[1:].lower() for word in words]
        return ' '.join(modified_words)

    
    def route_cipher_encrypt(self, plaintext, key,rows,cols):
        """Encrypt using the Route cipher."""
        cipherlist = list(plaintext.split())
        key_int = [int(i) for i in key.split()]
        translation_matrix = self.build_matrix(key_int, cipherlist,rows,cols)
        ciphertext = self.encrypt1(translation_matrix)
        return ciphertext
    
    def build_matrix(self,key_int,cipherlist,rows,cols):
        """building the matrix"""
        matrix = np.array(cipherlist).reshape(rows,cols)
        transposed_matrix = matrix.T
        adjusted_matrix = np.empty_like(transposed_matrix)
        for i, row in enumerate(transposed_matrix):
            if key_int[i] < 0:
                adjusted_matrix[i] = row[::-1]
            else:
                adjusted_matrix[i] = row
        return adjusted_matrix

    def encrypt1(self, translation_matrix):
        """route cipher encryption"""
        plaintext = ''
        for row in translation_matrix:
            for word in row:
                plaintext += word + ' '
        return plaintext

    def rail_fence_cipher_encrypt(self, plaintext,p):
        """Encrypt using the Rail Fence cipher."""
        message = "".join(plaintext.split())
        rails = self.build_rails(message)
        ciphertext = self.encrypt(rails,p)
        return ciphertext
    
    def build_rails(self, message):
        """building rails for rail fence cipher"""
        evens = message[::2]
        odds = message[1::2]
        rails = evens + odds
        return rails

    def encrypt(self, rails,p):
        ciphertext = ' '.join([rails[i:i + p] for i in range(0, len(rails), p)])
        return ciphertext

    def substitution_cipher_encrypt(self, plaintext):
        """substitution cipher encryption"""
        encrypted_text = ''
        for char in plaintext:
            if char in self.encrypt_dict:
                encrypted_text += self.encrypt_dict[char]
            else:
                encrypted_text += char
        return encrypted_text


    def kk_cipher_encrypt(self, plaintext, kk):
        """Encrypt using the kk cipher."""
        ciphertext = ''
        for char in plaintext:
            if char in kk:
                ciphertext += str(kk[char][0]) + str(kk[char][1])
            else:
                ciphertext += char
        return ciphertext

    def kk_cipher_decrypt(self,ciphertext, kk):
        """Decrypt the ciphertext using the kk_cipher."""
        plaintext = ''
        i = 0
        while i < len(ciphertext):
            if ciphertext[i] != ' ':
                row = int(ciphertext[i])
                col = int(ciphertext[i + 1])
                for char, (r, c) in kk.items():
                    if r == row and c == col:
                        plaintext += char
                        break
                i += 2
            else:
                plaintext += ' '
                i += 1
        return plaintext.strip()
    
    def substitutionDecrypt(self, ciphertext):
        """substitution cipher decryption"""
        decrypted_text = ''
        for char in ciphertext:
            if char in self.decrypt_dict:
                decrypted_text += self.decrypt_dict[char.lower()]
            else:
                decrypted_text += char
        return decrypted_text