class Patterns:
    '''This is a class containing Patterns'''
    def __init__(self,n):
        assert type(n)==int,"ValueError: integer is needed "
        self.n=n
    def square_grid_pat_1(self):
        for i in range(self.n): # Using for loop to iterate from 0 to n-1
            print('* '*self.n) #Printing row of asteriks '*' multiplied by the value n
    def square_grid_num_pat_2(self):
        for i in range(1,self.n+1): # loop for n number of rows
            for j in range(1,self.n+1): # loop for n number of columns
                print(i,end=' ') # printing the i value and all the elements in a row are seperated with space
            print() # An empty print() method for next line
    def square_grid_num_pat_3(self):
        for i in range(1,self.n+1): ## loop for n number of rows within the range
            for j in range(1,self.n+1): # loop for n number of columns within the range
                print(j, end = ' ') # printing the j value and all the elements in a column are separated with space
            print() # An empty print() method for next line
    def square_grid_alpha_pat_4(self):
        for i in range(0,self.n):# loop for n number of rows which will run from 0 to n
            for j in range(self.n): #loop for n number of columns which will run for n number of times
                print(chr(65+i),end=" ")# printing the alphabet using chr() by adding i to 65('A') and all the elements in a row are seperated with spaces
            print()# An empty print() for next line
    def square_grid_alpha_pat_5(self):
        for i in range(self.n): # Outer loop iterating from 0 to n-1
            for j in range(self.n): # Inner loop iterating from 0 to n-1
                print(chr(65+j),end=' ') # Printing the uppercase letter corresponding to the ASCII value (65 corresponds to 'A')
            print() # Moving to the next line after each inner loop completes
    def square_grid_num_pat_6(self):
        for i in range(self.n,0,-1): # loop for n number of rows
            for j in range(self.n,0,-1): #loop for n number of columns
                print(i,end=' ') # printing i value
            print() # An empty print() method for next line
    def square_grid_num_pat_7(self):
        for i in range(self.n,0,-1):  ## loop for n number of rows within the range
            for j in range(self.n,0,-1): # loop for n number of columns within the range
                print(j, end = ' ')  # printing the j value and all the elements in a column are separated with space
            print() # An empty print() method for next line
    def square_grid_alpha_pat_8(self):
        for i in range(65+self.n-1,64,-1): #Outer loop to iterate through each line, starting feom the ASCII value of 'A'+n-1 and going backward
            for j in range(self.n): #Inner loop to print the character in each line
                print(chr(i),end=" ") #Printing the character corresponding to the ASCII value of i
            print()#Moving to the next line after completing the inner loop
    def square_grid_alpha_pat_9(self):
        for i in range(self.n): # Outer loop iterating from 0 to n-1
            for j in range(self.n): # Inner loop iterating from 0 to n-1
                print(chr(64+self.n-j),end=' ') # Printing the uppercase letter corresponding to the ASCII value (64 + n - j)
            print() # Moving to the next line after each inner loop completes
    def increasing_triangular_pat_10(self):
        for i in range(1,self.n+1): # loop for n number of rows
            for j in range(1,i+1): #loop for i number of columns for each row
                print('*',end=' ') # printing * seperated by space
            print() # # An empty print() method for next line
    def increasing_triangular_num_pat_11(self):
        for i in range(1,self.n+1): #loop for number of rows
            for j in range(i): #loop for number of columns
                print(i, end = ' ') # printing the i value and all the elements in a row are separated with space
            print() # An empty print() method for next line
    def increasing_triangular_num_pat_12(self):
        for i in range(1,self.n+1): #Outer loop to iterate through each line, starting from 1  upto n
            for j in range(i): #Inner loop to print numbers in each line
                print(j+1,end=" ")#Printing the value of k+j with a space after it
            print()#Moving to the next line after completing the inner loop
    def increasing_triangular_alpha_pat_13(self):
        for i in range(1,self.n+1): # Outer loop iterating from 0 to n-1
            for j in range(1,i+1): # Inner loop iterating from 0 to i (inclusive)
                print(chr(64+i),end=' ') # Printing the uppercase letter corresponding to the ASCII value (65 + i)
            print() # Moving to the next line after each inner loop completes
    def increasing_triangular_alpha_pat_14(self):
        for i in range(1,self.n+1): # loop for n number of rows
            for j in range(1,i+1): # loop for i number of columns for each row
                print(chr(64+j),end=' ') # printing alphabet pattern
            print() # An empty print() method for next line
    def decreasing_triangular_pat_15(self):
        for i in range(self.n,0,-1): #loop for printing number of rows in a given range
            for j in range(i): #loop for printing number of columns in a given range
                print('*',end = ' ') # printing aestric and are separated with space
            print() # An empty print() method for next line
    def decreasing_triangular_num_pat_16(self):
        for i in range(1,self.n):#Outer loop to iterate through each line, starting from 1 up to n-1
            for j in range(self.n-i):#Inner loop to print numbers in each line, starting from the current value of it and going upto n-1
                print(i,end=" ") #Printing the value of i with a space after it
            print()#Moving to the next line after completing the inner loop
    def decreasing_triangular_num_pat_17(self):
        for i in range(self.n): # Outer loop iterating from 0 to n-1
            for j in range(self.n-i): # Inner loop iterating from 0 to n-i-1
                print(j+1,end=' ') # Printing the current value of j+1
            print()  # Moving to the next line after each inner loop completes
    def decreasing_triangular_alpha_pat_18(self):
        c=0
        for i in range(self.n,0,-1): # loop for n number of rows
            for j in range(i): # loop for i number of columns
                print(chr(65+c),end=' ') # Printing alphabet pattern
            c+=1
            print() # An empty print() method for next line
    def decreasing_triangular_alpha_pat_19(self):
        for i in range(self.n,0,-1): #loop for printing number of rows in a given range
            for j in range(i): #loop for printing number of columns in a given range
                print(chr(65+j), end = ' ') #printing character by assigning ASCII value of A using chr(65) and incrementing its columns
            print() # An empty print() method for next line
    def decreasing_triangular_num_pat_20(self):
        for i in range(self.n,0,-1):#Outer loop to iterate through each line, starting from n and going down to 1
            for j in range(i):#Inner loop to print numbers in each line, starting from the current value of i
                print(i,end=" ") #Printing the value of i with a space after it
            print()#Moving to the next line after completing the inner loop
    def decreasing_triangular_num_pat_21(self):
        c=self.n # Initializing a constant value c with value of n
        for i in range(self.n,0,-1): # Outer loop iterating from n to 1 with a step of -1
            for j in range(i): # Inner loop iterating from 0 to i-1
                print(c-j,end=' ') # Printing the current value of c - j
            print() # Moving to the next line after each inner loop completes
    def decreasing_triangular_alpha_pat_22(self):
        for i in range(self.n,0,-1): # loop for n number of rows
            for j in range(i): # loop for i number of columns
                print(chr(65+i-1),end=' ') # printing alphabet pattern seperated by space
            print() # An empty print() for next line
    def decreasing_triangular_alpha_pat_23(self):
        for i in range(self.n,-1,-1): #loop for number of rows in the given range
            for j in range(i+1): #loop for number of columns in the given range
                print(chr(65+self.n-j), end = ' ') #printing character by assigning ASCII value of E using chr(65+n-j) and decrementing its columns
            print()# An empty print() method for next line
    def right_aligned_triangular_pat_24(self):
        for i in range(0,self.n+1): #Outer loop to iterate through each line, starting from 0 upto n
            for j in range(self.n-i):#Inner loop to print spaces before stars in each line, starting from n-1
                print(" ",end=" ") # Which will print spaces
            for j in range(i): #Inner loop to print stars in each line, starting from 0 upto i
                print("*",end=" ") #which will print stars
            print()#Moving to the next line after completing the inner loop
    def right_aligned_triangular_num_pat_25(self):
        for i in range(self.n+1): # Outer loop iterating from 0 to n (inclusive)
            for j in range(self.n-i): # Inner loop to print spaces before the numbers
                print(" ",end=' ')
            for k in range(i): # Inner loop to print numbers with increasing values
                print(i,end=' ')
            print()  # Moving to the next line after each row completes
    def right_aligned_triangular_num_pat_26(self):
        for i in range(1,self.n+1):  # loop for n number of rows
            for k in range(self.n-i): # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
            for j in range(1,i+1): # loop for i number of columns
                print(j,end=' ') # printing j value
            print() # An empty print() method for next line 
    def right_aligned_triangular_alpha_pat_27(self):
        for i in range(self.n): #loop for number of columns
            for k in range(self.n-i): #loop for printing spaces
                print(" ",end=' ') #printing spaces
            for j in range(i+1): #loop for number of columns
                print(chr(65+i), end = ' ') #printing character by assigning ASCII value of A using chr(65) and incrementing its rows
            print() #move to the next line after printing spaces and characters for each row
    def right_aligned_triangular_alpha_pat_28(self):
        for i in range(0,self.n+1): #Outer loop to iterate through each line, starting from 0 upto n
            for j in range(self.n-i): #Inner loop to print spaces before the charecters in each line, starting from n-i
                print(" ",end=" ")
            for j in range(65,65+i):#Inner loop to print characters in each line, starting from 'A' upto 'A'+i-1
                print(chr(j),end=" ")
            print() #Moving to the next line after completing the inner loops
    def right_aligned_decreasing_triangular_pat_29(self):
        for i in range(self.n): # Outer loop iterating from 0 to n-1
            for j in range(i): # Inner loop to print spaces before the asterisks
                print(" ",end=' ')
            for k in range(self.n-i): # Inner loop to print asterisks
                print('*',end=' ')
            print() # Moving to the next line after each row completes
    def right_aligned_decreasing_triangular_num_pat_30(self):
        for i in range(self.n,0,-1): # loop for n number of rows
            for k in range(self.n-i): # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
            for j in range(i): # loop for i number of columns
                print(i,end=' ') # printing i value -i times seperated by space
            print() # An empty print() for next line
    def right_aligned_decreasing_triangular_num_pat_31(self):
        for i in range(self.n,0,-1): #loop for number of rows in the given range
            for k in range(self.n-i): #loop for printing spaces
                print(" ",end=' ') #printing spaces
            for j in range(i): #loop for number of columns in the given range
                print(j+1, end = ' ') #printing the value of j+1 without a newline character
            print() #move to the next line after printing spaces and characters for each row
    def right_aligned_decreasing_triangular_alpha_pat_32(self):
        for i in range(self.n,0,-1):# Outer loop to iterate through each line, starting from n and going down to 1
            for j in range(self.n-i+1):# Inner loop to print spaces before the characters in each line, starting from n-i+1
                print(" ",end=' ')
            m=65# Initializing m to the ASCII value of 'A'
            for k in range(65,65+i):# Inner loop to print characters in each line, starting from 'A' up to 'A'+i-1
                print(chr(m+i-1),end=' ')
            m+=1# Incrementing m for next character
            print()# Moving to the next line after completing the inner loops
    def right_aligned_decreasing_triangular_alpha_pat_33(self):
        for i in range(self.n,0,-1): # Outer loop iterating from n to 1 with a step of -1
            for j in range(self.n-i): # Inner loop to print spaces before the letters
                print(" ",end=' ') #printing spaces
            for k in range(i):  # Inner loop to print letters with increasing values
                print(chr(65+k),end=' ') # printing alphabetic pattern
            print() # Moving to the next line after each row completes
    def increasing_triangular_pat_34(self):
        for i in range(1,self.n+1): # loop for n number of rows
            for k in range(self.n-i): # looop for n-i spaces in each row
                print(" ",end='') # printing n-i spaces
            for j in range(1,i+1): # loop for i number of columns in each row
                print("*",end=' ') # printing * seperated by space
            print() # an empty print() for next line
    def increasing_triangular_num_pat_35(self):
        for i in range(1,self.n+1): # loop for number of rows in the given range starting from 1 and incrementing it using n+1
            for k in range(self.n-i): #loop for printing spaces
                print(" ",end=' ') #print spaces
            for j in range(i*2-1): #loop for the number of columns in the given range
                print(i, end = ' ') #printing the value of i and seperating it using spaces
            print() #print method to next line
    def increasing_triangular_num_pat_36(self):
        k=1# Initializing k to 1
        for i in range(1,self.n//2+2):# Outer loop to iterate through each line, starting from 1 up to n//2+1
            for j in range(self.n-i):# Inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end=" ")
            for j in range(2*i-1):# Inner loop to print numbers in each line, starting from 1 up to 2*i-1
                print(k,end=" ")
            k+=2
            print()# Moving to the next line after completing the inner loops
    def increasing_triangular_alpha_pat_37(self):
        for i in range(0,self.n): # Outer loop iterating from 0 to n-1
            for j in range(self.n-i):  # Inner loop to print spaces before the letters
                print(" ",end=' ')
            for k in range(i*2+1): # Inner loop to print letters with increasing values
                print(chr(65+i),end=' ')
            print()  # Moving to the next line after each row completes
    def increasing_triangular_alpha_pat_38(self):
        x=0 # initializing x with 0
        for i in range(self.n//2): # loop for n/2 rows
            for k in range(self.n-i): # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
            for j in range(i*2+1): # loop for i*2+1 columns
                print(chr(65+x),end=' ') # printing alphabet pattern seperated by space
            x+=2 # incrementing x value
            print() # an empty print() for next line
    def increasing_triangular_num_pat_39(self):
        for i in range(1,self.n//2+1): #loop for number of rows in the range
            for k in range(self.n-i): #loop for printing spaces
                print(" ",end=' ') #printing spaces
            for j in range(1,i*2): #loop for numberof columns in the range
                print(j, end = ' ') #printing the value of j and seperating with spaces
            print() #Print method to move to other line
    def increasing_triangular_num_pat_40(self):
        for i in range(1,self.n//2+2):# Outer loop to iterate through each line, starting from 1 up to n//2+2
            for j in range(self.n-i-self.n//2):# Inner loop to print spaces before the numbers in each line, starting from n-i-n//2
                print(" ",end=" ")
            for k in range(2*i-1,0,-1):# Inner loop to print numbers in each line, starting from 2*i-1 and going down to 1
                print(k,end=" ")
            print() # Moving to the next line after completing the inner loops
    def increasing_triangular_alpha_pat_41(self):
        for i in range(0,self.n//2+1): # Outer loop iterating from 0 to n//2 (inclusive)
            for j in range(self.n-i-self.n//2): # Inner loop to print spaces before the letters
                print(" ",end=' ')
            for k in range(i*2+1): # Inner loop to print letters with increasing values
                print(chr(65+k),end=' ')
            print() # Moving to the next line after each row completes
    def increasing_triangular_alpha_pat_42(self):
        x=0 # initializing x with 0
        for i in range(self.n//2+1): # loop for n/2 rows
            for k in range(self.n-i): # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
            for j in range(i*2+1): # loop for i*2+1 columns
                print(chr(65+x-j),end=' ') # printing alphabet pattern seperated by space
            x+=2 # incrementing x value
            print() #an empty print() for next line
    def increasing_triangular_num_pat_43(self):
        for i in range(0,self.n+1): #loop for the number of rows
            for k in range(self.n-i): #loop for printing spaces before numbers
                print(" ",end=' ') #printing spaces
            for j in range(i,-1,-1): #loop for printing numbers in decreasing order
                print(j, end = ' ') #Print the current value of j separated using spaces
            for m in range(1,i+1): #loop for printing numbers in increasing order
                print(m, end=' ') # Print the current value of m
            print() #Move to the next line
    def increasing_triangular_alpha_pat_44(self):
        for i in range(1,self.n+1): # Outer loop to iterate through each line, starting from 1 up to n
            for j in range(self.n-i): # Inner loop to print spaces before the characters in each line, starting from n-i
                print(" ",end=" ")
            for k in range(i,0,-1): # First inner loop to print characters in descending order, starting from 'A'+i and going down to 'A'+1
                print(chr(64+k),end=" ")
            for m in range(1,i):# Second inner loop to print characters in ascending order, starting from 'A'+1 and going up to 'A'+i-1
                print(chr(65+m),end=" ")
            print()# Moving to the next line after completing the inner loops
    def increasing_triangular_num_pat_45(self):
        for i in range(1,self.n+1): # Outer loop iterating from 1 to n (inclusive)
            for j in range(self.n-i): # Inner loop to print spaces before the numbers
                print(" ",end=' ')
            for k in range(1,i+1): # Inner loop to print numbers in increasing order
                print(k,end=' ')
            for l in range(i-1,0,-1): # Inner loop to print numbers in decreasing order (excluding the last number in the row)
                print(l,end=' ')
            print()
    def increasing_triangular_alpha_pat_46(self):
        x=0 # initializing x with 0
        for i in range(self.n+1): # loop for n rows
            for k in range(self.n-i): # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
            for j in range(i): # loop for i number of columns
                print(chr(65+j),end=' ') # printing alphabet pattern seperated by space
            for m in range(i-1,0,-1): # loop for i-1 columns
                print(chr(65+m-1),end=' ') # printing alphabet pattern seperated by space
            print() #an empty print() for next line
    def left_aligned_decreasing_triangular_pat_47(self):
        for i in range(self.n//2,-1,-1): #loop for the number of rows in reverse order
            for k in range(self.n-i): #loop for printing spaces before asterisks
                print(" ",end=' ') #printing spaces
            for j in range(i+1): #loop for printing asterisks in increasing order
                print('*',end = ' ') #asterisk
            for m in range(i): #loop for printing asterisks in decreasing order
                print('*',end=' ') #Print asterisk
            print() #Move to the next line
    def left_aligned_decreasing_triangular_num_pat_48(self):
        m=2 # Initializing m to 2
        for i in range(self.n-1,0,-1): # Outer loop to iterate through each line, starting from n-1 and going down to 1
            for j in range(self.n-i): # Inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end=" ")
            for j in range(self.n+i-m): # Second inner loop to print numbers in each line, starting from n+i-m and going down to n
                print(i,end=" ")
            m+=1 # Incrementing m by 1
            print() # Moving to the next line after completing the inner loops
    def left_aligned_decreasing_triangular_num_pat_49(self):
        for i in range(self.n,0,-2): # Outer loop iterating from n to 1 with a step of -2
            for j in range(self.n-i//2-self.n//2+1): # Inner loop to print spaces before the numbers
                print(" ",end=' ')
            for k in range(i): # Inner loop to print numbers with the value of i
                print(i,end=' ')
            print()  # Moving to the next line after each row completes
    def inverted_pyramid_num_pat_50(self):
        for i in range(self.n//2+1,0,-1): # loop for n/2+1 rows
            for k in range(self.n-i): # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
            for j in range(1,i*2): # loop for i*2 columns
                print(j,end=' ') # printing j value seperated by space
            print() #an empty print() for next line
    def inverted_pyramid_alpha_pat_51(self):
        for i in range(self.n-1,-1,-1): #loop for the number of rows in reverse order
            for k in range(self.n-i): #loop for printing spaces before characters
                print(" ",end=' ') #printing spaces
            for j in range(i*2+1): #loop for the number of columns, based on the current row
                print(chr(65+i), end = ' ') #Print character by assigning ASCII value of A plus the row number
            print() # Move to the next line
    def inverted_pyramid_alpha_pat_52(self):
        k = 65+self.n*2-2 # Initializing k to the ASCII value of 'A' + n*2 - 2
        m=1 # Initializing m to 1
        for i in range(self.n, 0, -1): # Loop to iterate through each line, starting from n and going down to 1
            for j in range(self.n-i+1): # First inner loop to print spaces before the characters in each line, starting from n-i+1
                print(" ", end=" ")
            for j in range(self.n+i-m): # Second inner loop to print characters in each line, starting from the current ASCII value of k and going up to n+i-m
                print(chr(k), end=" ")
            m+=1
            k-=2
            print() # Moving to the next line after completing the inner loops
    def inverted_pyramid_alpha_pat_53(self):
        m=0 # Initializing a variable m with value 0
        for i in range(self.n//2+1,0,-1): # Loop iterating from n//2 + 1 to 1 with a step of -1
            print(' '*(m),end=' ') # Printing spaces before the letters based on the value of m
            for j in range(i*2-1):  # Inner loop to print letters in increasing order
                print(chr(65+j),end=' ') # Incrementing the value of m by 2 for the next row
            m+=2
            print()  # Moving to the next line after each row completes
    def alternating_triangular_pat_54(self):
        for i in range(self.n): # loop for n number of rows
            for j in range(i): # loop for i number of columns
                print("*",end=' ') # printing j number of *'s seperated by space
            print() #an empty print() for next line
        for i in range(self.n,0,-1): # loop for n-1 number of rows
            for k in range(i): # loop for i number of columns
                print("*",end=' ') # printing k number of *'s seperated by space
            print() #an empty print() for next line
    def alternating_triangular_num_pat_55(self):
        for i in range(self.n): #loop for numbers of rows
            for j in range(i+1):  #loop for numbers of columns
                print(self.n-j,end=' ') #Print decreasing numbers based on the current column
            print() # Empty print method to move to next line
        for i in range(self.n,-1,-1): #loop for the number of rows in reverse order
            for k in range(i+1): #loop for the number of columns
                print(self.n-k,end=' ') #Print decreasing numbers based on the current column
            print() # Empty print method to move to next line
    def alternating_triangular_num_pat_56(self):
        # First part of the pattern: Increasing order
        for i in range(self.n): # Outer loop to iterate through each line from 0 to n-1
            for j in range(i,-1,-1): # Inner loop to print numbers in decreasing order from n to n-j
                print(self.n-j,end=' ')
            print() # Moving to the next line after completing the inner loop
        # Second part of the pattern: Decreasing order
        for i in range(self.n,-1,-1):  # Outer loop to iterate through each line from n to 0
            for j in range(i,-1,-1): # Inner loop to print numbers in decreasing order from n to n-j
                print(self.n-j,end=' ')
            print() # Moving to the next line after completing the inner loop
    def alternating_triangular_alpha_pat_57(self):
        for i in range(self.n): #loop for numbers of rows
            for j in range(i+1):  #loop for numbers of columns
                print(chr(65+self.n-j),end=' ') #Print alphabetic pattern
            print() # Empty print method to move to next line
        for i in range(self.n,-1,-1): #loop for the number of rows in reverse order
            for k in range(i+1): #loop for the number of columns
                print(chr(65+self.n-k),end=' ') #Print alphabetic pattern
            print() # Empty print method to move to next line
    def alternating_triangular_alpha_pat_58(self):
        for i in range(self.n): # loop for n number of rows
            for j in range(i,-1,-1): # loop for i number of columns
                print(chr(65+self.n-j),end=' ') #Printing alphabet pattern seperated by space
            print() #an empty print() for next line
        for i in range(self.n,-1,-1): # loop for n number of rows
            for j in range(i,-1,-1): # loop for i number of columns
                print(chr(65+self.n-j),end=' ') #Printing alphabet pattern seperated by space
            print() #an empty print() for next line
    def left_pascal_triangle_pat_59(self):
        for i in range(1,self.n+1):# loop for number of rows in the range
            for j in range(self.n,i,-1): # loop for number of columns in the range
                print(" ",end=' ') #Print spaces
            for k in range(1,i+1): #loop for asterisks in the range
                print("*", end=' ') #print asteriss separated with spaces
            print() #an empty print() for next line
        for i in range(self.n-1,0,-1): # loop for number of rows in the range
            for j in range(self.n,i,-1): # loop for number of columns in the range
                print(" ",end = ' ')#Print spaces
            for k in range(1,i+1): #loop for number of asterisks in the range
                print("*",end=' ') #Print asterisks separated with spaces
            print() #an empty print() for next line
    def left_pascal_triangle_num_pat_60(self):
        # First part of the pattern: Increasing order
        for i in range(self.n): #loop for n number of rows
            for j in range(self.n-i): # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end=" ")
            for j in range(i+1): # Second inner loop to print numbers in decreasing order
                print(self.n-j,end=" ")
            print()  # Moving to the next line after completing the inner loops
        # Second part of the pattern: Decreasing order
        for i in range(self.n,-1,-1):
            for j in range(self.n-i): # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end=" ")
            for k in range(i+1):# Second inner loop to print numbers in decreasing order
                print(self.n-k,end=' ')
            print()
    def left_pascal_triangle_num_pat_61(self):
        # First part of the pattern
        for i in range(self.n): #Loop for no.of rowa
            x=0
            for j in range(self.n-i):  # Printing spaces before the numbers
                print(" ",end=' ')
                x+=1
            for k in range(i+1): # Printing numbers in increasing order
                print(x,end=' ')
                x+=1
            print() # Moving to the next line after each row completes
        # Second part of the pattern
        for i in range(self.n,-1,-1): #Loop for no.of rows
            x=0
            for j in range(self.n-i):  # Printing spaces before the numbers
                print(" ",end=' ')
                x+=1
            for k in range(i+1): # Printing numbers in increasing order
                print(x,end=' ')
                x+=1
            print()# Moving to the next line after each row completes
    def left_pascal_triangle_alpha_pat_62(self):
        for i in range(self.n):  # loop for n number of rows
            x=0  # initializing x with 0
            for j in range(self.n-i): # loop for n -i number of spaces in each row
                print(" ",end=' ')# printing n-i spaces
                x+=1 # incrementing x value
            for k in range(i):  # loop for i number of columns
                print(chr(ord('A')+x),end=' ') # printing alphabetical pattern seperated by space
                x+=1 # incrementing x value
            print() #an empty print() for next line
        for i in range(self.n,0,-1):  # loop for n number of rows
            x=0 #initializing x with 0
            for j in range(self.n-i): # loop for n -i number of spaces in each row
                print(" ",end=' ') # printing n-i spaces
                x+=1 # incrementing x value
            for k in range(i):  # loop for i number of columns
                print(chr(ord('A')+x),end=' ') # printing alphabetical pattern seperated by space
                x+=1 # incrementing x value
            print()  #an empty print() for next line
    def left_pascal_triangle_alpha_pat_63(self):
        for i in range(self.n): # loop for number of rows
            for j in range(self.n-i): # loop for number of columns
                print(" ", end=' ') #printing spaces
            for k in range(i+1): #Print characters in decreasing order
                print(chr(65+self.n-k), end=' ') #printing characters
            print() #an empty print() for next line
        for i in range(self.n,- 1,-1): # loop for number of rows
            for j in range(self.n-i): # loop for number of columns
                print(" ", end=' ') #printing spaces
            for k in range(i+1): #Print characters in decreasing order
                print(chr(65+self.n-k), end=' ') #printing characters
            print() #an empty print() for next line
    def increasing_triangular_pat_64(self):
        for i in range(0,self.n+1): #Outer loop for no.of rows which will run from 0 to n+1
            for j in range(self.n-i): # First inner loop to print spaces before the asterisks in each line, starting from 0
                print(" ",end="")
            for j in range(1,i+1):# Second inner loop to print asterisks in increasing order, starting from 1 up to i
                print("*",end=" ")
            print()
    def increasing_triangular_num_pat_65(self):
        for i in range(0,self.n+1): #Outer loop for no.of rows which will run from 0 to n+1
            for j in range(self.n-i): # First inner loop to print spaces before the asterisks in each line, starting from 0
                print(" ",end="")
            for j in range(1,i+1):# Second inner loop to print asterisks in increasing order, starting from 1 up to i
                print(i,end=" ")
            print()
    def increasing_triangular_num_pat_66(self):
        for i in range(1,self.n+1): # loop for n number of rows
            for j in range(self.n-i): # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
            for k in range(1,i+1): # loop for i number of columns
                print(k,end=' ') # printing k value seperated by space
            print()  #an empty print() for next line
    def increasing_triangular_alpha_pat_67(self):
        for i in range(self.n): # Loop for each row
            for j in range(self.n-i-1):# Loop for each column
                print(" ", end='') # Print spaces before characters
            for k in range(i+1):  # Print characters in increasing order
                print(chr(ord('A')+i), end=' ')
            print() # Move to the next line after printing each row
    def increasing_triangular_alpha_pat_68(self):
        for i in range(0,self.n+1): # Loop to print a pattern of characters in a pyramid
            for j in range(self.n-i): # First inner loop to print spaces before the characters in each line, starting from n-i
                print(" ",end='')
            for k in range(1,i+1): # Second inner loop to print characters in increasing order, starting from 'A' up to 'A+k' where k is the current value of i
                print(chr(64+k),end=' ')
            print() # Moving to the next line after completing the inner loops
    def decreasing_triangular_pat_69(self):
        for i in range(self.n,0,-1): # Loop to iterate through rows in reverse order
            for j in range(0,self.n-i): # Loop to add leading spaces for formatting
                print(end=' ')
            for k in range(0,i): # Loop to print asterisks for the current row
                print('*',end=" ")
            print()# Move to the next line after completing the row
    def decreasing_triangular_num_pat_70(self):
        for i in range(self.n,-1,-1): # loop for n number of rows
            for j in range(self.n-i): # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
            for k in range(i): # loop for i number of columns
                print(i,end=' ') # printing i value - k times
            print() #an empty print() for next line
    def decreasing_triangular_num_pat_71(self):
        for i in range(self.n,0,-1): # Loop for each row
            for j in range(self.n-i):# Loop for each column
                print(" ",end='') #print spaces
            for k in range(i,0,-1): #loop for printing numbers in decreasing order
                print(k, end = ' ')
            print() # Move to the next line after printing each row
    def decreasing_triangular_alpha_pat_72(self):
        for i in range(self.n,0,-1): # Loop to print a pattern of characters in a descending order pyramid
            for j in range(self.n-i+1): # First inner loop to print spaces before the characters in each line, starting from n-i+1
                print(" ",end='')
            for k in range(0,i): # Second inner loop to print characters in decreasing order, all being the same character 'A'+i
                print(chr(64+i),end=' ')
            print() # Moving to the next line after completing the inner loops
    def decreasing_triangular_alpha_pat_73(self):
        for i in range(self.n,0,-1): # Loop to iterate through rows in reverse order
            for j in range(self.n-i+1): # Loop to add leading spaces for formatting
                print(" ",end='')
            for k in range(0,i):  # Loop to print uppercase letters for the current row
                print(chr(64+i-k),end=' ')
            print() # Move to the next line after completing the row
    def decreasing_triangular_alpha_pat_74(self):
        for i in range(self.n,0,-1): # loop for n number of rows
            for j in range(self.n-i): # loop for n-i number of spaces row
                print(" ",end='') # printing n-i spaces
            for k in range(i): # loop for i number of columns
                print(chr(65+k),end=' ') # printing alphabets pattern seperated by space
            print() #an empty print() for next line
    def diamond_pat_75(self):
        for i in range(self.n): #loop for number of rows
            print(" " * (self.n-i), end=" ") #printing Aestric
            for j in range(0, i+1):# loop for number of columns
                print("*", end=" ")
            print() # Move to the next line after printing each row
        for i in range(self.n-1,0,-1): #loop for number of rows for the second half
            print(" " * (self.n-i+1), end=" ")
            for j in range(i): #loop for the number of columns for the second half
                print("*", end=" ")  #printing Aestric
            print() # Move to the next line after printing each row
    def diamond_num_pat_76(self):
        # First part of the pattern: Increasing order
        for i in range(0,self.n):
            for j in range(self.n-i): # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(' ',end='')
            for k in range(1,i+1): # Second inner loop to print numbers in increasing order, all being the same value 'i'
                print(i,end=' ')
            print() # Moving to the next line after completing the inner loops
        # Second part of the pattern: Decreasing order
        for i in range(self.n,0,-1):
            for j in range(self.n-i): # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end='')
            for k in range(1,i+1):# Second inner loop to print numbers in decreasing order, all being the same value 'i'
                print(i,end=' ')
            print()
    def diamond_num_pat_77(self):
        # First part of the pattern: Increasing order
        for i in range(0,self.n):
            for j in range(self.n-i): # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(' ',end='')
            for k in range(1,i+1): # Second inner loop to print numbers in increasing order, and printing the k vale
                print(k,end=' ')
            print() # Moving to the next line after completing the inner loops
        # Second part of the pattern: Decreasing order
        m=1
        for i in range(self.n,0,-1):
            for j in range(self.n-i): # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end='')
            for k in range(0,i):# Second inner loop to print numbers in decreasing order, and printing the value of k+m
                print(k+m,end=' ')
            m+=1
            print()
    def diamond_num_pat_78(self):
        for i in range(1,self.n): # loop for n-1 number of rows
            for j in range(self.n-i): # loop for n-i number of spaces in each row
                print(' ',end='')  # printing n-i spaces
            for k in range(1,i+1): # loop for i number of columns
                print(k,end=' ') # printing k value seperated by space
            print()  #an empty print() for next line
        for i in range(self.n,0,-1): # loop for n number of rows
            for j in range(self.n-i): # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
            for k in range(1,i+1): # loop for i number of columns
                print(k,end=' ') # printing k values seperated by spaces
            print()  #an empty print() for next line
    def diamond_alpha_pat_79(self):
        for i in range(self.n): #loop for number of rows
            for j in range(self.n - i - 1): #loop for number of columns
                print(" ", end='')   # Print spaces before characters
            for k in range(i + 1):
                print(chr(ord('A') + i), end=' ') # Print characters in increasing order
            print()  # Move to the next line after printing each row
        for i in range(1, self.n):
            for j in range(i):
                print(" ", end='')# Print spaces before characters
            for k in range(self.n - i):  # Print characters in decreasing order
                print(chr(ord('A') + self.n - i - 1), end=' ')
            print()  # Move to the next line after printing each row
    def diamond_alpha_pat_80(self):
        # First part of the pattern: Increasing order
        for i in range(self.n):
            for j in range(self.n - i - 1): # First inner loop to print spaces before the characters in each line, starting from n-i-1
                print(' ', end='')
            for k in range(i+1): # Second inner loop to print characters in increasing order, starting from 'A' to 'A+k'
                print(chr(65 + k), end=' ')
            print() # Moving to the next line after completing the inner loops
        # Second part of the pattern: Decreasing order
        m=1
        for i in range(1, self.n):
            for j in range(i):  # First inner loop to print spaces before the characters in each line, starting from i
                print(" ", end='')
            for k in range(self.n - i): # Second inner loop to print characters in decreasing order, starting from 'A+k+m'
                print(chr(65 + k+m), end=' ')
            m+=1
            print() # Moving to the next line after completing the inner loops
    def inverted_v_shaped_pat_81(self):
        for i in range(0,self.n+1): # Loop to iterate through rows
            for j in range(self.n-i+1): # Loop to add leading spaces for formatting
                print(' ',end='')
            for k in range(i+1): # Loop to print characters for the current row
                if k==0 or k==i:
                    print("*",end=' ')  # Print '*' if it's the first or last character in the row, otherwise print a space
                else:
                    print(" ",end=' ')
            print() # Move to the next line after completing the row
    def inverted_v_shaped_num_pat_82(self):
        for i in range(1,self.n+1): # loop for n number of rows
            for j in range(self.n-i): # loop for n-i number of spaces in each row
                print(' ',end='') # printing n-i spaces
            for k in range(1,i+1): # loop for i number of columns
                if k==1 or k==i: #Checking whether the value of k is equal to 1 or i.
                    print(i,end=' ') # printing i value if the k value is either 1 or i
                else: # else block will execute if k value is neither 1 nor i
                    print(" ",end=' ') # printing spaces
            print() #an empty print() for next line
    def inverted_v_shaped_num_pat_83(self):
        for i in range(0,self.n): # loop for n number of rows
            for j in range(self.n-i): # loop for n-i number of spaces in each row
                print(' ',end='') # printing n-i spaces
            for k in range(0,i+1): # loop for i number of columns
                if k==0 or k==i: #Checking whether the value of k is equal to 0 or i.
                    print(self.n-i,end=' ') # printing n-i value if the k value is either 1 or i
                else: # else block will execute if k value is neither 0 nor i
                    print(" ",end=' ') # printing spaces
            print() #an empty print() for next line
    def inverted_v_shaped_alpha_pat_84(self):
        for i in range(1,self.n+1): # Loop for number of rows
            for j in range(self.n-i+2): # First inner loop to print spaces before the characters in each line, starting from n-i+2
                print(' ',end='')
            for k in range(1,i+1): # Second inner loop to print characters in the shape of an isosceles triangle
                if k==1 or k==i:
                    print(chr(64+i),end=' ') # Printing the character 'A+i' at the beginning and end of each line
                else:
                    print(" ",end=' ') # Printing a space for the inner characters
            print() # Moving to the next line after completing the inner loops
    def inverted_v_shaped_alpha_pat_85(self):
        for i in range(1,self.n+1): # Loop to iterate through rows
            for j in range(self.n-i): # Loop to add leading spaces for formatting
                print(' ',end='')
            for k in range(1,i+1): # Loop to print characters for the current row
                if k==1 or k==i:
                    print(chr(65+self.n-i),end=' ')  # Print the uppercase letter based on the pattern
                else:
                    print(" ",end=' ')
            print()# Move to the next line after completing the row
    def v_shaped_pat_86(self):
        for i in range(self.n,-1,-1): # loop for n number of rows
            for j in range(self.n-i):  # loop for n-i number of spaces in each row
                print(' ',end='') # printing n-i spaces
            for k in range(i+1):  # loop for i number of columns
                if k==0 or k==i:  #Checking whether the value of k is equal to 0 or i.
                    print("*",end=' ') # printing i value if the k value is either 1 or i
                else: # else block will execute if k value is neither 0 nor i
                    print(" ",end=' ') # printing spaces
            print() #an empty print() for next line
    def v_shaped_num_pat_87(self):
        for i in range(self.n): # Loop for each row
            for j in range(i): # loop for each column
                print(" ", end='') # Print spaces before numbers
            print(i + 1, end='') # Print the leftmost number
            for k in range((self.n - i - 1) * 2 - 1): # Print spaces between numbers
                print(" ", end='')
            if i < self.n - 1: # Print the rightmost number (if not the first row)
                print(i + 1, end='')
            print()  # Move to the next line after printing each row
    def v_shaped_num_pat_88(self):
        for i in range(self.n,-1,-1): # Loop to print the  triangle pattern in reverse order
            for j in range(self.n-i):  # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(' ',end='')
            for k in range(1,i+1): # Second inner loop to print numbers in the shape of an isosceles triangle
                if k==1 or k==i:
                    print(i,end=' ')  # Printing the number 'i' at the beginning and end of each line
                else:
                    print(" ",end=' ') # Printing a space for the inner numbers
            print() # Moving to the next line after completing the inner loops
    def v_shaped_alpha_pat_89(self):
        m=1
        for i in range(self.n,0,-1): # loop for n number of rows
            for j in range(self.n-i):  # loop for n-i number of spaces in each row
                print(' ',end='') # printing n-i spaces
            for k in range(i+1):  # loop for i number of columns
                if k==1 or k==i:  #Checking whether the value of k is equal to 0 or i.
                    print(chr(64+m),end=' ') # printing alphabets by adding 1 to the order of the alphabet
                else: # else block will execute if k value is neither 0 nor i
                    print(" ",end=' ') # printing spaces
            m+=1
            print() #an empty print() for next line
    def v_shaped_alpha_pat_90(self):
        for i in range(self.n,0,-1):# loop for n number of rows
            for j in range(self.n-i): # loop for n-i number ofspaces in each row
                print(' ',end='') # printing n-i spaces
            for k in range(1,i+1): # loop for i number of columns
                if k==1 or k==i: #Checking whether the value of k is equal to 1 or i.
                    print(chr(64+i),end=' ') # printing alphabetic pattern if the k value is either 1 or i
                else:  # else block will execute if k value is neither 1 nor i
                    print(' ',end=' ') # printing spaces
            print() #an empty print() for next line
    def hallow_diamond_pat_91(self):
        for i in range(self.n):  # loop for the number of rows
            print(" " * (self.n - i), end=" ")  # print asterisk separated with spaces
            for j in range(0, i + 1):  # loop for the number of columns
                if j == 0 or j == i:  # using if condition to print asterisk at the beginning and end
                    print("*", end=" ")  # print asterisk separated by spaces
                else:
                    print(" ", end=' ')  # print space between asterisks
            print()  # move to the next line after completing a row
        for i in range(self.n, -1, -1):
            print(" " * (self.n - i), end=" ")  # print spaces before the asterisks
            for j in range(i+1):
                if j == 0 or j == i :  # using if condition to print asterisk at the beginning and end
                    print("*", end=" ")  # print asterisk separated by spaces
                else:
                    print(" ", end=' ')  # print space between asterisks
            print()  # move to the next line after completing a row
    def hallow_diamond_num_pat_92(self):
        for i in range(self.n): # Loop for no.of rows
            for j in range(self.n-i): # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(' ',end='')
            for k in range(1,i+1): # Second inner loop to print numbers in the shape of an isosceles triangle
                if k==1 or k==i:
                    print(i,end=' ')  # Printing the number 'i' at the beginning and end of each line
                else:
                    print(' ',end=' ') # Printing a space for the inner numbers
            print() # Moving to the next line after completing the inner loops

        for i in range(self.n,0,-1): #Loop for no.of rows
            for j in range(self.n-i): # First inner loop to print spaces before the numbers in each line, starting from n-i
                    print(' ',end='')
            for k in range(1,i+1): # Second inner loop to print numbers in the shape of an isosceles triangle
                if k==1 or k==i:
                    print(i,end=' ') # Printing the number 'i' at the beginning and end of each line
                else:
                    print(' ',end=' ') # Printing a space for the inner numbers
            print() # Moving to the next line after completing the inner loops
    def hallow_diamond_num_pat_93(self):
        # Upper part of the pyramid
        for i in range(self.n):  #Loop to iterate through no.o lines
            for j in range(self.n-i):  # Loop to add leading spaces for formatting
                print(' ',end='')
            for k in range(1,i+1): # Loop to print numbers for the current row
                if k==1 or k==i: # Print the number n+1-i at the first and last position in the row, otherwise print a space
                    print(self.n+1-i,end=' ')
                else:
                    print(' ',end=' ')
            print() # Move to the next line after completing the row
        # Lower part of the pyramid
        for i in range(self.n,0,-1): #Loop to iterate through no.o lines
            for j in range(self.n-i):  # Loop to add leading spaces for formatting
                print(' ',end='')
            for k in range(1,i+1): # Loop to print numbers for the current row
                if k==1 or k==i:  # Print the number n+1-i at the first and last position in the row, otherwise print a space
                    print(self.n+1-i,end=" ")
                else:
                    print(' ',end=' ')
            print()
    def hallow_diamond_alpha_pat_94(self):
        for i in range(self.n): # loop for n number of rows
            for j in range(self.n-i): # loop for n-i number of spaces in each row
                print(' ',end='')# printing n-i spaces
            for k in range(1,i+1): # loop for i number of columns
                if k==1 or k==i:  #Checking whether the value of k is equal to 1 or i.
                    print(chr(64+i),end=' ') # printing alphabetic pattern if the k value is either 1 or i
                else:   # else block will execute if k value is neither 1 nor i
                    print(' ',end=' ') # printing spaces
            print()  #an empty print() for next line

        for i in range(self.n,0,-1): # loop for n number of rows
            for j in range(self.n-i): # loop for n-i number of spaces in each row
                print(' ',end='') # printing n-i spaces
            for k in range(1,i+1): # loop for i number of columns
                if k==1 or k==i:  #Checking whether the value of k is equal to 1 or i.
                    print(chr(64+i),end=' ')  # printing alphabetic pattern if the k value is either 1 or i
                else:   # else block will execute if k value is neither 1 nor i
                    print(' ',end=' ')# printing spaces
            print() #an empty print() for next line
    def hallow_diamond_alpha_pat_95(self):
        # Upper part of the pyramid
        for i in range(self.n):  #Loop to iterate through no.o lines
            for j in range(self.n-i):  # Loop to add leading spaces for formatting
                print(' ',end='')
            for k in range(1,i+1): # Loop to print numbers for the current row
                if k==1 or k==i: # Print the alphabet chr(64+n+1-i) at the first and last position in the row, otherwise print a space
                    print(chr(65+self.n-i),end=' ')
                else:
                    print(' ',end=' ')
            print() # Move to the next line after completing the row
        # Lower part of the pyramid
        for i in range(self.n,0,-1): #Loop to iterate through no.o lines
            for j in range(self.n-i):  # Loop to add leading spaces for formatting
                print(' ',end='')
            for k in range(1,i+1): # Loop to print numbers for the current row
                if k==1 or k==i:  # Print the alphabet chr(64+n+1-i) at the first and last position in the row, otherwise print a space
                    print(chr(65+self.n-i),end=" ")
                else:
                    print(' ',end=' ')
            print() # Move to the next line after completing the row
    def half_diamond_with_increasing_space_96(self):
        for i in range(self.n,-1,-1): # Loop to print the pattern in descending order
            for j in range(i): # First inner loop to print left-aligned asterisks
                print("*",end='')
            for k in range(self.n-i): # Second inner loop to print spaces, aligning to the right
                print(' ',end=' ')
            for k in range(i): # Third inner loop to print right-aligned asterisks
                print("*",end='')
            print() # Moving to the next line after completing the inner loops
    def decreasing_space_diamond_pattern_97(self):
        for i in range(self.n):  # loop for n number of rows
            for j in range(i+1):  # loop for i number of columns
                print("*",end='') # printing i number of *'s seperated by space
            for k in range(self.n-i-1):  # loop for n-i-1 number of spaces in each row
                print(" ",end=' ')  # printing n-i-1 spaces
            for m in range(i+1):  # loop for i number of columns
                print("*",end='') # printing i number of *'s seperated by space
            print() #an empty print() for next line
    def mirrored_diamond_98(self):
        for i in range(self.n):  # loop for n number of rows
            for j in range(i+1):  # loop for i number of columns
                print("*",end='') # printing i number of *'s seperated by space
            for k in range(self.n-i-1):  # loop for n-i-1 number of spaces in each row
                print(" ",end=' ')  # printing n-i-1 spaces
            for m in range(i+1):  # loop for i number of columns
                print("*",end='') # printing i number of *'s seperated by space
            print() #an empty print() for next line

        for i in range(self.n-1,0,-1):  # loop for n-1 number of rows
            for j in range(i):  # loop for i number of columns
                print("*",end='')  # printing i number of *'s seperated by space
            for k in range(self.n-i):  # loop for n-i number of spaces in each row
                print(' ',end=' ') # printing n-i spaces
            for k in range(i):  # loop for i number of columns
                print("*",end='')# printing i number of *'s seperated by space
            print() #an empty print() for next line
    def symmetrical_triangular_pat_99(self):
        if self.n%2==0: #checking whether the number is even or odd
            self.n=self.n-1 # If the number is odd decrement it by 1

        for i in range(1, self.n // 2 + 2):  # Outer loop to iterate through each line, starting from 1 up to n//2+1
            for j in range(self.n - i - self.n // 2):  # Inner loop to print spaces before the asterisks in each line, starting from n-i-n//2
                print(" ", end=" ")
            for j in range(1, 2 * i):  # Inner loop to print asterisks in each line, starting from 1 up to 2i-1
                print("*", end=" ")

            for j in range(self.n - i - self.n // 2):  # Inner loop to print spaces before the asterisks in each line, starting from n-i-n//2
                print("   ", end=" ")
            for j in range(1, 2 * i):  # Inner loop to print asterisks in each line, starting from 1 up to 2i-1
                print("*", end=" ")

            print()  # Moving to the next line after completing the inner loops
    def symmetrical_triangular_pat_100(self):
        for i in range(1,self.n+1): # Outer loop to print the pattern in ascending order
            for j in range(self.n-i): # First inner loop to print spaces, aligning to the left
                print(" ",end='')
            for k in range(1,i+1): # Second inner loop to print left-aligned asterisks
                print("*",end=' ')
            for j in range(self.n-i):  # Third inner loop to print spaces, aligning to the right
                print(" ",end=' ')
            for k in range(1,i+1): # Fourth inner loop to print right-aligned asterisks
                print("*",end=' ')
            print() # Moving to the next line after completing the inner loops


    