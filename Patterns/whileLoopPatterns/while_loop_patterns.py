class Patterns:
    '''This is a class containing Patterns'''
    def __init__(self,n):
        assert type(n)==int,"ValueError: integer is needed "
        self.n=n
    def square_grid_pat_1(self):
        i=0  #Initializing i to zero
        while i<self.n: #Using a while loop to iterate as long as i is less than n
            print("* "*self.n) #Printing a row of asterisks '*' multiplied by the value of 'n'
            i+=1 #Incrementing the value of i by 1 in each iteration
    def square_grid_num_pat_2(self):
        i=1 # initializing i value for outer loop
        while i in range(1,self.n+1): # loop for n number of rows
            j=1 # initializing j value for inner loop
            while j in range(1,self.n+1): # loop for n number of rows
                print(i,end=' ') # printing the i value and all the elements in a row are seperated with space
                j+=1 # incrementing j value
            i+=1 # incrementing i value
            print() # An empty print() method for next line
    def square_grid_num_pat_3(self):
        i=1 # initializing i value for outer loop
        while i in range(1,self.n+1): # loop for n number of rows
            j=1 # initializing j value for inner loop
            while j in range(1,self.n+1): # loop for n number of rows
                print(j,end=' ') # printing the j value and all the elements in a row are seperated with space
                j+=1 # incrementing j value
            i+=1 # incrementing i value
            print() # An empty print() method for next line
    def square_grid_alpha_pat_4(self):
        i=65 #Initializing i value for the outer loop with ASCII value 'A'
        while i<=65+self.n-1: #Outer loop to iterate through each line
            j=0 #Initializing z for the inner loop
            while j<=self.n-1: #Inner loop to print characters in each line
                print(chr(i),end=" ") #Printing the character corresponding to the ASCII value of i
                j+=1 #Incrementing j to move to the next character in the line
            print() #Moving to the next line after completing the inner loop
            i+=1 #Incrementing i to move to the next character for the next line.
    def square_grid_alpha_pat_5(self):
        i=0 # Initializing a variable i with value 0
        while i<self.n: # Outer while loop iterating as long as i is less than n
            j=0 # Initializing a variable j with value 0 for each row
            while j<self.n: # Inner while loop iterating as long as j is less than n
                print(chr(65+j), end=" ") # Printing the uppercase letter corresponding to the ASCII value
                j+=1 # Incrementing the value of j by 1 in each iteration
            i+=1
            print() # Moving to the next line after each inner loop completes
    def square_grid_num_pat_6(self):
        i=self.n #initializing i value to n
        while i!=0: #loop for n number of columns
            j=self.n # initializing j value to n
            while j!=0: # loop for n number of columns
                print(i,end=' ') # printing i value
                j-=1 # decrementing j value
            i-=1 # decrementing i value
            print() # An empty print() method for next line
    def square_grid_num_pat_7(self):
        i=self.n #initializing i value to n
        while i!=0: #loop for n number of columns
            j=self.n # initializing j value to n
            while j!=0: # loop for n number of columns
                print(j,end=' ') # printing j value
                j-=1 # decrementing j value
            i-=1 # decrementing i value
            print() # An empty print() method for next line
    def square_grid_alpha_pat_8(self):
        i=65+self.n-1 #Initializing i value for the outer loop with ASCII value of 'A'+n-1
        while i>=65:#Outer loop to iterate through each line, starting from the ASCII value of 'A'+n-1 and going backward to 'A'
            j=0 #Initializing j for the inner loop
            while j<=self.n-1: #Inner loop to print the characters in each line
                print(chr(i),end=" ") #Printing the character corresponding to the ASCII value of i
                j+=1 #Incrementing j to move to the next character in the line
            print()#Moving to the next line after completing the inner loop
            i-=1 #Decrementing i to move to the next character for the next line.
    def square_grid_alpha_pat_9(self):
        i=0 # Initializing a variable i with value 0
        while i<self.n: # Outer while loop iterating as long as i is less than n
            j=0 # Initializing a variable j with value 0 for each row
            while j<self.n: # Inner while loop iterating as long as j is less than n
                print(chr(64+self.n-j),end=" ") # Printing the uppercase letter corresponding to the ASCII value (64 + n - j)
                j+=1 # Incrementing the value of j by 1 in each iteration
            print()  # Moving to the next line after each inner loop completes
            i+=1 # Incrementing the value of i by 1 after each outer loop iteration
    def increasing_triangular_pat_10(self):
        i=1 # initializing i value as 1
        while i<=self.n: #loop for n number of rows
            j=1 # innitializing j value as 1
            while j<=i: # loop for i number of columns for each row
                print("*",end=' ') # printing * seperated bt space
                j+=1 # incrementing j value
            i+=1 # incrementing i value
            print() # An empty print() method for next line
    def increasing_triangular_num_pat_11(self):
        i=1 # initializing i value as 1
        while i<=self.n: #loop for n number of rows
            j=1 # innitializing j value as 1
            while j<=i: # loop for i number of columns for each row
                print(i,end=' ') # printing i seperated by space
                j+=1 # incrementing j value
            i+=1 # incrementing i value
            print() # An empty print() method for next line
    def increasing_triangular_num_pat_12(self):
        i=0  #Initializing i for the outer loop
        while i in range(0,self.n): #Outer loop to iterate through each line, starting from 0 up to n-1
            j=0 #Initializing j for the inner loop
            while j in range(i+1): #inner loop to print numbers in each line, starting from 0 upto i+1
                print(j+1,end=' ') #Printing the value of j+1 with a space after it
                j+=1 #Incrementing j to move to the next position in the line
            i+=1 #Incrementing i to move to the next line for the outer loop
            print() #Moving to the next line after completing the inner loop
    def increasing_triangular_alpha_pat_13(self):
        i=0 # Initializing a variable i with value 0
        while i<self.n: # Outer while loop iterating as long as i is less than n
            j=0  # Initializing a variable j with value 0 for each row
            while j<i+1: # Inner while loop iterating as long as j is less than i+1
                print(chr(65+i),end=" ") # Printing the uppercase letter corresponding to the ASCII value (65 + i)
                j+=1 # Incrementing the value of j by 1 in each iteration
            print() # Moving to the next line after each inner loop completes
            i+=1  # Incrementing the value of i by 1 after each outer loop iteration
    def increasing_triangular_alpha_pat_14(self):
        i=0 # initializing i value as 0
        while i in range(0,self.n): # loop for n number of rows
            j=0 # initializing j value as 0
            while j in range(i+1): # loop for i+1 number of columns for each row
                print(chr(65+j),end=' ') # printing alphabet pattern
                j+=1 # incrementing j value
            i+=1 # incrementing i value
            print() # An empty print() method for next line
    def decreasing_triangular_pat_15(self):
        i=self.n # initializing loop variable i as n
        while i>0: # loop for n number of rows
            j=0 # initializing j as 0
            while j<i: # loop for i number of columns
                print("*",end=' ') # printing *'s seperated by space
                j+=1 #incrementing j value
            i-=1 # decrementing i value
            print() # An empty print() method for next line
    def decreasing_triangular_num_pat_16(self):
        i=self.n-1 #Initializing i for the outer loop, starting from n-1
        c=1 #Initializing c to 1
        while i>0: #Outer loop to iterate trough each line, starting from n-1 and going down to 1
            j=0 #Initializing j for the inner loop
            while j<i: #Inner loop to print numbers in each line, from 1 upto i
                print(c,end=' ') #Printing the value of c with a space after it
                j+=1 #Incrementing j to kove to the next position in the line
            i-=1 #Decrementing i to move to the next line for the outer loop
            c+=1 #Incrementing c for the next number
            print() #Moving to the next line after completing the inner loop
    def decreasing_triangular_num_pat_17(self):
        i=0 # Initializing a variable i with value 0
        while i<self.n: # Outer while loop iterating as long as i is less than n
            j=0  # Initializing a variable j with value 0 for each row
            while j<self.n-i:  # Inner while loop iterating as long as j is less than n-i
                print(j+1,end=" ") # Printing the current value of j+1
                j+=1 # Incrementing the value of j by 1 in each iteration
            print() # Moving to the next line after each inner loop completes
            i+=1  # Incrementing the value of i by 1 after each outer loop iteration
    def decreasing_triangular_alpha_pat_18(self):
        i=self.n # initializing loop variable i as n
        c=0
        while i>0: # loop for n number of rows
            j=0 # initializing j as 0
            while j<i: # loop for i number of columns
                print(chr(65+c),end=' ') # printing alphabet pattern
                j+=1 #incrementing j value
            i-=1 # decrementing i value
            c+=1
            print() # An empty print() method for next line
    def decreasing_triangular_alpha_pat_19(self):
        i=self.n # initializing loop variable i as n
        while i>0: # loop for n number of rows
            j=0 # initializing j as 0
            while j<i: # loop for i number of columns
                print(chr(65+j),end=' ') # printing alphabet pattern
                j+=1 #incrementing j value
            i-=1 # decrementing i value
            print() # An empty print() method for next line
    def decreasing_triangular_num_pat_20(self):
        i=self.n #Initializing i for the outer loop, starting from the user input value.
        while i>0: #Outer loop to iterate through each line, starting from the user input value and going down to 1
            j=0 #Initializing j for inner loop
            while j<i: #Inner loop to print numbers in each line, starting from the current value of i
                print(i,end=' ') #Printing the value of i with a space after it
                j+=1 #Incrementing j to move to the next position in the line
            i-=1 #Decrementing i to move to the next line for the outer loop
            print() #Moving to the next line after completing the inner loop
    def decreasing_triangular_num_pat_21(self):
        c=self.n # Initializing a constant value c with value of n
        i=self.n # Initializing a variable i with the value of n
        while i>-1: # Outer while loop iterating as long as i is greater than -1
            j=0 # Initializing a variable j with value 0 for each row
            while j<i: # Inner while loop iterating as long as j is less than i
                print(c-j,end=" ") # Printing the current value of c - j
                j+=1 # Incrementing the value of j by 1 in each iteration
            print() # Moving to the next line after each inner loop completes
            i-=1 # Decrementing the value of i by 1 after each outer loop iteration
    def decreasing_triangular_alpha_pat_22(self):
        i=self.n # initializing i with n
        while i>0: # loop for n number of rows
            j=0 # initializing j with 0
            while j<i: # loop for i number of columns
                print(chr(65+i-1),end=' ') # printing alphabet pattern seperated by space
                j+=1 # incrementing j value by 1
            i-=1 # decrementing i value by 1
            print() # An empty print() method for next line
    def decreasing_triangular_alpha_pat_23(self):
        ch=65+self.n
        i=self.n # initializing i with n
        while i>=0: # loop for n number of rows
            j=0 # initializing j with 0
            while j<=i: # loop for i number of columns
                print(chr(ch-j),end=' ') # printing alphabet pattern seperated by space
                j+=1 # incrementing j value by 1
            i-=1 # decrementing i value by 1
            print() # An empty print() method for next line
    def right_aligned_triangular_pat_24(self):
        i=0 #Initializing i for the outer loop
        while i<self.n+1: #Outer loop to iterate through each line, starting from 0 upto n+1
            j,k=0,0 #Inintializing j for the first inner loop and k for the next inner loop
            while j<self.n-i: #First inner loop to print spaces before stars in each line, starting from n-i
                print(" ",end=' ')
                j+=1
            while k<i: #Second inner loop to print stars in each line, starting from 0 upto i
                print("*",end=' ')
                k+=1
            i+=1
            print()
    def right_aligned_triangular_num_pat_25(self):
        i=0 # Initializing a variable i with value 0
        while i<self.n+1: # Outer while loop iterating as long as i is less than n+1
            j,k=0,0  # Initializing variables j and k with value 0 for each row
            while j<self.n-i: # First inner while loop to print spaces before the numbers
                print(" ",end=" ")
                j+=1
            while k<i: # Second inner while loop to print numbers with increasing values
                print(i,end=" ")
                k+=1
            i+=1  # Incrementing the value of i by 1 after each outer loop iteration
            print() # Moving to the next line after each row completes
    def right_aligned_triangular_num_pat_26(self):
        i=1 # initializing i value as 1
        while i in range(1,self.n+1): # loop for n number of rows
            j,k=0,1 # initializing j and k values as 0 and 1 respectively
            while j in range(self.n-i): # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k in range(1,i+1): # loop for i number of columns
                print(k,end=' ') # printing k value seperated by space
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print() # An empty print() method for next line
    def right_aligned_triangular_alpha_pat_27(self):
        i=1 # initializing i value as 1
        while i in range(1,self.n+1): # loop for n number of rows
            j,k=0,1 # initializing j and k values as 0 and 1 respectively
            while j in range(self.n-i): # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k in range(1,i+1): # loop for i number of columns
                print(chr(64+i),end=' ') # printing alphabetic pattern seperated by space
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print() # An empty print() method for next line
    def right_aligned_triangular_alpha_pat_28(self):
        i=0# Initializing i for the outer loop
        while i in range(self.n+1):# Outer loop to iterate through each line, starting from 0 up to n
            j,k=0,65# Initializing j for the first inner loop and k for next inner loop
            while j in range(self.n-i):# First inner loop to print spaces before the characters in each line, starting from n-i
                print(" ",end=' ')
                j+=1
            while k in range(65,65+i):# Second inner loop to print characters in each line, starting from 'A' up to 'A'+i-1
                print(chr(k),end=' ')
                k+=1
            i+=1# Incrementing i to move to the next line for the outer loop
            print()# Moving to the next line after completing the inner loops
    def right_aligned_decreasing_triangular_pat_29(self):
        i=0 # Initializing a variable i with value 0
        while i<self.n: # Outer while loop iterating as long as i is less than n
            j,k=0,0 # Initializing variables j and k with value 0 for each row
            while j<i: # First inner while loop to print spaces before the asterisks
                print(" ",end=" ")
                j+=1
            while k<self.n-i: # Second inner while loop to print asterisks
                print("*",end=" ")
                k+=1
            i+=1  # Incrementing the value of i by 1 after each outer loop iteration
            print()  #Moving to the next line after each row completes
    def right_aligned_decreasing_triangular_num_pat_30(self):
        i=self.n # assigining i value with n
        while i>0: # loop for n number of rows
            j,k=0,0 # assigning j and k values with 0
            while j in range(self.n-i): #loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k in range(i): # loop for i number of columns
                print(i,end=' ') # printing i value - i times seperated by space
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print() # an empty print() for next line
    def right_aligned_decreasing_triangular_num_pat_31(self):
        i=self.n # assigining i value with n
        while i>0: # loop for n number of rows
            j,k=0,1 # assigning j and k values with 0
            while j in range(self.n-i): #loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k in range(i+1): # loop for i number of columns
                print(k,end=' ') # printing k value seperated by space
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print() # an empty print() for next line
    def right_aligned_decreasing_triangular_alpha_pat_32(self):
        i=self.n #Initializing i for the outer loop, starting from the user input value
        while i in range(self.n,0,-1):# Outer loop to iterate through each line, starting from n and going down to 1
            j,k=0,65# Initializing j for the first inner loop and k for next inner loop
            while j in range(self.n-i+1):# First inner loop to print spaces before the characters in each line, starting from n-i+1
                print(" ",end=' ')
                j+=1
            m=65# Initializing m to the ASCII value of 'A'
            while k in range(65,65+i):# Second inner loop to print characters in each line, starting from 'A' up to 'A'+i-1
                print(chr(m+i-1),end=' ')
                k+=1
            i-=1# Decrementing i to move to the next line for the outer loop
            print()# Moving to the next line after completing the inner loops
    def right_aligned_decreasing_triangular_alpha_pat_33(self):
        i=self.n # Initializing a variable i with the value of n
        while i>0: # Outer while loop iterating as long as i is greater than 0
            j,k=0,0 # Initializing variables j and k with value 0 for each row
            while j<self.n-i:  # First inner while loop to print spaces before the letters
                print(" ",end=" ") # printing spaces
                j+=1 # incrementing j value
            while k<i:  # Second inner while loop to print letters with increasing values
                print(chr(65+k),end=" ") # printing alphaetic pattern
                k+=1 #incrementing k value
            print() # Moving to the next line after each row completes
            i-=1  # Decrementing the value of i by 1 after each outer loop iteration
    def increasing_triangular_pat_34(self):
        i=1 # assigning i with 1
        while i<=self.n: # loop for n number of rows
            j,k=0,1 # assigining j and k with 0 and 1 respectively
            while j<self.n-i: # loop for n-i spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i: # loop for i number of columns
                print("*",end=' ') # printing i number of *'s seperated by space
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print() # an empty print() for next line
    def increasing_triangular_num_pat_35(self):
        i=1 # initializing i with 1
        while i<=self.n: # loop for n number of rows
            k,j=0,0 # initializing k and j with 0
            while j<self.n-i: # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k<i*2-1: # loop for i*2-1 columns
                print(i,end=' ') # printing alphabet pattern seperated by space
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print()
    def increasing_triangular_num_pat_36(self):
        i,j,m=1,0,1# Initializing i to 1, j to 0, and m to 1
        while i<self.n//2+2:# Outer loop to iterate through each line, starting from 1 up to n//2+2
            j,k=0,0 # Initializing j for the first inner loop and k for secon inner loop
            while j<self.n-i:# First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end=' ')
                j+=1
            while k<2*i-1:# Second inner loop to print numbers in each line, starting from the current value of m
                print(m,end=' ')
                k+=1
            m+=2
            i+=1 # Incrementing i to move to the next line for the outer loop
            print()# Moving to the next line after completing the inner loops
    def increasing_triangular_alpha_pat_37(self):
        i=0 # Initializing a variable i with value 0
        while i<self.n: # Outer while loop iterating as long as i is less than n
            j,k=0,0  # Initializing variables j and k with value 0 for each row
            while j<self.n-i:  # First inner while loop to print spaces before the letters
                print(" ",end=" ")
                j+=1
            while k<i*2+1:  # Second inner while loop to print letters with increasing values
                print(chr(65+i),end=" ")
                k+=1
            print() # Moving to the next line after each row completes
            i+=1 # Incrementing the value of i by 1 after each outer loop iteration
    def increasing_triangular_alpha_pat_38(self):
        i,x=0,0 # initializing i and x with 0
        while i<self.n//2: # loop for n/2 rows
            j,k=0,0 # initializing j and k with 0
            while j<self.n-i:  # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k<i*2+1: # loop for i*2+1 columns
                print(chr(65+x),end=' ') # printing alphabet pattern seperated by space
                k+=1 # incrementing k value
            x+=2 # incrementing x value
            i+=1 # incrementing i value
            print() #an empty print() for next line
    def increasing_triangular_num_pat_39(self):
        i=1 # initializing i with 1
        while i<=self.n//2: # loop for n/2 number of rows
            k,j=1,0 # initializing k and j with 1 and 0
            while j<self.n-i: # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i*2-1: # loop for i*2-1 columns
                print(k,end=' ') # printing alphabet pattern seperated by space
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print() #an empty print() for next line
    def increasing_triangular_num_pat_40(self):
        i,x=0,1# Initializing i to 0 and x to 1
        while i<=self.n//2:# Outer loop to iterate through each line, starting from 0 up to n//2
            k,j=0,0 #Initializing  k and j values for inner loops
            while j<self.n-i-self.n//2-1:# First inner loop to print spaces before the numbers in each line, starting from n-i-n//2-1
                print(" ",end=" ")
                j+=1
            while k < 2*i+1:# Second inner loop to print numbers in each line, starting from x-k and going up to x+2*i
                print(x-k,end=" ")
                k+=1
            x+=2 #Incrementing x by 2 for the next number
            i+=1 #Incrementing i to move to the next line for the outer loop
            print() # Moving to the next line after completing the inner loops
    def increasing_triangular_alpha_pat_41(self):
        i=0 # Initializing a variable i with value 0
        while i<self.n//2+1: # Outer while loop iterating as long as i is less than n//2 + 1
            j,k=0,0  # Initializing variables j and k with value 0 for each row
            while j<self.n-i-self.n//2:  # First inner while loop to print spaces before the letters
                print(" ",end=" ")
                j+=1
            while k<i*2+1: # Second inner while loop to print letters with increasing values
                print(chr(65+k),end=" ")
                k+=1
            print() # Moving to the next line after each row completes
            i+=1 # Incrementing the value of i by 1 after each outer loop iteration
    def increasing_triangular_alpha_pat_42(self):
        i=x=0 # initializing i and x with 0
        while i<=self.n//2: # loop for n/2 rows
            k,j=0,0 # initializing k and j with 0
            while j<self.n-i: # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k<i*2+1: # loop for i*2+1 columns
                print(chr(65+x-k),end=' ') # printing alphabet pattern seperated by space
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            x+=2 # incrementing x value
            print() #an empty print() for next line
    def increasing_triangular_num_pat_43(self):
        i=0 # initializing i with 0
        while i<=self.n: # loop for n+2 rows
            j,m=0,1 # initializing j and m with 0 and 1
            k=i # initializing k with i-1
            while j<self.n-i: # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k>=0: # loop for i-1 number of columns
                print(k,end=' ') # printing k value seperated by space
                k-=1 #decrementing k value
            while m<=i: # loop for i number of  columns
                print(m,end=' ') # printing m value seperated by space
                m+=1 # incrementing m value
            i+=1 # incrementing i value
            print() #an empty print() for next line
    def increasing_triangular_alpha_pat_44(self):
        i=1 # Initializing i to 1 for the outer loop
        while i<=self.n: # Outer loop to iterate through each line, starting from 1 up to n
            j,k,m=0,i-1,0 # Initializing j for the first inner loop and k for the second inner loop, starting from i-1 and m for the third inner loop
            while j<self.n-i: # First inner loop to print spaces before the characters in each line, starting from n-i
                print(" ",end=" ")
                j+=1
            while k>0: # Second inner loop to print characters in descending order, starting from 'A'+k and going down to 'A'
                print(chr(65+k),end=" ")
                k-=1
            while m<i: # Third inner loop to print characters in ascending order, starting from 'A' and going up to 'A'+m
                print(chr(65+m),end=" ")
                m+=1
            i+=1 # Incrementing i to move to the next line for the outer loop
            print() # Moving to the next line after completing the inner loops
    def increasing_triangular_num_pat_45(self):
        i=1 # Initializing a variable i with value 1
        while i<self.n+1: # Outer while loop iterating as long as i is less than n+1
            j,k,l=1,1,i-1 # Initializing variables j, k, and l with values 1, 1, and i-1 for each row
            while j<=self.n-i: # First inner while loop to print spaces before the numbers
                print(" ",end=" ")
                j+=1
            while k<i+1: # Second inner while loop to print numbers in increasing order
                print(k,end=" ")
                k+=1
            while l>0:  # Third inner while loop to print numbers in decreasing order
                print(l,end=" ")
                l-=1
            print() # Moving to the next line after each row completes
            i+=1 # Incrementing the value of i by 1 after each outer loop iteration
    def increasing_triangular_alpha_pat_46(self):
        i=0 # initializing i with 0
        while i<=self.n: # loop for n rows
            j=k=0 # initializing j and k with 0
            m=i-1 # initializing m with i-1
            while j<self.n-i: # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k<i: # loop for i number of columns
                print(chr(65+k),end=' ') # printing alphabet pattern seperated by space
                k+=1 #incrementing k value
            while m>0: # loop for i-1 number of  columns
                print(chr(65+m-1),end=' ') # printing alphabet pattern seperated by space
                m-=1 # decrementing m value
            i+=1 # incrementing i value
            print() #an empty print() for next line
    def left_aligned_decreasing_triangular_pat_47(self):
        i=self.n//2+1 # initializing i with n/2+1
        while i>0: # loop for n/2+1 rows
            j,k=0,1 # initializing j and k with 0 and 1 respectively
            while j<self.n-i: # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k <i*2: # loop for i*2 columns
                print("*",end=' ') # printing *'s seperated by space
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print() # an empty print() for next line
    def left_aligned_decreasing_triangular_num_pat_48(self):
        m=2 # Initializing m to 2
        i=self.n-1 # Initializing i to n-1 for the outer loop
        while i>-1: # Outer loop to iterate through each line, starting from n-1 and going down to 0
            j,k=0,0  # Initializing j for the first inner loop and k for next inner loop
            while j<self.n-i: # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end=" ")
                j+=1
            while k<self.n+i-m: # Second inner loop to print numbers in each line, starting from n+i-m and going down to n
                print(i,end=" ")
                k+=1
            m+=1
            i-=1 # Decrementing i to move to the next line for the outer loop
            print() # Moving to the next line after completing the inner loops
    def left_aligned_decreasing_triangular_num_pat_49(self):
        i=self.n # Initializing a variable i with value n
        while i>0: # Outer while loop iterating as long as i is greater than 0
            j,k=0,0 # Initializing variables j and k with value 0 for each row
            while j<self.n-i//2-self.n//2+1: # First inner while loop to print spaces before the numbers
                print(" ",end=" ")
                j+=1
            while k<i: # Second inner while loop to print numbers with the value of i
                print(i,end=" ")
                k+=1
            print() # Moving to the next line after each row completes
            i-=2 # Decrementing the value of i by 2 after each outer loop iteration
    def inverted_pyramid_num_pat_50(self):
        i=self.n//2+1 # initializing i with n/2+1
        while i>0: # loop for n/2+1 rows
            j,k=0,1 # initializing j and k with 0 and 1 respectively
            while j<self.n-i: # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k <i*2: # loop for i*2 columns
                print(k,end=' ') # printing k value seperated by space
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print() # an empty print() for next line
    def inverted_pyramid_alpha_pat_51(self):
        i=self.n # initializing i with n
        while i>0: # loop for n rows
            j,k=0,1 # initializing j and k with 0 and 1 respectively
            while j<self.n-i: # loop for n-i spaces in each row
                print(" ",end=' ') # printing n-i spaces
                j+=1 # incrementing j value
            while k <i*2: # loop for i*2 columns
                print(chr(64+i),end=' ') # printing alphabetic pattern seperated by space
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print() # an empty print() for next line
    def inverted_pyramid_alpha_pat_52(self):
        p=65+self.n*2-2 # Initializing p to the ASCII value of 'A' + n*2 - 2
        m=1 # Initializing m to 1
        i=self.n # Initializing i to n for the outer loop
        while i>0: # Outer loop to iterate through each line, starting from n and going down to 1
            j,k=0,0 # Initializing j for the first inner loop and k for second inner loop
            while j<self.n-i+1: # First inner loop to print spaces before the characters in each line, starting from n-i+1
                print(" ",end=" ")
                j+=1
            while k<self.n+i-m: # Second inner loop to print characters in each line, starting from the current ASCII value of p and going up to n+i-m
                print(chr(p),end=" ")
                k+=1
            p-=2
            m+=1
            i-=1  # Decrementing i to move to the next line for the outer loop
            print() # Moving to the next line after completing the inner loops
    def inverted_pyramid_alpha_pat_53(self):
        m=0 # Initializing a variable m with value 0
        i=self.n//2+1 # Initializing a variable i with value n//2 + 1
        while i>0: # Outer while loop iterating as long as i is greater than 0
            print(" "*m,end=" ")  # Printing spaces before the letters based on the value of m
            j=0
            while j<i*2-1: # Inner while loop to print letters in increasing order
                print(chr(65+j),end=" ")
                j+=1
            m+=2
            print() # Moving to the next line after each row completes
            i-=1 # Decrementing the value of i by 1 after each outer loop iteration
    def alternating_triangular_pat_54(self):
        i=0 # initializing i with 0
        while i<self.n: # loop for n number of rows
            j=0 # initializing j with 0
            while j<i: # loop for i number of columns
                print("*",end=' ') # printing j number of *'s seperated by space
                j+=1 # incrementing j value
            i+=1 # incrementing i value
            print() #an empty print() for next line
        while i>0: # loop for n-1 number of rows
            j=0 # initializing j with 0
            while j<i: # loop for i number of columns
                print("*",end=' ') # printing j number of *'s seperated by space
                j+=1 # incrementing j value
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def alternating_triangular_num_pat_55(self):
        i=0 # initializing i with 0
        while i<=self.n: # loop for n number of rows
            j=0 # initializing j with 0
            while j<i: # loop for i number of columns
                print(self.n-j,end=' ') # printing n-j values seperated by space
                j+=1 # incrementing j value
            i+=1 # incrementing i value
            print() #an empty print() for next line

        while i>0: # loop for n-1 number of rows
            j=0 # initializing j with 0
            while j<i: # loop for i number of columns
                print(self.n-j,end=' ') # printing n-j values seperated by space
                j+=1 # incrementing j value
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def alternating_triangular_num_pat_56(self):
        # First part of the pattern: Increasing order
        i=0
        while i<self.n: # Initializing j to i for the first inner loop
            j=i
            while j>-1: # Inner loop to print numbers in decreasing order from n to n-j
                print(self.n-j,end=' ')
                j-=1
            i+=1 # Incrementing i to move to the next line
            print() # Moving to the next line after completing the inner loop
        # Second part of the pattern: Decreasing order
        while i>=0: # Initializing j to i for the second inner loop
            j=i
            while j>-1: # Inner loop to print numbers in decreasing order from n to n-j
                print(self.n-j,end=' ')
                j-=1
            i-=1 # Decrementing i to move to the next line
            print() # Moving to the next line after completing the inner loop
    def alternating_triangular_alpha_pat_57(self):
        i=0 # initializing i with 0
        while i<=self.n: # loop for n number of rows
            j=0 # initializing j with 0
            while j<i: # loop for i number of columns
                print(chr(65+self.n-j),end=' ') # printing alphabetic pattern seperated by space
                j+=1 # incrementing j value
            i+=1 # incrementing i value
            print() #an empty print() for next line

        while i>0: # loop for n-1 number of rows
            j=0 # initializing j with 0
            while j<i: # loop for i number of columns
                print(chr(65+self.n-j),end=' ') # printing Alphabetic pattern seperated by space
                j+=1 # incrementing j value
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def alternating_triangular_alpha_pat_58(self):
        i=0 # initializing i with 0
        while i<self.n: # loop for n number of rows
            j=i # initializing j with i
            while j>-1: # loop for i number of columns
                print(chr(65+self.n-j),end=' ') #Printing alphabet pattern seperated by space
                j-=1 # decrementing j value
            i+=1 # incrementing i value
            print() #an empty print() for next line

        while i>=0: # loop for n number of rows
            j=i # initializing j with i
            while j>-1: # loop for i number of columns
                print(chr(65+self.n-j),end=' ') #Printing alphabet pattern seperated by space
                j-=1 # decrementing j value
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def left_pascal_triangle_pat_59(self):
        i=0 #initializing i with 0
        while i<self.n:  # loop for n number of rows
            x=0 # initializing x with 0
            j=k=0 # initializing j and k with 0
            while k<self.n-i: # loop for n -i number of spaces in each row
                print(' ',end=' ') # printing n-i spaces
                k+=1 # incrementing k value
                x+=1 # incrementing x value
            while j<i:  # loop for i number of columns
                print("*",end=' ') # printing *'s pattern seperated by space
                j+=1 # incrementing j value
                x+=1 # incrementing x value
            i+=1 # incrementing i value
            print() #an empty print() for next line

        while i>0:  # loop for n number of rows
            x=0 # initializing x with 0
            j=k=0 #initializing j and k with 0
            while k<self.n-i: # loop for n -i number of spaces in each row
                print(' ',end=' ') # printing n-i spaces
                k+=1 # incrementing k value
                x+=1 # incrementing x value
            while j<i:  # loop for i number of columns
                print("*",end=' ') # printing *'s pattern seperated by space
                j+=1 # incrementing j value
                x+=1 # incrementing x value
            i-=1 # decrement i value
            print() #an empty print() for next line
    def left_pascal_triangle_num_pat_60(self):
        i=0
        # First part of the pattern: Increasing order
        while i<self.n:
            j=k=0 # Initializing j and k for the inner loops
            while k<self.n-i: # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(' ',end=' ')
                k+=1
            while j<i+1: # Second inner loop to print numbers in decreasing order
                print(self.n-j,end=' ')
                j+=1
            i+=1  # Incrementing i for the next line
            print() # Moving to the next line after completing the inner loops
        # Second part of the pattern: Decreasing order
        i=self.n
        while i>-1:
            j=k=0 # Initializing j and k for the inner loops
            while k<self.n-i: # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(' ',end=' ')
                k+=1
            while j<i+1: # Second inner loop to print numbers in decreasing order
                print(self.n-j,end=' ')
                j+=1
            i-=1 # Decrementing i for the next line
            print() # Moving to the next line after completing the inner loops
    def left_pascal_triangle_num_pat_61(self):
        # First part of the pattern
        i=0 #Initializing i to 0
        while i<self.n: #Loop for no.of rows
            x,j,k=0,0,0 #Initializing x,j,k to 0
            while j<self.n-i: # Printing spaces before the numbers
                print(" ",end=' ')
                x+=1
                j+=1
            while k<i+1: # Printing numbers in increasing order
                print(x,end=' ')
                x+=1
                k+=1
            print() # Moving to the next line after each row completes
            i+=1
        # Second part of the pattern
        i=self.n #Initializing i to n
        while i>-1: #Loop for no.of rows
            x,j,k=0,0,0
            while j<self.n-i: # Printing spaces before the numbers
                print(" ",end=' ')
                x+=1
                j+=1
            while k<i+1: # Printing numbers in increasing order
                print(x,end=' ')
                k+=1
                x+=1
            print() # Moving to the next line after each row completes
            i-=1
    def left_pascal_triangle_alpha_pat_62(self):
        i=0 #initializing i with 0
        while i<self.n:  # loop for n number of rows
            x=0 # initializing x with 0
            j=k=0 # initializing j and k with 0
            while k<self.n-i: # loop for n -i number of spaces in each row
                print(' ',end=' ') # printing n-i spaces
                k+=1 # incrementing k value
                x+=1 # incrementing x value
            while j<i:  # loop for i number of columns
                print(chr(ord('A')+x),end=' ') # printing alphabetical pattern seperated by space
                j+=1 # incrementing j value
                x+=1 # incrementing x value
            i+=1 # incrementing i value
            print() #an empty print() for next line

        while i>0:  # loop for n number of rows
            x=0 # initializing x with 0
            j=k=0 #initializing j and k with 0
            while k<self.n-i: # loop for n -i number of spaces in each row
                print(' ',end=' ') # printing n-i spaces
                k+=1 # incrementing k value
                x+=1 # incrementing x value
            while j<i:  # loop for i number of columns
                print(chr(ord('A')+x),end=' ') # printing alphabetical pattern seperated by space
                j+=1 # incrementing j value
                x+=1 # incrementing x value
            i-=1 # decrement i value
            print() #an empty print() for next line

    def left_pascal_triangle_alpha_pat_63(self):
        i=0 #initializing i with 0
        while i<self.n:  # loop for n number of rows
            x=0 # initializing x with 0
            j=k=0 # initializing j and k with 0
            while k<self.n-i: # loop for n -i number of spaces in each row
                print(' ',end=' ') # printing n-i spaces
                k+=1 # incrementing k value
                x+=1 # incrementing x value
            while j<=i:  # loop for i number of columns
                print(chr(65+self.n-j),end=' ') # printing alphabetical pattern seperated by space
                j+=1 # incrementing j value
                x+=1 # incrementing x value
            i+=1 # incrementing i value
            print() #an empty print() for next line

        while i>=0:  # loop for n number of rows
            x=0 # initializing x with 0
            j=k=0 #initializing j and k with 0
            while k<self.n-i: # loop for n -i number of spaces in each row
                print(' ',end=' ') # printing n-i spaces
                k+=1 # incrementing k value
                x+=1 # incrementing x value
            while j<=i:  # loop for i number of columns
                print(chr(65+self.n-j),end=' ') # printing alphabetical pattern seperated by space
                j+=1 # incrementing j value
                x+=1 # incrementing x value
            i-=1 # decrement i value
            print() #an empty print() for next line

    def increasing_triangular_pat_64(self):
        i=0 # Initializing i to 0 for the outer loop
        while i<=self.n:
            j,k=0,1  # Initializing j and k to 0 and 1, respectively, for the inner loops
            while j<self.n-i: # First inner loop to print spaces before the asterisks in each line, starting from n-i
                print(" ",end='')
                j+=1
            while k<=i: # Second inner loop to print asterisks in increasing order, starting from 1 up to i
                print("*",end=' ')
                k+=1
            i+=1  # Incrementing i for the next line
            print() # Moving to the next line after completing the inner loops
    def increasing_triangular_num_pat_65(self):
        i=0 # Initializing i to 0 for the outer loop
        while i<=self.n:
            j,k=0,1  # Initializing j and k to 0 and 1, respectively, for the inner loops
            while j<self.n-i: # First inner loop to print spaces before the asterisks in each line, starting from n-i
                print(" ",end='')
                j+=1
            while k<=i: # Second inner loop to print numbers in increasing order, starting from 1 up to i
                print(i,end=' ')
                k+=1
            i+=1  # Incrementing i for the next line
            print() # Moving to the next line after completing the inner loops
    def increasing_triangular_num_pat_66(self):
        i=1 # initializing i value with 1
        while i<=self.n: # loop for n number of rows
            j=0 # intializing j value with 0
            k=1 # initializing k with 1
            while j<self.n-i:# loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:# loop for i number of columns
                print(k,end=' ') # printing k value seperated by space
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print()  #an empty print() for next line
    def increasing_triangular_alpha_pat_67(self):
        i=0 # initializing i value with 0
        while i<=self.n: # loop for n number of rows
            j=0 # intializing j value with 0
            k=1 # initializing k with 1
            while j<self.n-i:# loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:# loop for i number of columns
                print(chr(64+i),end=' ') # printing alphabetic pattern seperated by space
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print()  #an empty print() for next line
    def increasing_triangular_alpha_pat_68(self):
        i=0 # Initializing i to 0 for the outer loop
        while i<=self.n: #Outer loop for no.of rows
            j,k=0,1 # Initializing j and k to 0 and 1, respectively, for the inner loops
            while j<self.n-i: # First inner loop to print spaces before the characters in each line, starting from n-i
                print(" ",end='')
                j+=1
            while k<=i: # Second inner loop to print characters in increasing order, starting from 'A' up to 'A+k'
                print(chr(64+k),end=' ')
                k+=1
            i+=1 # Incrementing i for the next line
            print() # Moving to the next line after completing the inner loops
    def decreasing_triangular_pat_69(self):
        i=self.n #Initializing i to n
        while i>-1: # Loop to iterate through rows in reverse order
            j,k=0,0 #Initializing j and i value to 0
            while j<self.n-i: # Loop to add leading spaces for formatting
                print(end=" ")
                j+=1
            while k<i:  # Loop to print asterisks for the current row
                print("*",end=" ")
                k+=1
            print() # Move to the next line after completing the row
            i-=1 #Decrementing i value to 1
    def decreasing_triangular_num_pat_70(self):
        i=self.n # initializing i value with n
        while i>0: # loop for n number of rows
            j=k=0 # initializing j and k with 0
            while j<self.n-i: # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<i: # loop for i number of columns
                print(i,end=' ') # printing i value - k times
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def decreasing_triangular_num_pat_71(self):
        i=self.n # initializing i value with n
        while i>0: # loop for n number of rows
            j=k=0 # initializing j and k with 0
            while j<self.n-i: # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<i: # loop for i number of columns
                print(i-k,end=' ') # printing i-k value - i times
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def decreasing_triangular_alpha_pat_72(self):
        i=self.n # Initializing i to n for the outer loop
        while i>0: #Outer loop for number of rows in descending order
            j=k=0 # Initializing j and k to 0 for the inner loops
            while j<self.n-i+1: # First inner loop to print spaces before the characters in each line, starting from n-i+1
                print(" ",end='')
                j+=1
            while k<i:  # Second inner loop to print characters in decreasing order, all being the same character 'A'+i
                print(chr(64+i),end=' ')
                k+=1
            i-=1 # Decrementing i for the next line
            print() # Moving to the next line after completing the inner loops
    def decreasing_triangular_alpha_pat_73(self):
        i=self.n #Initializing i to n
        while i>0:  # Loop to iterate through rows in reverse order
            j,k=0,0 #Initializing j,k to 0,0
            while j<self.n-i+1: # Loop to add leading spaces for formatting
                print(" ",end="")
                j+=1 #Incrementing j value to 1
            while k<i: # Loop to print uppercase letters for the current row
                print(chr(64+i-k),end=" ")
                k+=1 #Incrementing k value to 1
            print()  # Move to the next line after completing the row
            i-=1 #Decrementing i value to 1
    def decreasing_triangular_alpha_pat_74(self):
        i=self.n # initializing i value with n
        while i>0: # loop for n number of rows
            j=k=0 # initializing j and k values with 0
            while j<self.n-i: # loop for n-i number of  spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<i: # loop for i number of columns
                print(chr(65+k),end=' ') # printing alphabets pattern seperated by space
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def diamond_pat_75(self):
        i=1 # initializing i value with 1
        while i<self.n: # loop for n-1 number of rows
            j,k=0,1 # initializing j and k values with 0 and 1
            while j<self.n-i: # loop for n-i number of spaces in each row
                print(" ",end='')  # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:  # loop for i number of columns
                print("*",end=' ') # printing *'s pattern seperated by spaces
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print() #an empty print() for next line
        while i>0: # loop for n number of rows
            j,k=0,1 # initializing j and k values with 0 and 1
            while j<self.n-i: # loop for n-i number of spaces in each row
                print(" ",end='')  # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:  # loop for i number of columns
                print("*",end=' ') # printing *'s pattern seperated by spaces
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print()  #an empty print() for next line
    def diamond_num_pat_76(self):
        i=0
        # First part of the pattern: Increasing order
        while i<self.n:
            j,k=0,1 # Initializing j and k to 0 and 1, respectively, for the inner loops
            while j<self.n-i: # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end='')
                j+=1
            while k<=i: # Second inner loop to print numbers in increasing order, all being the same value 'i'
                print(i,end=' ')
                k+=1
            i+=1 # Incrementing i for the next line
            print() # Moving to the next line after completing the inner loops
        # Second part of the pattern: Decreasing order
        while i>0:
            j,k=0,1 # Initializing j and k to 0 and 1, respectively, for the inner loops
            while j<self.n-i: # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end='')
                j+=1
            while k<=i: # Second inner loop to print numbers in decreasing order, all being the same value 'i'
                print(i,end=' ')
                k+=1
            i-=1# Decrementing i for the next line
            print()  # Moving to the next line after completing the inner loops
    def diamond_num_pat_77(self):
        i=0
        # First part of the pattern: Increasing order
        while i<self.n:
            j,k=0,1 # Initializing j and k to 0 and 1, respectively, for the inner loops
            while j<self.n-i: # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end='')
                j+=1
            while k<=i: # Second inner loop to print numbers in increasing order, and printing the value of k
                print(k,end=' ')
                k+=1
            i+=1 # Incrementing i for the next line
            print() # Moving to the next line after completing the inner loops
        # Second part of the pattern: Decreasing order
        m=1
        while i>0:
            j,k=0,0 # Initializing j and k to 0 and 1, respectively, for the inner loops
            while j<self.n-i: # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end='')
                j+=1
            while k<i: # Second inner loop to print numbers in decreasing order, and printing the value of k+m
                print(k+m,end=' ')
                k+=1
            m+=1
            i-=1# Decrementing i for the next line
            print()  # Moving to the next line after completing the inner loops
    def diamond_num_pat_78(self):
        i=1 # initializing i value with 1
        while i<self.n: # loop for n-1 number of rows
            j,k=0,1 # initializing j and k values with 0 and 1
            while j<self.n-i: # loop for n-i number of spaces in each row
                print(" ",end='')  # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:  # loop for i number of columns
                print(k,end=' ') # printing k values seperated by spaces
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print() #an empty print() for next line
        while i>0: # loop for n number of rows
            j,k=0,1 # initializing j and k values with 0 and 1
            while j<self.n-i: # loop for n-i number of spaces in each row
                print(" ",end='')  # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:  # loop for i number of columns
                print(k,end=' ') # printing k values seperated by spaces
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print()  #an empty print() for next line
    def diamond_alpha_pat_79(self):
        i=1 # initializing i value with 1
        while i<self.n: # loop for n-1 number of rows
            j,k=0,1 # initializing j and k values with 0 and 1
            while j<self.n-i: # loop for n-i number of spaces in each row
                print(" ",end='')  # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:  # loop for i number of columns
                print(chr(64+i),end=' ') # printing alphabetic pattern seperated by spaces
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print() #an empty print() for next line
        while i>0: # loop for n number of rows
            j,k=0,1 # initializing j and k values with 0 and 1
            while j<self.n-i: # loop for n-i number of spaces in each row
                print(" ",end='')  # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:  # loop for i number of columns
                print(chr(64+i),end=' ') # printing alphabetic pattern seperated by spaces
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print()  #an empty print() for next line
    def diamond_alpha_pat_80(self):
        # First part of the pattern: Increasing order
        i=1
        while i<self.n+1:
            j,k=0,1 # Initializing j and k to 0 and 1, respectively, for the inner loops
            while j<self.n-i: # First inner loop to print spaces before the characters in each line, starting from n-i
                print(" ",end='')
                j+=1
            while k<=i: # Second inner loop to print characters in increasing order, starting from 'A' to 'A+k'
                print(chr(64+k),end=' ')
                k+=1
            i+=1 # Incrementing i for the next line
            print() # Moving to the next line after completing the inner loops
        # Second part of the pattern: Decreasing order
        i=1
        m=1
        while i<self.n:
            j,k=0,1 # Initializing j and k to 0 and 1, respectively, for the inner loops
            while j<i: # First inner loop to print spaces before the characters in each line, starting from i
                print(" ",end='')
                j+=1
            while k<self.n-i+1:  # Second inner loop to print characters in decreasing order, starting from 'A+k'
                print(chr(64+k+m),end=' ')
                k+=1
            m+=1
            i+=1 # Incrementing i for the next line
            print() # Moving to the next line after completing the inner loops
    def inverted_v_shaped_pat_81(self):
        i=1
        while i<=self.n+1: # Loop to iterate through rows
            j,k=0,1
            while j<=self.n-i+1:  # Loop to add leading spaces for formatting
                print(' ',end='')
                j+=1
            while k<i+1: # Loop to print characters for the current row
                if k==1 or k==i:
                    print("*",end=' ') # Print '*' if it's the first or last character in the row, otherwise print a space
                else:
                    print(" ",end=' ')
                k+=1
            i+=1
            print() # Move to the next line after completing the row
    def inverted_v_shaped_num_pat_82(self):
        i=1 # initializing i value with 1
        while i<=self.n: # loop for n number of rows
            j,k=0,1 # initializing j and k values with 0 and 1
            while j<self.n-i: # loop for n-i number of spaces in each row
                print(' ',end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i: # loop for i number of columns
                if k==1 or k==i: #Checking whether the value of k is equal to 1 or i.
                    print(i,end=' ') # printing i value if the k value is either 1 or i
                else:  # else block will execute if k value is neither 1 nor i
                    print(" ",end=' ') # printing spaces
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print() #an empty print() for next line
    def inverted_v_shaped_num_pat_83(self):
        i=0 # initializing i value with 0
        while i<self.n: # loop for n number of rows
            j,k=0,0 # initializing j and k values with 0 and 0
            while j<self.n-i: # loop for n-i number of spaces in each row
                print(' ',end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i: # loop for i number of columns
                if k==0 or k==i: #Checking whether the value of k is equal to 1 or i.
                    print(self.n-i,end=' ') # printing n-i value if the k value is either 1 or i
                else:  # else block will execute if k value is neither 1 nor i
                    print(" ",end=' ') # printing spaces
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print() #an empty print() for next line
    def inverted_v_shaped_alpha_pat_84(self):
        i=1 # Initializing the variable for the outer loop
        while i<=self.n: # Outer loop to iterate through each line
            j,k=0,1 # Initializing variables for the first and second inner loops
            while j<self.n-i+2: # First inner loop to print spaces before the characters in each line, starting from n-i+2
                print(' ',end='')
                j+=1
            while k<=i: # Second inner loop to print characters in the shape of an isosceles triangle
                if k==1 or k==i:
                    print(chr(64+i),end=' ') # Printing the character 'A+i' at the beginning and end of each line
                else:
                    print(" ",end=' ') # Printing a space for the inner characters
                k+=1
            i+=1 # Incrementing i for the next line
            print() # Moving to the next line after completing the inner loops
    def inverted_v_shaped_alpha_pat_85(self):
        i=1 #Initialising i to 1
        while i<=self.n: # Loop to iterate through rows
            j,k=0,1 #Initializing j,k values to 0,1
            while j<=self.n-i:  # Loop to add leading spaces for formatting
                print(' ',end='')
                j+=1 #Incrementing j to 1
            while k<=i: # Loop to print characters for the current row
                if k==1 or k==i:
                    print(chr(65+self.n-i),end=' ')  # Print the uppercase letter based on the pattern
                else:
                    print(" ",end=' ')
                k+=1 #Incrementing k to 1
            i+=1 #Incrementing i to 1
            print() # Move to the next line after completing the row
    def v_shaped_pat_86(self):
        i= self.n# initializing i value with n
        while i>=0: # loop for n number of rows
            j=k=0 # initializing j and k value with 0
            while j<self.n-i:  # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i: # loop for i number of columns
                if k==0 or k==i:  #Checking whether the value of k is equal to 0 or i.
                    print("*",end=' ') # printing i value if the k value is either 1 or i
                else: # else block will execute if k value is neither 0 nor i
                    print(" ",end=' ') # printing spaces
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def v_shaped_num_pat_87(self):
        i=self.n # initializing i value with n
        while i>0: # loop for n number of rows
            j=k=0 # initializing j and k value with 0
            while j<self.n-i:  # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i: # loop for i number of columns
                if k==1 or k==i:  #Checking whether the value of k is equal to 0 or i.
                    print(self.n-i+1,end=' ') # printing n-i+1 value if the k value is either 1 or i
                else: # else block will execute if k value is neither 0 nor i
                    print(" ",end=' ') # printing spaces
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def v_shaped_num_pat_88(self):
        i=self.n # Initializing the variable for the outer loop
        while i>0: # Outer loop to iterate through each line in reverse order
            j,k=0,1 # Initializing variables for the first and second inner loops
            while j<self.n-i:  # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end='')
                j+=1
            while k<=i: # Second inner loop to print numbers in the shape of an isosceles triangle
                if k==1 or k==i:
                    print(i,end=' ') # Printing the number 'i' at the beginning and end of each line
                else:
                    print(" ",end=' ') # Printing a space for the inner numbers
                k+=1
            i-=1  # Decrementing i for the next line
            print() # Moving to the next line after completing the inner loop
    def v_shaped_alpha_pat_89(self):
        i=self.n # initializing i value with n
        m=1
        while i>0: # loop for n number of rows
            j=k=0 # initializing j and k value with 0
            while j<self.n-i:  # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i: # loop for i number of columns
                if k==1 or k==i:  #Checking whether the value of k is equal to 0 or i.
                    print(chr(64+m),end=' ') # printing alphabets by adding 1 to the order of the alphabet
                else: # else block will execute if k value is neither 0 nor i
                    print(" ",end=' ') # printing spaces
                k+=1 # incrementing k value
            m+=1
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def v_shaped_alpha_pat_90(self):
        i=self.n # initializing i value with n
        while i>0: # loop for n number of rows
            j,k=0,1 # initializing j and k values with 0 and 1
            while j<self.n-i: # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i: # loop for i number of columns
                if k==1 or k==i: #Checking whether the value of k is equal to 1 or i.
                    print(chr(64+i),end=' ') # printing alphabetic pattern if the k value is either 1 or i
                else:  # else block will execute if k value is neither 1 nor i
                    print(" ",end=' ') # printing spaces
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def hallow_diamond_pat_91(self):
        i=0 # initializing i value with 0
        while i<self.n:  # loop for n number of rows
            j,k=0,0 # initializing j and k  values with 0
            while j<self.n-i:  # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:  # loop for i number of columns
                if k==0 or k==i:  #Checking whether the value of k is equal to 0 or i.
                    print("*",end=' ') # printing alphabetic pattern if the k value is either 0 or i
                else:   # else block will execute if k value is neither 0 nor i
                    print(" ",end=' ') # printing spaces
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print()  #an empty print() for next line

        while i>=0: # loop for n number of rows
            j,k=0,0 # initializing jand k value with 0
            while j<self.n-i:  # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:  # loop for i number of columns
                if k==0 or k==i: #Checking whether the value of k is equal to 0 or i.
                    print("*",end=' ') # printing alphabetic pattern if the k value is either 0 or i
                else:  # else block will execute if k value is neither 0 nor i
                    print(" ",end=' ') # printing spaces
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print()  #an empty print() for next line
    def hallow_diamond_num_pat_92(self):
        i=0 #Initializing i to 0
        while i<self.n:  #Loop for no.of rows
            j,k=0,1 # Initializing variables for the first and second inner loops
            while j<self.n-i: # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end='')
                j+=1
            while k<=i: # Second inner loop to print numbers in the shape of an isosceles triangle
                if k==1 or k==i:
                    print(i,end=' ') # Printing the number 'i' at the beginning and end of each line
                else:
                    print(" ",end=' ') # Printing a space for the inner numbers
                k+=1
            i+=1 # Incrementing i for the next line
            print() # Moving to the next line after completing the inner loops

        while i>0: #Loop for no.of rows
            j,k=0,1 # Initializing variables for the first and second inner loops
            while j<self.n-i: # First inner loop to print spaces before the numbers in each line, starting from n-i
                print(" ",end='')
                j+=1
            while k<=i: # Second inner loop to print numbers in the shape of an isosceles triangle
                if k==1 or k==i:
                    print(i,end=' ') # Printing the number 'i' at the beginning and end of each line
                else:
                    print(" ",end=' ') # Printing a space for the inner numbers
                k+=1
            i-=1 # Decrementing i for the next line
            print() # Moving to the next line after completing the inner loops
    def hallow_diamond_num_pat_93(self):
        # Upper part of the pyramid
        i=0
        while i<self.n:  #Loop to iterate through no.o lines
            j,k=0,1
            while j<self.n-i:  # Loop to add leading spaces for formatting
                print(' ',end='')
                j+=1
            while k<i+1: # Loop to print numbers for the current row
                if k==1 or k==i: # Print the number n+1-i at the first and last position in the row, otherwise print a space
                    print(self.n+1-i,end=' ')
                else:
                    print(' ',end=' ')
                k+=1
            print() # Move to the next line after completing the row
            i+=1
        # Lower part of the pyramid
        i=self.n
        while i>0: #Loop to iterate through no.o lines
            j,k=0,1
            while j < self.n-i:  # Loop to add leading spaces for formatting
                print(' ',end='')
                j+=1
            while k<i+1: # Loop to print numbers for the current row
                if k==1 or k==i:  # Print the number n+1-i at the first and last position in the row, otherwise print a space
                    print(self.n+1-i,end=" ")
                else:
                    print(' ',end=' ')
                k+=1
            print()
            i-=1
    def hallow_diamond_alpha_pat_94(self):
        i=0 # initializing i value with 0
        while i<self.n:  # loop for n number of rows
            j,k=0,1 # initializing j and k  values with 0 and 1
            while j<self.n-i:  # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:  # loop for i number of columns
                if k==1 or k==i:  #Checking whether the value of k is equal to 1 or i.
                    print(chr(64+i),end=' ') # printing alphabetic pattern if the k value is either 1 or i
                else:   # else block will execute if k value is neither 1 nor i
                    print(" ",end=' ') # printing spaces
                k+=1 # incrementing k value
            i+=1 # incrementing i value
            print()  #an empty print() for next line

        while i>0: # loop for n number of rows
            j,k=0,1 # initializing jand k value with 0 and 1
            while j<self.n-i:  # loop for n-i number of spaces in each row
                print(" ",end='') # printing n-i spaces
                j+=1 # incrementing j value
            while k<=i:  # loop for i number of columns
                if k==1 or k==i: #Checking whether the value of k is equal to 1 or i.
                    print(chr(64+i),end=' ') # printing alphabetic pattern if the k value is either 1 or i
                else:  # else block will execute if k value is neither 1 nor i
                    print(" ",end=' ') # printing spaces
                k+=1 # incrementing k value
            i-=1 # decrementing i value
            print()  #an empty print() for next line
    def hallow_diamond_alpha_pat_95(self):
        # Upper part of the pyramid
        i=0
        while i<self.n:  #Loop to iterate through no.o lines
            j,k=0,1
            while j<self.n-i:  # Loop to add leading spaces for formatting
                print(' ',end='')
                j+=1
            while k<i+1: # Loop to print numbers for the current row
                if k==1 or k==i: # Print the alphabet chr(65+n+1-i) at the first and last position in the row, otherwise print a space
                    print(chr(65+self.n-i),end=' ')
                else:
                    print(' ',end=' ')
                k+=1
            print() # Move to the next line after completing the row
            i+=1
        # Lower part of the pyramid
        i=self.n
        while i>0: #Loop to iterate through no.o lines
            j,k=0,1
            while j < self.n-i:  # Loop to add leading spaces for formatting
                print(' ',end='')
                j+=1
            while k<i+1: # Loop to print numbers for the current row
                if k==1 or k==i:  # Print the alphabet chr(65+n+1-i) at the first and last position in the row, otherwise print a space
                    print(chr(65+self.n-i),end=" ")
                else:
                    print(' ',end=' ')
                k+=1
            print() # Move to the next line after completing the row
            i-=1
    def half_diamond_with_increasing_space_96(self):
        i=self.n# Initializing i for the outer loop
        while i>-1: # Outer loop to print the pattern in descending order
            j=k=m=0 # Initializing variables for the first, second, and third inner loops
            while j<i: # First inner loop to print left-aligned asterisks
                print("*",end='')
                j+=1
            while k<=self.n-i-1: # Second inner loop to print spaces, aligning to the right
                print(' ',end=' ')
                k+=1
            while m<i: # Third inner loop to print right-aligned asterisks
                print("*",end='')
                m+=1
            i-=1 # Decrementing i for the next line
            print() # Moving to the next line after completing the inner loops
    def decreasing_space_diamond_pattern_97(self):
        i=0  # initializing i value with 0
        while i<self.n:  # loop for n number of rows
            j=k=m=0  # initializing j and k value with 0
            while j<=i:  # loop for i number of columns
                print("*",end='') # printing i number of *'s seperated by space
                j+=1 # incrementing j value
            while k<self.n-i-1:  # loop for n-i-1 number of spaces in each row
                print(" ",end=' ') # printing n-i-1 spaces
                k+=1  # incrementing k value
            while m<=i:  # loop for i number of columns
                print("*",end='') # printing i number of *'s seperated by space
                m+=1  # incrementing m value
            i+=1  # incrementing i value
            print() #an empty print() for next line
    def mirrored_diamond_98(self):
        i=0  # initializing i value with 0
        while i<self.n:  # loop for n number of rows
            j=k=m=0  # initializing j and k value with 0
            while j<=i:  # loop for i number of columns
                print("*",end='') # printing i number of *'s seperated by space
                j+=1 # incrementing j value
            while k<self.n-i-1:  # loop for n-i-1 number of spaces in each row
                print(" ",end=' ') # printing n-i-1 spaces
                k+=1  # incrementing k value
            while m<=i:  # loop for i number of columns
                print("*",end='') # printing i number of *'s seperated by space
                m+=1  # incrementing m value
            i+=1  # incrementing i value
            print() #an empty print() for next line

        i=self.n-1  # initializing i value with n-1
        while i>0:  # loop for n-1 number of rows
            j=k=m=0
            while j<i:  # loop for i number of columns
                print("*",end='') # printing i number of *'s seperated by space
                j+=1  # incrementing j value
            while k<=self.n-i-1:  # loop for n-i-1 number of spaces in each row
                print(' ',end=' ') # printing n-i-1 spaces
                k+=1  # incrementing k value
            while m<i:  # loop for i number of columns
                print("*",end='') # printing i number of *'s seperated by space
                m+=1 # incrementing m value
            i-=1 # decrementing i value
            print() #an empty print() for next line
    def symmetrical_triangular_pat_99(self):
        if self.n%2==0: #checking whether the number is even or odd
            self.n=self.n-1 # If the number is odd decrement it by 1
            
        i=1 # initializing i and x with 0
        while i<self.n//2+2: # loop for n/2+2 rows
            j=m=0 # initializing j and m with 0
            k=l=1 # initializing k and l with 1
            while j<self.n-i-self.n//2:  # loop for n-i-n/2 spaces in each row
                print(" ",end=' ') # printing spaces
                j+=1 # incrementing j value
            while k<i*2: # loop for i*2 columns
                print("*",end=' ') # printing *'s pattern seperated by space
                k+=1 # incrementing k value
            while m<2*(self.n-i-self.n//2):  # loop for 2*(n-i-n//2) spaces in each row
                print(" ",end=' ') # printing spaces
                m+=1 # incrementing m value
            while l<i*2: # loop for i*2+1 columns
                print("*",end=' ') # printing *'s pattern seperated by space
                l+=1 # incrementing l value

            i+=1 # incrementing i value
            print() #an empty print() for next line
    def symmetrical_triangular_pat_100(self):
        i=1 # Initializing i for the outer loop
        while i<self.n+1: # Outer loop to print the pattern in ascending order
            j,k=0,1 # Initializing variables for the first and second inner loops
            while j<self.n-i:  # First inner loop to print spaces, aligning to the left
                print(" ",end="")
                j+=1
            while k<i+1: # Second inner loop to print left-aligned asterisks
                print("*",end=" ")
                k+=1
            j,k=0,1 # Resetting variables for the third and fourth inner loops
            while j<self.n-i: # Third inner loop to print spaces, aligning to the left
                print(" ",end=" ")
                j+=1
            while k<i+1: # Fourth inner loop to print right-aligned asterisks
                print("*",end=" ")
                k+=1
            print()  # Moving to the next line after completing the inner loops
            i+=1 # Incrementing i for the next line


    