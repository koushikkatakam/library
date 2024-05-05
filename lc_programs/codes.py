from collections import Counter
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
  def lc_1(self,nums,target):
      """
      Finds two numbers in the given list that sum up to the target value.

      Parameters:
          nums (list of int): List of integers.
          target (int): Target sum value.

      Returns:
          list of int: Indices of the two numbers that sum up to the target value.

      Example:
          Input: nums = [2,7,11,15], target = 9
          Output: [0,1]
      """

      for i in range(len(nums)):    # Loop through each index in the nums list
          for j in range(i,len(nums)):   # Loop through each index from i to the end of the nums list
              if nums[i]+nums[j]==target:    # Check if the sum of nums[i] and nums[j] equals the target
                  return list[i,j]    # If found, return the indices i and j as a list

  def lc_9(self, x): # define a method named isPalindrome which takes an integer x as an input
        """
        Checks if a given integer is a palindrome.

        Palindrome: A palindrome is a word, number, phrase, or other sequence of characters that reads the same forward and backward.

        Parameters:
            x (int): The integer to be checked for palindrome property.

        Returns:
            bool: True if the integer is a palindrome, False otherwise.

        Example:
            Input: x = 121
            Output: True
        """

        s=str(x)  #convert the integer to a string
        k=s[::-1] #reverse the string
        if s==k: #check if the original string is equal to its reverse
            return True #return true if it is a palindrome
        else:
            return False #return False otherwise

  def lc_13(self, s):
        """
        Converts a Roman numeral string to an integer.

        Parameters:
            s (str): The Roman numeral string to be converted.

        Returns:
            int: The integer equivalent of the Roman numeral string.

        Example:
            Input: s = "MCMXCIV"
            Output: 1994
        """

        # Dictionary for Roman numerals to their integer values
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        summ=0   # Initialize the sum to 0
        for i in range(len(s)-1,-1,-1):   # Loop through the string from right to left
            num=dic[s[i]]   # Get the integer value of the current Roman numeral
            if 3*num<summ:   # If the value of the numeral is less than 3 times the sum, subtract it from the sum
                summ=summ-num
            else:
                summ+=num   # Otherwise, add it to the sum
        return summ # Return the final sum

  def lc_14(self, strs):
        """
        Find the longest common prefix among a list of strings.

        Parameters:
            strs (List[str]): The list of input strings.

        Returns:
            str: The longest common prefix among the strings.

        Example:
            Input: strs = ["flower","flow","flight"]
            Output: 'fl'
        """
        if len(strs)==0: # If the list of strings is empty
            return "" # Return an empty string
        base=strs[0] # Consider the first string as the base for comparison
        for i in range(len(base)): # Iterate over the characters of the first string
            for word in strs[1:]: # Iterate over the rest of the strings in the list
                if i==len(word) or word[i]!=base[i]: # If the index is out of bounds for any string or the characters don't match
                    return base[0:i] # Return the prefix up to the current index
        return base # Return the base string if all strings have the same prefix

  def lc_20(self, s):
        """
        Checks if the input string contains a valid combination of parentheses.

        This function takes a string `s` containing only parentheses ('(', ')', '[', ']', '{', '}') and returns True if the parentheses are properly closed and nested, and False otherwise.

        Parameters:
            s (str): The input string containing parentheses.

        Returns:
            bool: True if the parentheses in the input string are properly closed and nested, False otherwise.

        Example:
            Input: s = "()[]{}"
            Output: True
        """

        l=[] #Initialize a list to store opening parenthesis
        d={')':'(',']':'[','}':'{'} # define a dictionary to map closing parenthesis to their corresponding opening parenthesis
        for i in s: #Iterate over each character in the input string
            if i in d:# If the character is a closing parenthesis
                if l and l[-1]==d[i]:# If the list is not empty and the top of the list contains the corresponding opening parenthesis
                    l.pop() # Pop the opening parenthesis from the list
                else:
                    return False # Return False if the parentheses are not properly matched
            else:
                 l.append(i)# If the character is an opening parenthesis, append it onto the list
        return True if not l else False # Return True if the list is empty (all parentheses are properly matched), otherwise return False

  def lc_26(self, nums):
        """
        Remove duplicates from the sorted array nums in-place and return the number of unique elements.

        Parameters:
            nums (List[int]): The input array of integers.

        Returns:
            int: The number of unique elements.

        Example:
            Input: nums = [1,1,2]
            Output: 2
        """
        j=1 # Initialize a pointer j to keep track of the position to replace next unique element
        for i in range(1,len(nums)): # Iterate over the array starting from index 1
            if nums[i]!=nums[i-1]:  # If the current element is different from the previous one
                nums[j]=nums[i] # Replace the element at index j with the current element
                j+=1 # Move j to the next position
        return j # Return the number of unique elements

  def lc_27(self, nums, val):
        """
        Remove all occurrences of a specified value from the given list nums in-place.

        Parameters:
            nums (List[int]): The input list of integers.
            val (int): The value to be removed from the list.

        Returns:
            int: The number of elements remaining in the list after removing all occurrences of val.

        Example:
           Input: nums = [3,2,2,3], val = 3
            Output: 2
        """
        j=0 # Initialize a pointer j to keep track of the position to replace next non-val element
        for i in nums: # Iterate over each element in nums
            if i==val: # If the current element is equal to val
                continue # Skip it
            else:
                nums[j]=i # Replace the element at index j with the current non-val element
                j+=1 # Move j to the next position
        return j # Return the number of elements remaining after removing all occurrences of val

  def lc_28(self, haystack, needle):
        """
        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Parameters:
            haystack (str): The input string to be searched.
            needle (str): The string to be found within haystack.

        Returns:
            int: The index of the first occurrence of needle in haystack, or -1 if needle is not found.

        Example:
            Input: haystack = "sadbutsad", needle = "sad"
            Output: 0
        """
        len1=len(needle) # Length of the needle string
        for i in range(len(haystack)): # Iterate over each index in haystack
            if haystack[i:i+len1]==needle: # Check if the substring of length len1 starting from index i equals needle
                return i # Return the index i if needle is found at this position
        else:
            return -1 # Return -1 if needle is not found in haystack

  def lc_34(self, nums, target):
        """
        Finds the starting and ending positions of a target value within a sorted list of integers.

        Parameters:
            nums (List[int]): A sorted list of integers.
            target (int): The target value to search for within the list.

        Returns:
            List[int]: A list containing the starting and ending positions of the target value
                       within the input list. If the target is not found, returns [-1, -1].
        Example:
            Input: nums = [5,7,7,8,8,10], target = 8
            Output: [3,4]
        """
        positions = []

        # Check if the target is not in the list, return [-1, -1]
        if target not in nums:
            return [-1, -1]
        else:
            # Iterate through the list to find the positions of the target value
            for i in range(len(nums)):
                if nums[i] == target:
                    positions.append(i)

            # Return the starting and ending positions of the target value
            return [positions[0], positions[-1]]

  def lc_35(self, nums, target):
        """
        Return the index where the target is found, if the target is not found
        then it will return where the target should be inserted inserted in the sorted array nums.

        Parameters:
            nums (List[int]): The sorted array of integers.
            target (int): The target value to be inserted.

        Returns:
            int: The index where the target should be inserted.

        Example:
            Input: nums = [1,3,5,6], target = 5
            Output: 2
        """
        for i in range(len(nums)): # Iterate over each element in nums
            if nums[i]==target:  # If the current element equals the target
                return i # Return the index where the target is found
        else: # If target is not found in nums, find the index where target should be inserted
            index=0 # Initialize index to store the index where target should be inserted
            for i in range(len(nums)): # Iterate over each element in nums
                if nums[i]<target: # If the current element is less than target
                    index+=1 # Increment index to move to the next position
            return index # Return the index where target should be inserted

  def lc_53(self, nums):
        """
        Finds the contiguous subarray with the largest sum.

        This function takes a list of integers `nums` and finds the contiguous subarray (containing at least one element)
        which has the largest sum and returns the sum of that subarray.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            int: The sum of the contiguous subarray with the largest sum.

        Example:
            Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
            Output: 6
        """
        maxi=0 # Initialize the current maximum subarray sum to 0
        overal_max=-100000 # Initialize the overall maximum subarray sum to a very small value
        for i in nums: # Iterate through each element in nums
            maxi=max(maxi+i,i) # Calculate the maximum subarray sum ending at the current element
            overal_max=max(overal_max,maxi) # Update the overall maximum subarray sum
        return overal_max # Return the overall maximum subarray sum

  def lc_58(self, s):
        """
        Calculates the length of the last word in a given string s.

        Parameters:
            s (str): The input string.

        Returns:
            int: The length of the last word.

        Example :
            Input: s = "   fly me   to   the moon  "
            Output: 4
        """
        words=s.split() # Split the string into words using whitespace as delimiter and store them in a list
        return len(words[-1]) # Return the length of the last word in the list of words

  def lc_66(self, digits):
        """
        Adds one to a non-negative integer represented as a list of digits.

        Parameters:
            digits (List[int]): A list of non-negative integers representing the digits of a number.

        Returns:
            List[int]: A list of integers representing the digits of the resulting number after adding one.

        Example:
            Input: digits = [1,6,7]
            Output: [1,6,8]
        """

        digit=0  # Initialize digit=0 to store the converted number
        for i in digits:
            digit=digit*10+i # Convert the list of digits into a single number

        num=digit+1 # Add 1 to the converted number
        res=[] # Initialize an empty list to store the digits of the resulting number

        # Extract each digit from the number and insert it at the beginning of the list
        while num!=0:
            d=num%10
            res.insert(0,d)
            num//=10

        return res # Return the list of digits

  def lc_67(self, a, b):
        """
        Adds two binary strings and returns the result as a binary string.

        Parameters:
            a (str): A binary string representing the first number.
            b (str): A binary string representing the second number.

        Returns:
            str: A binary string representing the sum of the two input binary strings.

        Example:
            Input: a = "11", b = "1"
            Output: "100"
        """
        # Convert binary strings to integers and add them
        x = int(a, 2)
        y = int(b, 2)
        z = x + y

        # Convert the sum back to a binary string
        c = bin(z)

        # Remove the '0b' prefix from the binary string representation
        return c.replace("0b", "")

  def lc_69(self, x):
        """
        Computes the integer square root of a non-negative integer.

        Parameters:
            x (int): A non-negative integer.

        Returns:
            int: The integer square root of the input integer.

        Example:
            Input: x = 4
            Output: 2
        """
        # Using the sqrt function from the math module to compute the square root,
        # then converting the result to an integer
        return int(math.sqrt(x))

  def lc_70(self, n):
        """
        Calculates the number of distinct ways to climb to the top of the staircase.

        Parameters:
            n (int): The number of steps in the staircase.

        Returns:
            int: The number of distinct ways to reach the top of the staircase.

        Example:
            Input: n = 6
            Output: 13
        """

        if n==1: #if there is only one step, there is only one way to climb it
            return 1
        elif n==2: #if there are two steps, there are only two way to climb it(1 step at a time or two steps at once)
            return 2
        dp=[0]*(n+1) #initialize a dynamic programming list to store the no.of ways to climb each step.
        dp[1]=1 #there is one way to climb the each step
        dp[2]=2 #there are two ways to climb the second step.
        for i in range(3,n+1): #Iterate from 3rd step to the top
            dp[i]=dp[i-1]+dp[i-2] #The no.of ways to climb the current step is the sum of the ways to climb the previous two steps.
        return dp[n] #return the no.of ways to climb to the top of the staircase

  def lc_74(self, matrix, target):
        """
        Searches for a target value within a 2D matrix and returns True if found, otherwise False.

        Parameters:
            matrix (List[List[int]]): A 2D matrix of integers where each row is sorted in ascending order.
            target (int): The target value to search for within the matrix.

        Returns:
            bool: True if the target value is found in the matrix, False otherwise.

        Example:
            Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
            Output: true
        """
        # Iterate through each row of the matrix
        for row in matrix:
            # Check if the target is present in the current row
            if target in row:
                return True
        # If the target is not found in any row, return False
        return False

  def lc_88(self, nums1, m, nums2, n):
        """
        Merges two sorted arrays into the first array.

        This function takes two sorted arrays `nums1` and `nums2`, each with lengths `m` and `n` respectively,
        and merges them into `nums1`. It assumes that `nums1` has enough space (size that is greater or equal to m + n)
        to accommodate additional elements from `nums2`.

        Parameters:
            nums1 (List[int]): The first sorted array containing integers.
            m (int): The number of elements in `nums1` (excluding additional allocated space).
            nums2 (List[int]): The second sorted array containing integers.
            n (int): The number of elements in `nums2`.

        Returns:
            List[int]: The merged sorted array `nums1`.

        Example:
            Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
            Output: [1, 2, 2, 3, 5, 6]
        """

        merged=sorted(nums1[:m]+nums2[:n]) #merge two arrays and sort them
        nums1[:m+n]=merged #copy the merged array into nums1
        return nums1 #return the merged array

  def lc_121(self, prices):
        """
        Calculates the maximum profit from buying and selling a stock given its prices.

        Parameters:
            prices (List[int]): A list of integers representing the prices of the stock on each day.

        Returns:
            int: The maximum profit that can be achieved.

        Example:
            Input: prices = [7,1,5,3,6,4]
            Output: 7
        """

        ans=0   # Initialize a variable to store the maximum profit
        for i in range(1,len(prices)): # Iterate through the prices starting from the second day
            if prices[i]>prices[i-1] :
                # If the price on the current day is greater than the price on the previous day, add the difference to the maximum profit
                ans+=prices[i]-prices[i-1]
        return ans # Return the maximum profit

  def lc_136(self, nums):
        """
        Finds the single number in a list that appears only once while all other numbers appear twice.

        Parameters:
            nums (List[int]): A list of integers where each integer appears twice except for one.

        Returns:
            int: The single number that appears only once.

        Example:
            Input: nums = [1,2,3,2,1]
            Output: 3
        """

        res=nums[0] # Initialize the result variable with the first number in the list
        for i in range(1,len(nums)): # Iterate through the list starting from the second number
            res=res^nums[i]# XOR operation between the current result and the current number
        return res # Return the single number that appears only once

  def lc_169(self, nums):
        """
        Finds the majority element in a list of integers.

        Parameters:
            nums (List[int]): A list of integers.

        Returns:
            int: The majority element.

        Example:
            Input: nums = [2,2,1,1,1,2,2]
            Output: 2
        """

        count=0 # Initialize a counter variable to keep track of the majority element's count
        num=0 # Initialize a variable to store the majority element
        s=set(nums) # Convert the list of integers into a set to get unique elements
        for i in s:  # Iterate through the unique elements in the set
            # Check if the count of the current element is greater than half the length of the list
            # and if it's greater than the current maximum count
            if nums.count(i)>len(nums)//2  and nums.count(i)>count:
                # Update the majority element and its count
                num=i
                count = nums.count(i)
        return num # Return the majority element

  def lc_171(self, columnTitle):
        """
        Converts a column title as it appears in an Excel sheet to the corresponding column number.

        This function takes a string `columnTitle` representing the column title as it appears in an Excel sheet and returns the corresponding column number.

        Parameters:
            columnTitle (str): The column title as it appears in an Excel sheet.

        Returns:
            int: The corresponding column number.

        Example:
            Input: columnTitle = 'ZY'
            Output: 701
        """

        s=0 # Initialize a variable to store the column number
        for i in range(len(columnTitle)): # Iterate over each character in the columnTitle string
            s*=26 # Multiply the current column number by 26 (base 26 numbering system)
            s+=ord(columnTitle[i])-ord('A')+1 # Add the numerical value of the current character to the column number
        return s # Return the final column number

  def lc_191(self, n: int) -> int:
        """
        Calculates the Hamming weight of a given integer.

        The Hamming weight of an integer is the number of set (i.e., '1') bits
        in its binary representation.

        Parameters:
            n (int): The integer for which the Hamming weight needs to be calculated.

        Returns:
            int: The number of set bits (Hamming weight) in the binary representation of n.

        Example:
            Input: n = 11
            Output: 3
        """
        b = bin(n)  # Get the binary representation of n
        c = b.count('1')  # Count the number of set bits ('1') in the binary representation
        return c

  def lc_202(self, n):
        """
        Determines whether a given number is a happy number.

        A happy number is defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

        Parameters:
            n (int): The number to be checked for happiness.

        Returns:
            bool: True if the given number is happy, False otherwise.

        Example:
            Input: n = 19
            Output: True
        """
        num_value=n # Store the initial number value in num_value
        ls=[] # List to store visited numbers to check for cycles
        while num_value!=1 and num_value not in ls: # Loop until num_value equals 1 (happy number) or until num_value is encountered again in visited list (loop detected)
            ls.append(num_value) # Add current number to visited list
            square_num=0 # Initialize square_sum to store sum of squares of digits
            while num_value!=0: # Calculate the sum of squares of digits of num_value
                rem=num_value%10 # Extract the rightmost digit
                square_num=square_num+rem**2 # Add the square of the digit to square_sum
                num_value=num_value//10 # Move to the next digit
            num_value=square_num # Update num_value with the sum of squares for the next iteration
        # if num_value is equal to 1 return true elese return false
        if num_value==1:
            return True
        else:
            return False

  def lc_205(self, s, t: str):
        """
        Determines whether two strings are isomorphic.

        Two strings are considered isomorphic if characters in one string can be mapped to
        characters in another string such that all occurrences of each character in the
        first string correspond to the same character in the second string.

        Parameters:
            s (str): The first string.
            t (str): The second string.

        Returns:
            bool: True if the strings are isomorphic, False otherwise.

        Example:
            Input: s = "egg", t = "add"
            Output: true
        """
        x = set(s)
        y = set(t)
        if len(s) != len(t):
            return False
        elif len(x) == len(y) == len(set(zip(s,t))):
            return True
        else:
            return False

  def lc_217(self, nums):
        """
        Checks whether the given list contains any duplicates.

        This function takes a list of integers `nums` and returns True if there are any duplicate elements in the list, otherwise returns False.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            bool: True if the list contains any duplicates, False otherwise.

        Example:
            Input: nums = [1,2,3,1]
            Output: True
        """

        return len(set(nums))!=len(nums) # Return True if the length of the set of nums is not equal to the length of nums, indicating duplicates, otherwise return False

  def lc_242(self, s, t):
        """
        Checks if two strings are anagrams of each other.

        An anagram is a word or phrase formed by rearranging the letters of a different
        word or phrase, typically using all the original letters exactly once.

        Args:
            s (str): The first string.
            t (str): The second string.

        Returns:
            bool: True if the strings are anagrams, False otherwise.

        Example:
            Input: s = "anagram", t = "nagaram"
            Output: true
        """
        if sorted(s) == sorted(t):
            return True
        return False

  def lc_268(self, nums):
        """
        Finds the missing number in an array of consecutive integers from 0 to n.

        Parameters:
            nums (List[int]): A list of integers representing consecutive integers from 0 to n, with one missing number.

        Returns:
            int: The missing number.

        Example:
            Input: nums = [0,1,3]
            Output: 2
        """

        n=len(nums) # Calculate the length of the list
        #return (n*(n+1)//2)-sum(nums)
        for i in range(n+1): # Iterate through integers from 0 to n+1
            if i not in nums: # If the current integer is not in the list, it's the missing number
                return i # return the missing number

  def lc_283(self, nums):
        """
        Moves all zeroes in the given list nums to the end while maintaining the relative order of non-zero elements.

        Parameters:
            nums (List[int]): A list of integers.

        Returns:
            None: Modifies nums in-place.

        Example :
            Input: nums = [0,1,0,3,12]
            Output: [1,3,12,0,0]

        "Note : Do not return anything, modify nums in-place instead."
        """

        prev_index=0  # Initialize a variable to keep track of the index of the last non-zero element
        for i in range(len(nums)): # Iterate through each element in the list
            if nums[i]!=0: # If the current element is non-zero
                nums[i],nums[prev_index]=nums[prev_index],nums[i] # Swap the current non-zero element with the element at the previous non-zero index
                prev_index+=1 # Increment the previous non-zero index

  def lc_326(self, n):
        """
        Determines if a given integer is a power of three.

        A positive integer n is a power of three if there exists an integer i such that
        n == 3**i.

        Parameters:
            n (int): The integer to be checked.

        Returns:
            bool: True if n is a power of three, False otherwise.

        Example:
            Input: n = 27
            Output: true
        """
        for i in range(0, 100):
            if n == 3**i:
                return True
        return False

  def lc_338(self, n):
        """
        Counts the number of bits set to 1 in the binary representation of each number
        from 0 to n (inclusive).

        Parameters:
            n (int): The non-negative integer upper bound.

        Returns:
            List[int]: A list containing the count of bits set to 1 for each number
                       from 0 to n.

        Example:
            Input: n = 2
            Output: [0,1,1]
        """
        x = []
        y = []
        for i in range(n + 1):
            x.append(bin(i))
        for i in x:
            y.append(i.count("1"))
        return y

  def lc_342(self, n: int) -> bool:
        """
        Checks if a given integer is a power of four.

        A positive integer is a power of four if it can be expressed as 4^k for some integer k.

        Parameters:
            n (int): The integer to be checked.

        Returns:
            bool: True if n is a power of four, False otherwise.

        Example:
            Input: n = 16
            Output: true
        """
        for i in range(0, 32):
            if 4 ** i == n:
                return True
        return False

  def lc_344(self, s):
        """
        Reverses a list of characters in-place.

        Modifies the input list `s` by reversing its elements in-place.

        Parameters:
            s (List[str]): The list of characters to be reversed.

        Returns:
            None

        Example:
            Input: s = ["h","e","l","l","o"]
            Output: ["o","l","l","e","h"]
        """
        s[::] = s[::-1]

  def lc_345(self, s):
        """
        Reverses the vowels in a given string while keeping other characters unchanged.

        Parameters:
            s (str): The input string.

        Returns:
            str: The string with vowels reversed.

        Example:
            Input: s = "hello"
            Output: holle
        """
        vowels = 'AEIOUaeiou'
        v = ''  # Stores the vowels in the input string
        res = ''  # Stores the result string with reversed vowels
        k = -1  # Index for iterating through vowels in reverse order

        # Extract vowels from the input string
        for i in s:
            if i in vowels:
                v += i

        # Iterate through the input string
        for i in s:
            if i in vowels:
                # Append the vowels from 'v' in reverse order
                res += v[k]
                k -= 1
            else:
                # Append non-vowel characters as they are
                res += i

        return res

  def lc_371(self, a, b):
        """
        Returns the sum of two integers a and b.

        Parameters:
            a (int): The first integer.
            b (int): The second integer.

        Returns:
            int: The sum of a and b.

        Example:
            Input: a = 1, b = 2
            Output: 3
        """
        return a + b

  def lc_378(self, matrix, k):
        """
        Finds the kth smallest element in a sorted matrix.

        Flattens the matrix into a single list, sorts it, and returns the kth smallest
        element.

        Parameters:
            matrix (List[List[int]]): The sorted matrix.
            k (int): The index of the desired smallest element (1-indexed).

        Returns:
            int: The kth smallest element in the matrix.

        Example:
            Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
            Output: 13
        """
        s = []
        for row in matrix:
            for element in row:
                s.append(element)
        x = sorted(s)
        return x[k - 1]

  def lc_383(self, ransomNote, magazine):
        """
        Determines whether it is possible to construct the ransom note from the magazine.

        This function takes two strings, `ransomNote` and `magazine`, and checks whether it is possible to construct the `ransomNote` from characters in the `magazine`. Each letter in the `magazine` can only be used once.

        Parameters:
            ransomNote (str): The string representing the ransom note.
            magazine (str): The string representing the magazine.

        Returns:
            bool: True if the ransom note can be constructed from the magazine, False otherwise.

        Example:
            Input: ransomNote = "aa", magazine = "aab"
            Output: True
        """

        for i in ransomNote: # Iterate over each character in the ransomNote string
            count=ransomNote.count(i) # Count the occurrences of the current character in the ransomNote
            count1=magazine.count(i) # Count the occurrences of the current character in the magazine
            if i not in magazine or count>count1: # If the current character is not in the magazine or its count in the ransomNote is greater than its count in the magazine
                return False
        return True # If all characters in the ransomNote can be found in the magazine with sufficient counts, return True

  def lc_387(self, s):
        """
        Finds the index of the first unique character in a string.

        Creates a dictionary to count the occurrences of each character in the string.
        Then iterates through the dictionary to find the first character with a count
        of 1 and returns its index in the original string. If no such character is found,
        returns -1.

        Parameters:
            s (str): The input string.

        Returns:
            int: The index of the first unique character, or -1 if no such character exists.

        Example:
            Input: s = "leetcode"
            Output: 0
        """
        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

        for char, count in char_count.items():
            if count == 1:
                return s.index(char)

        return -1

  def lc_389(self, s, t):
        """
        Finds the character that is added to string t compared to string s.

        Creates dictionaries to count the occurrences of each character in strings s and t.
        Then iterates through the dictionary of characters in t to find the character that
        is not present in the dictionary of characters in s or has a different count.

        Parameters:
            s (str): The original string.
            t (str): The modified string with an added character.

        Returns:
            str: The character that is added to string t.

        Example:
            Input: s = "abcd", t = "abcde"
            Output: "e"
        """
        char_count_t = {}
        char_count_s = {}

        for char in t:
            if char not in char_count_t:
                char_count_t[char] = 1
            else:
                char_count_t[char] += 1

        for char in s:
            if char not in char_count_s:
                char_count_s[char] = 1
            else:
                char_count_s[char] += 1

        for char, count in char_count_t.items():
            if char not in char_count_s:
                return char
            if char in char_count_s and count != char_count_s[char]:
                return char

  def lc_392(self, s, t):
        """
        Checks if string s is a subsequence of string t.

        Iterates through both strings simultaneously, moving to the next character
        in string s only when a match is found in string t. Returns True if the end
        of string s is reached during the iteration, indicating that it is a subsequence
        of string t, otherwise returns False.

        Parameters:
            s (str): The potential subsequence string.
            t (str): The string to check against.

        Returns:
            bool: True if s is a subsequence of t, False otherwise.

        Example 1:
            Input: s = "abc", t = "ahbgdc"
            Output: true
        """
        a = 0
        b = 0
        while a < len(s) and b < len(t):
            if s[a] == t[b]:
                a += 1
            b += 1
        if a == len(s):
            return True
        else:
            return False

  def lc_409(self, s):
        """
        Finds the length of the longest palindrome that can be formed from the given string.

        Counts the occurrence of each character in the string and calculates the maximum
        length of a palindrome that can be formed from these characters. Adds 1 to the length
        if there is at least one character with an odd count, as it can be placed in the
        center of the palindrome.

        Parameters:
            s (str): The input string.

        Returns:
            int: The length of the longest palindrome that can be formed from the string.

        Example 1:
            Input: s = "abccccdd"
            Output: 7
        """
        if len(s) == 1:
            return 1

        total_length = len(s)
        odd_count = 0

        for char in set(s):
            if s.count(char) % 2 != 0:
                odd_count += 1

        max_length = abs(total_length - odd_count)

        if odd_count >= 1:
            max_length += 1

        return max_length

  def lc_412(self, n):
        """
        Generates a list of strings representing the numbers from 1 to n with certain
        replacements:

        - For multiples of three, the string "Fizz" is added instead of the number.
        - For multiples of five, the string "Buzz" is added instead of the number.
        - For multiples of both three and five, the string "FizzBuzz" is added instead of the number.

        Parameters:
            n (int): The upper limit of the numbers to consider.

        Returns:
            List[str]: A list of strings representing the numbers from 1 to n with the specified replacements.

        Example:
            Input: n = 15
            Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
        """
        numbers = []
        replacements = []
        i = 1

        while i <= n:
            numbers.append(i)
            i += 1

        for number in numbers:
            if number % 3 == 0 and number % 5 == 0:
                replacements.append("FizzBuzz")
            elif number % 3 == 0:
                replacements.append("Fizz")
            elif number % 5 == 0:
                replacements.append("Buzz")
            else:
                replacements.append(str(number))

        return replacements

  def lc_448(self, nums):
        """
        Finds the disappeared numbers in a list of integers.

        Given a list of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear
        twice and others appear once. Find all the elements of [1, n] inclusive that do not
        appear in this list.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            List[int]: A list of integers representing the numbers that are missing from the list.

        Example:
            Input: nums = [4,3,2,7,8,2,3,1]
            Output: [5,6]
        """
        possible_numbers = list(range(1, len(nums) + 1))
        return list(set(possible_numbers) - set(nums))

  def lc_485(self, nums):
        """
        Finds the maximum number of consecutive 1s in a list of binary integers.

        Iterates through the list of binary integers and counts the consecutive
        occurrences of 1s. Stores the counts in a list and returns the maximum count.

        Parameters:
            nums (List[int]): The list of binary integers.

        Returns:
            int: The maximum number of consecutive 1s in the list.

        Example:
            Input: nums = [1,1,0,1,1,1]
            Output: 3
        """
        count = 0
        counts_list = []
        for num in nums:
            if num == 1:
                count += 1
            else:
                counts_list.append(count)
                count = 0
        counts_list.append(count)

        return max(counts_list)

  def lc_509(self, n):
        """
        Calculates the nth Fibonacci number.

        Parameters:
            n (int): The index of the Fibonacci number to calculate.

        Returns:
            int: The nth Fibonacci number.

        Example:
            Input: n = 2
            Output: 1
        """

        ls=[0,1] # Initialize a list to store Fibonacci numbers with initial values 0 and 1.
        for i in range(n): # Iterate n times.
            ls.append(ls[i]+ls[i+1]) # Append the sum of the last two elements to the list.
        return ls[n] # Return the nth Fibonacci number.

  def lc_520(self, word):
        """
        Determines if a word's use of capitalization is correct.

        Checks if the word satisfies one of the following conditions:
        1. All letters in the word are capitalized.
        2. All letters in the word are lowercase.
        3. Only the first letter in the word is capitalized.

        Parameters:
            word (str): The word to be checked.

        Returns:
            bool: True if the word's capitalization is correct, False otherwise.

        Example 1:
            Input: word = "USA"
            Output: true
        """
        uppercase_word = word.upper()
        if word == uppercase_word or word == word.lower() or word == word.capitalize():
            return True
        else:
            return False

  def lc_540(self, nums):
        """
        Finds the single element that appears only once in a sorted array of integers.

        Uses the property that all elements before the single non-duplicate are in pairs
        (i.e., nums[i] == nums[i+1]). Iteratively checks pairs to find the single non-duplicate.

        Parameters:
            nums (List[int]): The sorted list of integers.

        Returns:
            int: The single element that appears only once.

        Example:
            Input: nums = [1,1,2,3,3,4,4,8,8]
            Output: 2
        """
        unique_sum = sum(set(nums))
        total_sum = sum(nums)

        return abs(total_sum - unique_sum - unique_sum)

  def lc_557(self, s):
        """
        Reverses the order of characters in each word of a string.

        Parameters:
            s (str): Input string.

        Returns:
            str: A new string where each word in the input string has its characters reversed while maintaining the word order.

        Example:
            Input: s = "Let's take LeetCode contest"
            Output: "s'teL ekat edoCteeL tsetnoc"
        """

        s=s.split() # Split the input string into words.
        new_s="" # Initialize an empty string 'new_s' to store the reversed words.
        for i in s: # Iterate through each word in the list of words.
            new_s+=i[::-1]+' ' # Reverse the characters of the current word and append it to 'new_s' with a space.
        return new_s.strip()  # Return 'new_s' with leading and trailing spaces removed.

  def lc_657(self, moves):
        """
        Determines whether the robot returns to the original position after a sequence of moves.

        This function takes a string `moves` representing a sequence of moves made by a robot on a 2D plane. Each move is represented by a character: 'U' for moving up, 'D' for moving down, 'L' for moving left, and 'R' for moving right. The function returns True if the robot returns to the original position after the sequence of moves, otherwise returns False.

        Parameters:
            moves (str): The sequence of moves made by the robot.

        Returns:
            bool: True if the robot returns to the original position after the sequence of moves, False otherwise.

        Example:
            Input: moves"UD"
            Output: True
        """
        # Count occurrences of each move
        count_U=moves.count('U') # Count the number of 'U' moves in the input string.
        count_D=moves.count('D') # Count the number of 'D' moves in the input string.
        count_R=moves.count('R') # Count the number of 'R' moves in the input string.
        count_L=moves.count('L') # Count the number of 'L' moves in the input string.
        # Check if counts of up/down and left/right movements are equal
        if count_D == count_U and count_R==count_L: # Check if counts of up/down and left/right movements are equal
            return True # If the counts are equal, return True, indicating the robot returns to the original position.
        return False # If the counts are not equal, return False, indicating the robot does not return to the original position.

  def lc_709(self, s):
        """
        Converts a string to lowercase.

        Parameters:
            s (str): Input string.

        Returns:
            str: String converted to lowercase.

        Example:
            Input: s ="Hello"
            Output: 'hello'
        """

        return s.lower() # Return the lowercase version of the input string.

  def lc_728(self, left, right):
        """
        Finds all self-dividing numbers in the range from left to right, inclusive.

        Parameters:
            left (int): The left endpoint of the range.
            right (int): The right endpoint of the range.

        Returns:
            List[int]: A list of self-dividing numbers found in the range.

        Example :
            Input: left = 1, right = 22
            Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        """

        nums=[] # Initialize an empty list to store the self-dividing numbers
        for num in range(left,right+1): # Iterate through each number in the range from left to right+1
            n=num # Make a copy of the current number
            while num!=0: # Iterate through each digit of the current number
                d=num%10 # Extract the last digit of the number

                # If the digit is 0 or the original number is not divisible by the digit, break the loop
                if d==0 or n%d!=0:
                    break
                num//=10 # Move to the next digit

            # If the loop completes without breaking, it means the number is self-dividing, so append it to the list
            else:
                nums.append(n)
        return nums # Return the list of self-dividing numbers

  def lc_724(self, nums):
        """
        Finds the index of the pivot element in an array, if it exists.

        Calculates the total sum of the array and iterates through each element,
        checking if the sum of elements to the left and right of the current element
        are equal. Returns the index of the pivot element if found, otherwise -1.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            int: The index of the pivot element, or -1 if no pivot exists.

        Example 1:
            Input: nums = [1,7,3,6,5,6]
            Output: 3
        """
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            total_sum -= nums[i]
            if left_sum == total_sum:
                return i
            else:
                left_sum += nums[i]

        return -1

  def lc_744(self, letters, target):
        """
        Finds the smallest letter in the list that is greater than a given target letter.

        Adds the target letter to the list of letters, creates a sorted set from the
        updated list, and finds the index of the target letter in the sorted set. If the
        target letter is not the last element in the sorted set, returns the next letter;
        otherwise, returns the first letter.

        Parameters:
            letters (List[str]): The list of letters.
            target (str): The target letter.

        Returns:
            str: The smallest letter greater than the target letter.

        Example:
            Input: letters = ["c","f","j"], target = "a"
            Output: "c"
        """
        letters.append(target)
        unique_letters = sorted(set(letters))

        index_of_target = unique_letters.index(target)

        if index_of_target < len(unique_letters) - 1:
            return unique_letters[index_of_target + 1]
        else:
            return unique_letters[0]

  def lc_760(self, A, B):
        """
        Finds the mapping of elements in list A to their positions in list B.

        Parameters:
            A (List[int]): The first list.
            B (List[int]): The second list.

        Returns:
            List[int]: A list containing the indices of elements in list B corresponding to elements in list A.

        Example :
            Input: A = [12,28,46,32,50], B = [50,12,32,46,28]
            Output: [1,4,3,2,0]
        """

        P=[] # Initialize an empty list to store the mapping indices
        for i in range(len(A)): # Iterate through each element in list A
            j=B.index(A[i]) # Find the index of the current element in list B
            P.append(j) # Append the index to the result list P
        return P # Return the list containing the mapping indices

  def lc_762(self, left, right):
        """
        Counts the number of integers with a prime number of set bits in their binary representation within the range [left, right].

        Parameters:
            left (int): The left endpoint of the range.
            right (int): The right endpoint of the range.

        Returns:
            int: The count of integers with a prime number of set bits.

        Example :
            Input: left = 6, right = 10
            Output: 4
        """
        count=0 # Initialize the count with 0
        for num in range(left,right+1): # Iterate through each number in the given range

            b=bin(num) # Get the binary representation of the number
            n=b[2:] # Remove '0b' prefix
            s=sum(list(map(int,n))) # count the number of '1's or sum of '1's
            # Check if the count of set bits is a prime number
            for i in range(2,s//2+1):
                # break the loop if the number is not ptime
                if s%i==0:
                    break
            else:
                # Increment the count value if the number is prime
                if s>1:
                    count+=1
        return count # Return the count of integers with prime set bits

  def lc_771(self, jewels, stones):
        """
        Counts the number of characters in 'stones' that are present in 'jewels'.

        Parameters:
            jewels (str): String representing types of jewels.
            stones (str): String representing stones.

        Returns:
            int: Number of characters in 'stones' that are also present in 'jewels'.

        Example:
            Input: jewels = "aA", stones = "aAAbbbb"
            Output: 3
        """

        count=0 # Initialize a counter for the number of characters.
        for i in stones: # Iterate through each character in the stones string.
            if i in jewels:  # Check if the character is present in the jewels string.
                count+=1 # Increment the count if the character is found in jewels.
        return count # Return the final count.

  def lc_804(self, words):
        """
        Calculates the number of unique Morse code representations for a list of words.

        This function takes a list of strings `words`, where each string consists of lowercase English letters, and calculates the number of unique Morse code representations corresponding to the words. Each letter is mapped to its Morse code representation, and the function counts the number of distinct combinations of Morse codes for the given words.

        Parameters:
            words (List[str]): A list of strings containing lowercase English letters.

        Returns:
            int: The number of unique Morse code representations.

        Example:
            Input: ["gin", "zen", "gig", "msg"]
            Output: 2
        """
        ls=[] # Initialize an empty list ls to store Morse code representations of words.
        d={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."} # Define a dictionary d mapping lowercase English letters to their Morse code representations.
        for w in words: # Iterate through each word in the list words.
            c="" # Initialize an empty string c to store the Morse code representation of the current word.
            for char in w: # Iterate through each character in the current word.
                c+=d[char] # Append the Morse code representation of the current character to the string c.
            ls.append(c) # Append the Morse code representation of the current word to the list ls.
        s=set(ls) # Convert the list ls to a set s to remove duplicate Morse code representations.
        return len(s) # Return the number of unique Morse code representations.

  def lc_832(self, image):
        """
        Flips and inverts a given binary image.

        Parameters:
            image (List[List[int]]): A binary image represented as a list of lists of integers.

        Returns:
            List[List[int]]: The flipped and inverted binary image.

        Example :
            Input: image = [[1,1,0],[1,0,1],[0,0,0]]
            Output: [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
        """

        flip_img=[] # Initialize an empty list to store the flipped and inverted image
        for lis in image: # Iterate through each list in the given image
            x=[] # Initialize an empty list to store the flipped and inverted row
            for i in lis[::-1]: # Iterate through each element in the row in reverse order
                if i==0: # If the element is 0, append 1 to the new row;
                    x.append(1)
                else: # otherwise, append 0
                    x.append(0)
            flip_img.append(x) # Append the new row to the flipped and inverted image

        return flip_img # Return the flipped and inverted image

  def lc_905(self, nums):
        """
        Sorts an array of integers such that even integers appear before odd integers.

        Parameters:
            nums (List[int]): An array of integers.

        Returns:
            List[int]: The sorted array with even integers appearing before odd integers.

        Example :
            Input: nums = [1,2,4,3]
            Output: [2,4,1,3]
        """

        # Initialize empty lists to store even and odd integers
        even=[]
        odd=[]
        for n in nums: # Iterate through each integer in the input array
            if n%2==0: # If the integer is even, append it to the even list;
                even.append(n)
            else: # otherwise, append it to the odd list
                odd.append(n)
        res=even+odd # Concatenate the even and odd lists to form the sorted array with even integers appearing before odd integers
        return res  # Return the resultant array

  def lc_961(self, nums):
        """
        Finds the integer that appears more than once in the list.

        This function takes a list of integers `nums`, where each integer represents an element. It identifies and returns the integer that appears more than once in the list.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            int: The integer that appears more than once in the list.

        Example:
            Input: nums[1, 2, 3, 3]
            Output: 3
        """

        for i in nums: # Iterate through each element in the list nums.
            if nums.count(i)>1: # Check if the count of the current element in nums is greater than 1, indicating it appears more than once.
                return i # If so, return the current element.

  def lc_977(self, nums):
        """
        Squares each element in the given list of integers, sorts the resulting squared numbers, and returns the sorted list.

        Parameters:
            nums (List[int]): A list of integers.

        Returns:
            List[int]: The sorted list of squared numbers.

        Example :
            Input: nums[-4,-1,0,3,10]
            Output: [0, 1, 9, 16, 100]
        """

        sqr_nums=list(map(lambda x:x**2,nums)) # Square each element in the input list using the map function and a lambda function
        sqr_nums.sort() # Sort the squared numbers in ascending order
        return sqr_nums # Return the sorted list of squared numbers

  def lc_1002(self, words):
        """
        Find common characters among a list of words.

        Parameters:
            words (list of str): A list of strings where common characters are to be found.

        Returns:
            list of str: A list containing common characters found in all words. If a character appears multiple times in all words,
            it will appear multiple times in the returned list.

        Example:
            Input: words = ["cool", "lock", "cook"]
            Output: ['c', 'o']
        """
        res = Counter(words[0]) # Create a Counter object for the first word in the list
        for i in words: # Iterate through each word in the list starting from the second word
            res &= Counter(i) # Intersect the Counter of the current word with the Counter of the result
        return list(res.elements()) # Return a list of elements from the resulting Counter (common characters)

  def lc_1025(self, n):
        """
        Determines whether Alice can win the divisor game for a given integer n.

        Parameters:
            n (int): The input integer.

        Returns:
            bool: True if Alice can win, False otherwise.

        Example :
            Input: n = 2
            Output: True
        """

        # Check if the input integer n is even (divisible by 2)
        # If n is even, Alice can choose 1 as a divisor, resulting in an odd number for Bob, and vice versa.
        # As long as Alice starts the game with an even number, she can always make Bob end up with an odd number,
        # ensuring she wins the game.
        return n%2==0

  def lc_1051(self, heights):
        """
        Calculates the number of students who need to change their positions to be in non-decreasing order of heights.

        Sorts the list of heights and compares it with the original list to count the number of students
        who need to change their positions to make the heights in non-decreasing order.

        Parameters:
            heights (List[int]): The list of heights of the students.

        Returns:
            int: The number of students who need to change their positions.
        Example 1:
            Input: heights = [1,1,4,2,1,3]
            Output: 3
        """
        sorted_heights = sorted(heights)
        num_changes = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                num_changes += 1
        return num_changes

  def lc_1085(self, A):
        """
        Given an array A of positive integers, this function calculates the sum of the digits of the minimal element of A.
        It returns 0 if the sum is odd, otherwise returns 1.

        Parameters:
            A (list): A list of positive integers.

        Returns:
            int: 0 if the sum of digits of the minimal element of A is odd, 1 otherwise.

        Example:
            Input: A = [34, 23, 1, 24, 75, 33, 54, 8]
            Output: 0
        """

        min_num=min(A) # Find the minimal element in the list A.
        sum_digits=sum(int(digits) for digits in str(min_num)) # Calculate the sum of digits of the minimal element.
        return 0 if sum_digits%2!=0 else 1 # Return 0 if the sum of digits is odd, otherwise return 1.

  def lc_1108(self, address):
        """
        Defangs an IP address by replacing "." with "[.]".

        Iterates through each character in the IP address string. If the character
        is a period ".", it is replaced with "[.]" and appended to a list. Otherwise,
        the character is appended to the list as is. Finally, the list is joined into
        a single string and returned.

        Parameters:
            address (str): The IP address to be defanged.

        Returns:
            str: The defanged IP address.

        Example 1:
            Input: address = "1.1.1.1"
            Output: "1[.]1[.]1[.]1"
        """
        defanged_address = []
        for char in address:
            if char == ".":
                char = "[.]"
            defanged_address.append(char)
        return "".join(defanged_address)

  def lc_1119(self, input):
      """
        Removes vowels from the given input string.

        Parameters:
            input (str): The input string from which vowels are to be removed.

        Returns:
            str: The input string with vowels removed.

        Example:
            Input: input = "leetcodeisacommunityforcoders"
            Output: 'ltcdscmmntyfrcdrs'
      """
      vowels="aeiou" # String containing vowels
      ans="" # Initialize an empty string to store the result
      # Iterate over each character in the input string
      for i in input:
        if i in vowels: # If the character is a vowel
          continue # Skip it
        else: # If the character is not a vowel
          ans+=i # Append it to the result string
      return ans # Return the result string

  def lc_1160(self, words, chars):
        """
        Counts the total length of words from a list words that can be formed using the characters from a string chars.

        Parameters:
            words (List[str]): The list of words.
            chars (str): The string of characters.

        Returns:
            int: The total length of words that can be formed using the characters from chars.

        Example :
            Input: words = ["cat","bt","hat","tree"], chars = "atach"
            Output: 6
        """
        ans=0 # Initialize a variable to store the total length of words that can be formed
        # Create a dictionary to store the count of each character in the chars string
        d={}
        for i in chars:
            d[i]=chars.count(i)
        for word in words: # Iterate through each word in the words list
            for ch in word: # Iterate through each character in the word
                # If the character is not present in chars or if its count in the word exceeds its count in chars, break out of the loop
                if ch not in chars or word.count(ch)>d[ch]:
                    break
            else:
                # If the loop completes without breaking, add the length of the word to the total length
                ans+=len(word)
        return ans # Return the total length of words that can be formed using the characters from chars

  def lc_1207(self, arr):
        """
        Checks if the number of occurrences of each value in the list is unique.

        Parameters:
            arr (List[int]): A list of integers.

        Returns:
            bool: True if the number of occurrences of each value is unique, False otherwise.

        Example:
            arr = [1, 2, 2, 1, 1, 3]
            Output: True
        """

        k=set(arr) # Create a set 'k' from the input list 'arr' to get unique values.
        ls=[arr.count(i) for i in k] # Count occurrences of each unique value in 'arr' and store them in a list 'ls'.
        # Loop through the list 'ls' to check for non-unique occurrences.
        for i in range(len(ls)-1):
            for j in range(len(ls)):
                if ls[i]==ls[j] and i!=j: # If the counts are equal and the indices are different, it means non-unique occurrences.
                    return False # Return False if non-unique occurrences are found.
        return True # If no non-unique occurrences are found, return True.

  def lc_1221(self, s):
        """
        Counts the number of balanced substrings in a given string.

        Iterates through each character in the string, incrementing a counter
        when encountering 'R' and decrementing it when encountering 'L'. When
        the counter reaches zero, it indicates the end of a balanced substring,
        so the total count of balanced substrings is incremented. Returns the
        total count of balanced substrings.

        Parameters:
            s (str): The input string consisting of characters 'R' and 'L'.

        Returns:
            int: The number of balanced substrings in the input string.

        Example:
            Input: s = "RLRRLLRLRL"
            Output: 4
        """
        count = 0
        balance = 0
        for char in s:
            if char == 'R':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count

  def lc_1232(self, coordinates):
        """
        Checks if the given set of coordinates lie on a straight line.

        This function takes a list of coordinate pairs `coordinates` and checks if all the points lie on the same straight line.

        Parameters:
            coordinates (List[List[int]]): A list of coordinate pairs where each pair represents the (x, y) coordinates of a point.

        Returns:
            bool: True if all the points lie on the same straight line, False otherwise.

        Example:
            coordinates = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
            Output: True
        """

        x0,y0=coordinates[0] # Get the x and y coordinates of the first point.
        x1,y1=coordinates[1] # Get the x and y coordinates of the second point.
        for x,y in coordinates[2:]: # Iterate through the remaining points in coordinates.
            if ((y1-y0)*(x-x0)) - ((y-y0)*(x1-x0)) !=0: # Check if the current point lies on the same straight line defined by the first two points.
                return False # If not, return False.
        return True # If all points lie on the same straight line, return True.

  def lc_1281(self, n):
        """
        Calculates the difference between the product of the digits and the sum of the digits of a given integer n.

        Parameters:
            n (int): The input integer.

        Returns:
            int: The difference between the product of the digits and the sum of the digits.

        Example :
            Input: n = 234
            Output - 15
        """

        # Initialize variables to store the sum of digits and the product of digits
        digit_sum=0
        product=1
        while n!=0: # Iterate through each digit of the integer
            d=n%10 # Extract the last digit of the integer
            # Update the sum of digits and the product of digits
            digit_sum+=d
            product*=d
            n//=10 # Remove the last digit from the integer
        return product-digit_sum # return the difference between the product of digits and the sum of digits

  def lc_1295(self, nums):
        """
        Finds the number of integers in a list that have an even number of digits.

        Iterates through the list of integers and checks if the length of their
        string representation is even. If it is, the integer is added to a list.
        Finally, returns the length of the list.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            int: The number of integers in the list that have an even number of digits.

        Example:
            Input: nums = [12,345,2,6,7896]
            Output: 2
        """
        even_digit_nums = []
        for num in nums:
            if len(str(num)) % 2 == 0:
                even_digit_nums.append(num)
        return len(even_digit_nums)

  def lc_1299(self, arr):
        """
        Replaces each element in the array with the greatest element to its right,
        and sets the last element to -1.

        Iterates through the array and for each element, replaces it with the maximum
        element in the subarray to its right. Finally, sets the last element of the array
        to -1.

        Parameters:
            arr (List[int]): The input array of integers.

        Returns:
            List[int]: The modified array after replacing elements.

        Example:
            Input: arr = [17,18,5,4,6,1]
            Output: [18,6,6,6,1,-1]
        """
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i + 1:])
        arr[-1] = -1
        return arr

  def lc_1304(self, n):
        """
        Generates an array of n unique integers such that their sum is zero.

        Parameters:
            n (int): The number of integers to generate.

        Returns:
            List[int]: The generated array.

        Example :
            Input: n = 5
            Output: [0,1,-1,3,-3]
        """
        if n==0: # If n is 0, return an array containing only 0
            return [0]
        res=[] # Initialize an empty list to store the generated integers
        if n%2!=0:
            res.append(0)

        for i in range(1,n,2): # Iterate from 1 to n with a step of 2
            res.extend([i,-i]) # Append i and -i to the result list
        return res # Return the generated array

  def lc_1313(self, nums):
        """
        Decompresses a run-length encoded list.

        Parameters:
            nums (List[int]): A run-length encoded list.

        Returns:
            List[int]: The decompressed list.

        Example :
            Input: nums[1,2,3,4]
            Output: [2, 4, 4, 4]
        """

        res=[] # Initialize an empty list to store the decompressed list
        for i in range(0,len(nums),2): # Iterate through the encoded list in steps of 2
            # Get the frequency (how many times the value appears) and the value itself
            freq=nums[i]
            val=nums[i+1]

            # Append the value to the result list 'freq' times
            for j in range(freq):
                res.append(val)
        return res # Return the decompressed list

  def lc_1337(self, mat, k):
        """
        Finds the indices of the k weakest rows in a binary matrix.

        Counts the number of soldiers in each row and stores the counts
        in a list. Then sorts the list of counts and retrieves the indices
        of the k smallest counts. Returns these indices as the result.

        Parameters:
            mat (List[List[int]]): The binary matrix representing the soldiers.
            k (int): The number of weakest rows to return.

        Returns:
            List[int]: The indices of the k weakest rows.
        Example:
            Input: mat = [[1,1,0,0,0],
                          [1,1,1,1,0],
                          [1,0,0,0,0],
                          [1,1,0,0,0],
                          [1,1,1,1,1]],
                  k = 3
            Output: [2,0,3]
        """
        soldier_counts = []
        for row in mat:
            count = sum(row)
            soldier_counts.append(count)
        weakest_rows = sorted(range(len(soldier_counts)), key=lambda x: soldier_counts[x])
        return weakest_rows[:k]

  def lc_1342(self, num):
        """
        Calculates the number of steps to reduce a non-negative integer to zero.

        Each step consists of the following:
        - If the current number is even, divide it by 2.
        - If the current number is odd, subtract 1 from it.

        Parameters:
            num (int): A non-negative integer.

        Returns:
            int: The number of steps required to reduce `num` to zero.

        Example:
            Input: num = 123
            Output - 12
        """

        count=0 # Initialize a variable 'count' to store the number of steps.
        while num!=0: # Continue the loop until 'num' becomes zero.
            if num%2==0: # If 'num' is even:
                num=num//2 # Divide 'num' by 2.
                count+=1 # Increment the step count.
            else:  # If 'num' is odd:
                num=num-1 # Subtract 1 from 'num'.
                count+=1  # Increment the step count.
        return count # Return the total number of steps.

  def lc_1351(self, grid):
        """
        Counts the number of negative integers in a 2D grid.

        Iterates through each element in the 2D grid and counts the number of
        negative integers. Returns the total count of negative integers.

        Parameters:
            grid (List[List[int]]): The 2D grid of integers.

        Returns:
            int: The number of negative integers in the grid.

        Example:
            Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
            Output: 8
        """
        negatives = []
        for row in grid:
            for num in row:
                if num < 0:
                    negatives.append(num)
        return len(negatives)

  def lc_1365(self, nums):
        """
        Counts the number of elements smaller than each element in the given list.

        This function takes a list of integers `nums` and returns a new list where each element at index `i` represents the number of elements in `nums` that are smaller than `nums[i]`.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            List[int]: A new list where each element represents the number of elements smaller than the corresponding element in the input list.

        Example:
            Input: nums = [8, 1, 2, 2, 3]
            Output: [4, 0, 1, 1, 3]
        """

        ls=[] # Initialize an empty list ls to store the counts of elements smaller than each element in nums.
        for i in nums: # Iterate through each element i in nums.
            count=0 # Initialize a counter variable count.
            for j in nums: # Iterate through each element j in nums again.
                if i>j: # Check if the current element i is greater than the element j.
                    count+=1 # If so, increment the count by 1.
            ls.append(count) # Append the count to the list ls.
        return ls # Return the list ls containing counts of elements smaller than each element in nums.

  def lc_1374(self, n):
        """
        Generates a string with n characters such that each character in such string occurs an odd number of times.

        Parameters:
            n (int): The length of the string to generate.

        Returns:
            str: Return a string with n characters such that each character in such string occurs an odd number of times.

        Example :
            Input: n = 4
            Output: bbbz
        """

        if n%2!=0: # If n is odd, return a string consisting of 'a' repeated n times (any alphabet)
            return 'a'*n
        else: # If n is even, return a string consisting of 'b' repeated (n - 1) times followed by 'z' (any alphabet)
            return 'b'*(n-1)+'z'

  def lc_1389(self, nums, index):
        """
        Creates a target array using the given input arrays nums and index.

        Parameters:
            nums (List[int]): An array of integers.
            index (List[int]): An array of integers representing the desired indices for insertion.

        Returns:
            List[int]: The target array created using nums and index.

        Example :
            Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
            Output: [0, 4, 1, 3, 2]
        """

        target_array=[] # Initialize an empty list to store the target array

        # Iterate through each element in nums and index simultaneously using range and len
        for i in range(len(nums)):
            target_array.insert(index[i],nums[i]) # Insert the current element from nums at the specified index in target_array
        return target_array # Return the target array

  def lc_1431(self, candies, extraCandies):
        """
        Determines if each child can have the greatest number of candies after adding some extra candies.

        Parameters:
            candies (List[int]): A list representing the number of candies each child has.
            extraCandies (int): The number of extra candies that can be added to each child.

        Returns:
            List[bool]: A list where each element indicates whether the corresponding child can have the greatest number of candies after adding extra candies.

        Example :
            Input: candies[2,3,5,1,3],extraCandies = 3
            Output: [True, True, True, False, True]
        """
        res=[] # Initialize an empty list to store the result
        maxx=max(candies) # Find the maximum number of candies among all children
        for k in candies: # Iterate through each child's number of candies
            # Check if the current child can have the greatest number of candies after adding extra candies by comparing with the maximum number of candies
            res.append(k+extraCandies>=maxx) # append the result after comparing

        return res # Return the result list

  def lc_1456(self, s, k):
        """
        Finds the maximum number of vowels in a substring of length k within a given string s.

        Parameters:
            s (str): The input string.
            k (int): The length of the substring.

        Returns:
            int: The maximum number of vowels in a substring of length k.

        Example:
            Input: s = "abciiidef", k = 3
            Output : 3
        """

        vowel='aeiou' # Define a string containing all vowels
        max_count=0 # Initialize a variable to store the maximum count of vowels
        for i in range(len(s)): # Iterate through the characters in the input string
            count=0  # Initialize a counter for vowels in the substring of length k
            x=s[i:i+k] # Extract a substring of length k starting from index i

            # Count the number of vowels in the substring
            for j in x:
                if j in vowel:
                    count+=1

            # Update the maximum count if the current count is greater
            if count>max_count:
                max_count=count
        return max_count # Return the maximum count of vowels

  def lc_1460(self, target, arr):
        """
        Checks if the target array can be made equal to the given array by rearranging its elements.

        Creates a dictionary to count the occurrences of each element in the given array. Then, iterates
        through the elements of the target array and decrements the corresponding count in the dictionary.
        Finally, checks if all counts in the dictionary are zero. If so, returns True; otherwise, returns False.

        Parameters:
            target (List[int]): The target array.
            arr (List[int]): The array to compare with the target.

        Returns:
            bool: True if the target array can be made equal to the given array; otherwise, False.

        Example:
            Input: target = [1,2,3,4], arr = [2,4,1,3]
            Output: true
        """
        counts = {}
        for num in arr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for num in target:
            if num in counts:
                counts[num] -= 1

        for count in counts.values():
            if count != 0:
                return False

        return True

  def lc_1464(self, nums):
        """
        Finds the maximum product of two integers in the given list.

        Sorts the list of integers in non-decreasing order and returns the product
        of the two largest integers subtracted by one.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            int: The maximum product of two integers in the list.

        Example:
            Input: nums = [3,4,5,2]
            Output: 12
        """
        sorted_nums = sorted(nums)
        return (sorted_nums[-1] - 1) * (sorted_nums[-2] - 1)

  def lc_1470(self, nums, n):
        """
        Shuffle the array `nums` into the desired pattern.

        Parameters:
            nums (List[int]): The input array of integers.
            n (int): The size of the split between the two halves of the array.

        Returns:
            List[int]: The shuffled array.

        Example:
            Input: nums = [2, 5, 1, 3, 4, 7], n = 3
            Output: [2, 3, 5, 4, 1, 7]
        """

        n=len(nums)//2 # Calculate the size of the split between the two halves of the array.
        ls=nums[:n] # Get the first half of the array.
        k=nums[n:] # Get the second half of the array.
        s=[] # Initialize an empty list to store the shuffled array.
        for i in range(len(ls)): # Iterate through the elements of the first half.
            s.extend([ls[i],k[i]]) # Add the corresponding elements from both halves alternately.
        return s # Return the shuffled array.

  def lc_1475(self, prices):
        """
        Calculates the final prices after discounts for each item in the given list.

        Iterates through the list of prices and compares each price with the prices
        of subsequent items. If a subsequent price is smaller than or equal to the current
        price, subtracts it from the current price and adds the result to the result list.
        If no subsequent price is smaller, adds the current price to the result list as is.

        Parameters:
            prices (List[int]): The list of prices for items.

        Returns:
            List[int]: The final prices after discounts.

        Example:
            Input: prices = [8,4,6,2,3]
            Output: [4,2,4,2,3]
        """
        final_prices = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    final_prices.append(prices[i] - prices[j])
                    break
            else:
                final_prices.append(prices[i])
        return final_prices

  def lc_1480(self, nums):
        """
        Calculates the running sum of a list of integers.

        Parameters:
            nums (List[int]): A list of integers.

        Returns:
            List[int]: Returns a list where the i-th element is the sum of the first i+1 elements of the input list.

        Example :
            Input: nums = [1,2,3,4,5]
            Output: [1, 3, 6, 10, 15]
        """
        res=[] # Initialize an empty list to store the running sum
        s=0 # Initialize a variable to keep track of the running sum
        for num in nums: # Iterate through each number in the input list
            s+=num # Add the current number to the running sum
            res.append(s) # Append the running sum to the result list
        return res # return the resultant lsit

  def lc_1512(self, nums):
        """
        Count the number of identical pairs in the given list.

        Parameters:
            nums (List[int]): The input list of integers.

        Returns:
            int: The count of identical pairs.

        Example:
            Input : nums = [1, 2, 3, 1, 1, 3]
            Output : 4
        """
        count=0 # Initialize count to 0 to count identical pairs
        # Nested loops to iterate over all pairs of elements in nums
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]==nums[j] : # If the elements at indices i and j are identical
                    count+=1 # Increment the count for identical pairs
        return count # Return the count of identical pairs

  def lc_1534(self, arr, a, b, c):
        """
        Counts the number of good triplets in the given array.

        This function takes a list of integers `arr` and three integers `a`, `b`, and `c`.
        It counts the number of good triplets in `arr`, where a triplet (arr[i], arr[j], arr[k]) is considered good
        if the following conditions are met:
        - 0 <= i < j < k < len(arr)
        - abs(arr[i] - arr[j]) <= a
        - abs(arr[j] - arr[k]) <= b
        - abs(arr[i] - arr[k]) <= c

        Parameters:
            arr (List[int]): The list of integers.
            a (int): The maximum difference allowed between arr[i] and arr[j].
            b (int): The maximum difference allowed between arr[j] and arr[k].
            c (int): The maximum difference allowed between arr[i] and arr[k].

        Returns:
            int: The number of good triplets in the array.

        Example:
            Input: arr = [3, 0, 1, 1, 9, 7], a = 7, b = 2, c = 3
            Output: 4
        """

        count=0 # Initialize a variable count to store the number of good triplets.
        for i in range(len(arr)-2): # Iterate through each element in arr until the third-to-last element.
            for j in range(i+1,len(arr)-1): # Iterate through each element in arr starting from the element after i until the second-to-last element.
                for k in range(j+1,len(arr)): # Iterate through each element in arr starting from the element after j until the last element.
                    if i>=0 and i<j and j<k and k<len(arr): # Check if the indices i, j, and k satisfy the condition: 0 <= i < j < k < len(arr).
                        if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c: # Check if the triplet satisfies the conditions for a good triplet.
                            count+=1 # If the triplet is good, increment the count.
        return count # Return the total count of good triplets.

  def lc_1588(self, arr):
        """
        Calculates the sum of all subarrays with an odd length in a given array arr.

        Parameters:
            arr (List[int]): The input array.

        Returns:
            int: The sum of all subarrays with an odd length.

        Example :
            Input: arr = [1,4,2,5,3]
            Output: 58
        """
        odd=1 # Initialize the length of subarrays to 1
        s=0 # Initialize the sum of subarrays to 0
        for i in range(len(arr)): # Iterate through each element of the array
            # Iterate through the array starting from the current element with a step of 2 (to get odd-length subarrays)
            for j in range(i,len(arr),2):
                nums=arr[i:j+1] # Extract the subarray from index i to j (inclusive)
                s+=sum(nums) # Add the sum of the subarray to the total sum

        return s # Return the sum of all subarrays with an odd length

  def lc_1614(self, s):
        """
        Find the maximum nesting depth of parentheses in the given string.

        Parameters:
            s (str): The input string containing parentheses.

        Returns:
            int: The maximum nesting depth.

        Example:
            Input: s = "(1+(2*3)+((8)/4))+1"
            Output: 3
        """
        ls=[] # list to keep track of opening parentheses
        res=0 # Variable to store the maximum nesting depth
        # Iterate over each character in the string
        for c in s:
            if c=='(': # If the character is an opening parenthesis
                ls.append(c)  # append to list
                res=max(res,len(ls)) # Update the maximum depth if needed
            elif c==')': # If the character is a closing parenthesis
                ls.pop() # Pop the corresponding opening parenthesis from the list
        return res # Return the maximum nesting depth

  def lc_1672(self, accounts):
        """
        Finds the maximum wealth among the customers.

        This function takes a list of lists `accounts`, where each inner list represents the wealth of a customer. It calculates the total wealth for each customer and returns the maximum wealth among them.

        Parameters:
            accounts (List[List[int]]): A list of lists representing the wealth of customers.

        Returns:
            int: The maximum wealth among the customers.

        Example:
            Input: accounts = [[1, 2, 3], [3, 2, 1]]
            Output: 6
        """

        max=sum(accounts[0]) # Initialize max as the total wealth of the first customer.
        for i in range(len(accounts)-1): # Iterate through each customer's wealth.
            if max<sum(accounts[i+1]): # Check if the total wealth of the next customer is greater than the current max.
                max=sum(accounts[i+1]) # If so, update max to the total wealth of the next customer.
        return max # Return the maximum wealth among the customers.

  def lc_1678(self, command):
        """
        Performs string interpretation based on a given command.

        Parameters:
            command (str): The input command string.

        Returns:
            str: The interpreted string.

        Example :
            Input: command = "G()(al)"
            Output: Goal
        """
        s='' # Initialize an empty string to store the interpreted result
        for i in range(len(command)): # Iterate over the indices of the command string
            if command[i:i+2]=='()':  # Check if the current substring is '()'
                s+='o' # If '()' is found, concat 'o' to the interpreted string
            elif command[i]=='(' or command[i]==')': # Check if the current character is '(' or ')'
                continue # If it is, skip this character and continue to the next iteration
            else:
                # If the current character is not '()' or '(', append it to the interpreted string
                s+=command[i]
        return s # Return the interpreted string

  def lc_1684(self, allowed, words):
        """
        Counts the number of consistent strings from a list of words with a given set of allowed characters.

        Parameters:
            allowed (str): A string representing the set of allowed characters.
            words (List[str]): A list of words to be checked for consistency.

        Returns:
            int: The count of consistent strings.

        Example :
            Input: allowed = 'ab', words = ["ad","bd","aaab","baa","badab"]
            Output: 2
        """
        res=0 # Initialize a variable to store the count of consistent strings
        for word in words: # Iterate through each word in the list of words
            for ch in word: # Iterate through each character in the current word
                if ch not in allowed:
                    # If any character in the word is not in the set of allowed characters, break out of the loop and move to the next word
                    break
            else:
                res+=1 # If all characters in the word are allowed, increment the count of consistent strings
        return res # Return the count of consistent strings

  def lc_1704(self, s):
        """
        Checks if the two halves of a given string have an equal number of vowels.

        Parameters:
            s (str): The input string to be checked.

        Returns:
            bool: Returns True if the two halves of the string have an equal number of vowels, otherwise returns False.

        Example :
            Input: s = "textbook"
            Output: False
        """
        vowels='aeiouAEIOU' # Define a string containing all vowels
        n=len(s)//2 # Calculate the length of half of the string
        a,b=s[:n],s[n:] # Split the string into two halves
        v1,v2=0,0 # Initialize counters for vowels in each half
        for i in range(n): # Iterate through the characters in the first half
            if a[i] in vowels: v1+=1 # Increment v1 if the character is a vowel
            if b[i] in vowels: v2+=1  # Increment v2 if the corresponding character in the second half is a vowel
        return v1==v2 # Check if the number of vowels in both halves are equal and return the result

  def lc_1725(self, rectangles):
        """
        Counts the number of rectangles with the maximum possible side length.

        Iterates through the list of rectangles and computes the minimum side length
        for each rectangle. Then, counts the number of rectangles with a minimum side
        length equal to the maximum among all minimum side lengths.

        Parameters:
            rectangles (List[List[int]]): The list of rectangles represented as pairs
                                           of side lengths.

        Returns:
            int: The number of rectangles with the maximum possible side length.

        Example:
            Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
            Output: 3
        """
        min_side_lengths = [min(rectangle) for rectangle in rectangles]
        max_min_side_length = max(min_side_lengths)
        return min_side_lengths.count(max_min_side_length)

  def lc_1742(self, lowLimit, highLimit):
        """
        Counts the maximum number of balls in any box after placing balls numbered from lowLimit to highLimit into boxes.

        Parameters:
            lowLimit (int): The lowest ball number.
            highLimit (int): The highest ball number.

        Returns:
            int: The maximum number of balls in any box.

        Example :
            Input: lowlimit = 11, highlimit = 104
            Output 9
        """
        boxes = [0] * 100 # Create a list to represent the boxes, initialized with zeros

        for i in range(lowLimit, highLimit + 1): # Iterate over each ball number from lowLimit to highLimit
            # Calculate the sum of digits in the current ball number and Increment the count of balls in the corresponding box
            boxes[sum([int(j) for j in str(i)])] += 1
        return max(boxes) # Return the maximum count of balls in any box

  def lc_1748(self, nums):
        """
        Calculates the sum of unique elements in the given list.

        Parameters:
            nums (List[int]): A list of integers.

        Returns:
            int: The sum of unique elements in the list.

        Example:
            Input: nums = [1, 2, 3, 2]
            Output: 4
        """
        ls=[] # Initialize an empty list 'ls' to store unique elements.
        for i in nums: # Iterate through each element in nums.
            if nums.count(i)==1: # Check if the current element appears only once in the list.
                ls.append(i) # If so, append it to the list of unique elements.
        return sum(ls) # Return the sum of unique elements.

  def lc_1733(self, items, ruleKey, ruleValue):
        """
        Counts the number of items in the given list that match the specified rule.

        Determines the index corresponding to the ruleKey ("type", "color", or "name").
        Then, iterates through each item in the list and checks if the value at the
        determined index matches the ruleValue. If it does, increments a counter.
        Finally, returns the count of matching items.

        Parameters:
            items (List[List[str]]): The list of items, each represented as a list of strings.
            ruleKey (str): The rule to match against ("type", "color", or "name").
            ruleValue (str): The value to match against.

        Returns:
            int: The number of items that match the specified rule.

        Example:
            Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], 
                    ruleKey = "color", ruleValue = "silver"
            Output: 1
        """
        count = 0
        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        elif ruleKey == "name":
            index = 2
        else:
            raise ValueError("Invalid ruleKey. Must be 'type', 'color', or 'name'.")

        for item in items:
            if item[index] == ruleValue:
                count += 1

        return count

  def lc_1816(self, s, k):
        """
        Truncates a sentence to contain only the first k words.

          Parameters:
              s (str): The input sentence.
              k (int): The number of words to retain in the truncated sentence.

          Returns:
              str: The truncated sentence.

        Example:
            Input: s = "Hello how are you Contestant",k = 4
            Output: Hello how are you
        """

        s=s.split() # Split the input sentence into words.
        s=s[:k] # Retain only the first k words.
        return " ".join(s) # Join the retained words to form the truncated sentence.

  def lc_1827(self, nums):
        """
        Find the minimum number of operations required to make the list of numbers strictly increasing.

        Parameters:
            nums (List[int]): The input list of integers.

        Returns:
            int: The minimum number of operations required.

        Example:
            Input: nums = [1, 1, 1]
            Output: 3
        """
        count=0 # Counter for the number of operations
        for i in range(len(nums)-1): # Iterate over each index in the range of the length of the list minus 1
            if nums[i]>=nums[i+1]: # If the current number is greater than or equal to the next number
                count+=(nums[i]+1)-nums[i+1] # Calculate the operation needed to make the next number greater
                nums[i+1]=nums[i]+1 # Update the next number to be strictly increasing
        return count # Return the minimum number of operations required

  def lc_1832(self, sentence):
        """
        Checks if the given sentence is a pangram.

        This function takes a string `sentence` and checks if it contains all the letters of the alphabet at least once, making it a pangram.

        Parameters:
            sentence (str): The input sentence.

        Returns:
            bool: True if the sentence is a pangram, False otherwise.

        Example:
            Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
            Output: True
        """

        sentence=sentence.lower() # Convert the sentence to lowercase to make the comparison case-insensitive.
        for i in range(97,123): # Iterate through the ASCII values corresponding to lowercase letters ('a' to 'z').
            if chr(i) not in sentence: # Check if the current letter (converted from ASCII value) is not present in the sentence.
                return False # If any letter is missing, return False as it's not a pangram.
        return True # If all letters are present, return True as it's a pangram.

  def lc_1837(self, n, k):
        """
        Calculates the sum of the digits of a positive integer n in base k.

        Iteratively computes the remainder of n when divided by k and adds it to
        the running total. Then, updates n to be the result of integer division of
        n by k. Continues this process until n becomes zero. Finally, returns the
        sum of the digits in base k.

        Parameters:
            n (int): The positive integer to convert to base k.
            k (int): The base to convert to.

        Returns:
            int: The sum of the digits of n in base k.

        Example:
            Input: n = 34, k = 6
            Output: 9
        """
        total = 0
        while n:
            remainder = n % k
            total += remainder
            n = n // k
        return total

  def lc_1844(self, s):
        """
        Replaces each digit in the string with a character.

        This function takes a string `s` containing lowercase English letters and digits. For each digit in `s`, it replaces it with the character located `shift` positions after it in the alphabet.

        Parameters:
            s (str): The input string containing lowercase English letters and digits.

        Returns:
            str: The modified string with digits replaced by characters.

        Example:
            Input: s = "a1c1e1"
            Output: "abcdef"
        """

        c='' # Initialize an empty string to store the modified string
        for i in range(len(s)): # Iterate over each character in the input string s
            if s[i].isalpha(): # If the current character is a letter
                c+=s[i] # Append the letter to the modified string
            else: # If the current character is a digit
                c+=chr(ord(s[i-1])+int(s[i])) # Append the character located `shift` positions after the previous letter to the modified string

        return c # Return the modified string

  def lc_1848(self, nums, target, start):
        """
        Finds the minimum distance between a target integer and a start index in a list.

        Iterates through the list of integers and checks for occurrences of the target integer.
        For each occurrence, calculates the absolute difference between its index and the start index
        and appends it to a list. Finally, returns the minimum value from the list of absolute differences.

        Parameters:
            nums (List[int]): The list of integers.
            target (int): The target integer to find.
            start (int): The starting index to measure the distance from.

        Returns:
            int: The minimum distance between the target integer and the start index.

        Example:
            Input: nums = [1,2,3,4,5], target = 5, start = 3
            Output: 1
        """
        distances = []
        for i in range(len(nums)):
            if nums[i] == target:
                distances.append(abs(i - start))
        return min(distances)

  def lc_1859(self, s):
        """
        Sorts a sentence based on the numbers present at the end of each word.

        Args:
            s (str): Input sentence where each word ends with a number.

        Returns:
            str: Sorted sentence with words ordered based on the numbers.

        Example:
            Input: s = "is2 sentence4 This1 a3"
            Output: 'This is a sentence'
        """
        ls=[] # Initialize an empty list to store words.
        s=s.split() # Split the input sentence into words.
        for i in range(1,len(s)+1): # Iterate over numbers from 1 to the length of the sentence.
            for j in range(len(s)): # Iterate through the words in the sentence.
                if str(i) in s[j]: # Check if the current number is present in the word.
                    k=s[j] # Store the word with the current number.
                    ls.append(k[:-1]) # Append the word without the number to the list.
        return " ".join(ls) # Join the words in the list to form the sorted sentence.

  def lc_1876(self, s):
        """
        Counts the number of good substrings in a string.

        A good substring is a substring of length 3 with distinct characters.

        Parameters:
            s (str): Input string.

        Returns:
            int: The number of good substrings in the input string.

        Example:
            Input: s = "aababcabc"
            Output: 4
        """

        ls=[]  # Initialize an empty list 'ls' to store all substrings of length 3.
        for i in range(len(s)-2): # Iterate through indices of 's' up to len(s) - 3.
            ls.append(s[i:i+3]) # Append each substring of length 3 to 'ls'.
        k=[] # Initialize an empty list 'k' to store good substrings.
        for i in ls: # Iterate through each substring in 'ls'.
            if len(set(i))==len(i): # Check if the substring has distinct characters.
                k.append(i) # If it does, append the substring to 'k'.
        return len(k) # Return the number of good substrings.

  def lc_1880(self, firstWord, secondWord, targetWord):
        """
        Checks if the sum of the numerical values of two words is equal to the numerical value of another word.

        This function takes three strings `firstWord`, `secondWord`, and `targetWord`, where each character in the strings represents a digit (from 'a' to 'j', i.e., 0 to 9) and returns True if the sum of the numerical values of `firstWord` and `secondWord` is equal to the numerical value of `targetWord`. Otherwise, it returns False.

        Parameters:
            firstWord (str): The first word.
            secondWord (str): The second word.
            targetWord (str): The target word.

        Returns:
            bool: True if the sum of the numerical values of `firstWord` and `secondWord` is equal to the numerical value of `targetWord`, False otherwise.

        Example:
            Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
            Output: True
        """

        s=[firstWord,secondWord,targetWord] #store three words in a list
        d={chr(97+i):i for i in range(0,26)} #create a dictionary to map characters to their numarical values(a maps to 0,b maps to 1.....)
        a=[] # Initialize a list to store the numerical values of the words.
        for word in s: #Iterate over each word in the list
            b=""  #Initialize an empty string to store the numerical value of the current word
            for letter in word: #Iterate over each letter in the current word
                b+=str(d[letter]) #Append numerical value of the current letter to the string
            a.append(b) #append numerical value of the current word to the list
        return int(a[0])+int(a[1])==int(a[2]) #check if the sum of numerical values of the first two words is equal to the numerical value of the third word and return true or false accordingly

  def lc_1913(self, nums):
        """
        Calculates the maximum difference between the products of any two pairs of numbers in the given list nums.

        Parameters:
            nums (List[int]): A list of integers.

        Returns:
            int: The maximum difference between the products of any two pairs of numbers.

        Example :
            Input : nums = [4,2,5,9,7,4,8]
            Output: 64
        """

        nums.sort() # Sort the input list nums in ascending order
        min_product=nums[0]*nums[1] # Calculate the product of the two smallest numbers
        max_product=nums[-1]*nums[-2] # Calculate the product of the two largest numbers
        return max_product-min_product # Return the difference between max_product and min_product

  def lc_1920(self, nums):
        """
        Builds an array where each element at index i is replaced with the value at index nums[i].

        Parameters:
            nums (List[int]): A list of integers representing indices.

        Returns:
            List[int]: The resulting array.

        Example:
            Input: nums = [0,2,1,5,3,4]
            Output: [0, 1, 2, 4, 5, 3]
        """

        ans=[] # Initialize an empty list to store the resulting array
        for i in range(len(nums)):  # Iterate through the indices in the nums list
            num=nums[nums[i]]  # Get the value at the index specified by nums[i]
            ans.append(num)  # Append the obtained value to the resulting array
        return ans # Return the resulting array

  def lc_1929(self, nums):
        """
        Concatenates a list with itself.

        Parameters:
            nums (List[int]): Input list of integers.

        Returns:
            List[int]: The concatenated list.

        Example:
            Input: nums = [1, 2, 1]
            Output: [1, 2, 1, 1, 2, 1]
        """

        return nums + nums # Concatenate the list nums with itself using the + operator.

  def lc_1935(self, text, brokenLetters):
        """
        Calculates the number of words in the given text that can be typed without using any broken letters.

        Splits the text into words and iterates through each character in the text.
        If a space character is encountered, increments the word count and continues.
        If a character in the text is found in the list of broken letters, adds the current
        word index to a set. Finally, returns the difference between the total number of words
        and the number of words with broken letters.

        Parameters:
            text (str): The input text.
            brokenLetters (str): The string containing broken letters.

        Returns:
            int: The number of words that can be typed without using any broken letters.

        Example:
            Input: text = "hello world", brokenLetters = "ad"
            Output: 1
        """
        broken_indices = set()
        word_count = 0
        for i, char in enumerate(text):
            if char == " ":
                word_count += 1
            elif char in brokenLetters:
                broken_indices.add(word_count)
        return len(text.split()) - len(broken_indices)

  def lc_1941(self, s: str) -> bool:
        """
        Checks if all characters in a string occur the same number of times.

        Parameters:
            s (str): The input string to be checked.

        Returns:
            bool: Returns True if all characters in the string occur the same number of times, otherwise returns False.

        Example :
            Input: s = 'abacbc'
            Output: True
        """
        d={} # Create an empty dictionary to store the count of occurrences for each character
        for i in set(s):
            # Count occurrences of each character and store them in the dictionary
            d[i]=s.count(i)
        l=set(d.values())  # Get the set of counts of occurrences
        return len(l)==1 # Check if all counts are the same

  def lc_1979(self, nums):
        """
        Finds the greatest common divisor (GCD) of the minimum and maximum elements in the given list.

        Uses the built-in `math.gcd` function to calculate the GCD of the minimum and maximum elements
        in the list. Returns the computed GCD.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            int: The greatest common divisor (GCD) of the minimum and maximum elements in the list.

        Example:
            Input: nums = [2,5,6,9,10]
            Output: 2
        """
        return math.gcd(min(nums), max(nums))

  def lc_2000(self, word, ch):
        """
        Reverses the substring of word from the beginning to the first occurrence of character ch, inclusive.

        Parameters:
            word (str): The input word.
            ch (str): The character used to determine the prefix to reverse.

        Returns:
            str: The word with the prefix reversed, or the original word if ch is not found.

        Example :
            Input: word = 'abxdss', ch = 'd'
            Output: dxbass
        """

        s='' # Initialize an empty string to store the result
        indx=word.find(ch) # Find the index of the first occurrence of character ch in the word

        if indx == -1:
            return word # If ch is not found in the word, return the original word
        else:
            # Construct the result string by concatenating the reversed prefix (from beginning to indx) with the remaining characters of the word (after indx)
            s=word[indx::-1]+word[indx+1:]
            return s # Return the result string

  def lc_2006(self, nums, k):
        """
        Counts the number of pairs in the list nums having a difference of k.

        Parameters:
            nums (List[int]): The input list of integers.
            k (int): The target difference.

        Returns:
            int: The count of pairs having a difference of k.

        Example :
            Input: nums = [1,2,2,1], k = 1
            Output: 4
        """
        count=0 # Initialize a variable to store the count of pairs
        for i in range(len(nums)): # Iterate over the indices of the list nums
            for j in range(i+1,len(nums)): # Iterate over the indices starting from i + 1 to the end of the list
                if abs(nums[i]-nums[j])==k: # Check if the absolute difference between the elements at indices i and j is equal to k
                    count+=1 # If so, increment the count
        return count# Return the count of pairs

  def lc_2011(self, operations):
        """
        Calculates the final value after performing a sequence of operations.

        Iterates through each operation in the list and updates the value based on
        the operation type ("--X" or "X++"). For each "--X" or "X--" operation, decrements
        the value by 1; for each "++X" or "X++" operation, increments the value by 1.
        Finally, returns the computed final value.

        Parameters:
            operations (List[str]): The list of operations to perform.

        Returns:
            int: The final value after performing the operations.

        Example:
            Input: operations = ["--X","X++","X++"]
            Output: 1
        """
        value = 0
        for operation in operations:
            if operation == "--X" or operation == "X--":
                value -= 1
            else:
                value += 1
        return value

  def lc_2032(self, nums1, nums2, nums3):
        """
        Finds the numbers that appear in at least two of the given lists.

        Iterates through each number in the first list and checks if it appears
        in either of the other two lists. If it does, adds it to a set. Then, repeats
        the same process for each number in the second list. Finally, returns the set
        of numbers that appear in at least two of the given lists.

        Parameters:
            nums1 (List[int]): The first list of integers.
            nums2 (List[int]): The second list of integers.
            nums3 (List[int]): The third list of integers.

        Returns:
            List[int]: The list of numbers that appear in at least two of the given lists.

        Example :
            Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
            Output: [3,2]
        """
        result = set()
        for num in nums1:
            if num in nums2 or num in nums3:
                result.add(num)
        for num in nums2:
            if num in nums1 or num in nums3:
                result.add(num)
        return list(result)

  def lc_2037(self, seats, students):
        """
        Calculates the minimum total number of moves required to seat students on seats.

        Parameters:
            seats (List[int]): A list of integers representing the positions of seats.
            students (List[int]): A list of integers representing the positions of students.

        Returns:
            int: Returns the minimum total number of moves required to seat all students.

        Example :
            Input: seats = [2,2,6,6], students = [1,3,2,6]
            Output: 4
        """
        # Sort the lists of seats and students to ensure they are in ascending order
        seats.sort()
        students.sort()
        res=0 # Initialize a variable to store the total number of moves required
        for i in range(len(seats)):
            # Calculate the absolute difference between the positions of seats and students and sum them up
            res+=abs(seats[i]-students[i])
        return res # return the total moves

  def lc_2053(self, arr, k):
        """
        Finds the kth distinct element in the given list.

        Counts the occurrences of each element in the list and creates a dictionary
        with elements as keys and their counts as values. Sorts the dictionary based on
        counts in ascending order. Then, iterates through the sorted dictionary and
        collects elements with a count of 1 (distinct elements) into a list. Finally,
        returns the kth element from the list of distinct elements.

        Parameters:
            arr (List[str]): The list of strings.
            k (int): The index of the desired distinct element (1-indexed).

        Returns:
            str: The kth distinct element in the list, or an empty string if not found.

        Example :
            Input: arr = ["d","b","c","b","c","a"], k = 2
            Output: "a"
        """
        counts = {}
        distinct_elements = []

        # Count occurrences of each element
        for item in arr:
            if item not in counts:
                counts[item] = 1
            else:
                counts[item] += 1

        # Sort the dictionary based on counts
        sorted_counts = dict(sorted(counts.items(), key=lambda x: x[1]))

        # Collect distinct elements
        for item, count in sorted_counts.items():
            if count == 1:
                distinct_elements.append(item)

        # Return the kth distinct element if it exists
        if len(distinct_elements) >= k:
            return distinct_elements[k - 1]
        else:
            return ""

  def lc_2057(self, nums):
        """
        Finds the smallest index i such that i modulo 10 equals the value at index i in the given list.

        Iterates through the list and checks if the index modulo 10 is equal to the value at that index.
        If it is, adds the index to a list. Finally, returns the smallest index from the list, or -1 if no
        such index is found.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            int: The smallest index i such that i modulo 10 equals the value at index i, or -1 if not found.

        Example :
            Input: nums = [0,1,2]
            Output: 0
        """
        indices = []
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                indices.append(i)
        if indices:
            return min(indices)
        else:
            return -1

  def lc_2089(self, nums, target):
        """
        Finds the indices of all occurrences of the target value in the given list.

        Sorts the given list and iterates through each element to find the indices
        where the element is equal to the target value. Appends these indices to a list
        and returns it.

        Parameters:
            nums (List[int]): The list of integers.
            target (int): The target value to search for.

        Returns:
            List[int]: The list of indices where the target value occurs in the list.

        Example :
            Input: nums = [1,2,5,2,3], target = 2
            Output: [1,2]
        """
        indices = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] == target:
                indices.append(i)
        return indices

  def lc_2103(self, rings):
        """
        Counts the number of points where rings of three different colors intersect at the same rod.
        Parameters:
            rings (str): A string representing rings and their positions.
        Returns:
            int: The count of points where rings of three different colors intersect at the same rod.
        Example :
            Input: rings = "G3R3R7B7R5B1G8G4B3G6"
            Output: 1
        """
        ring='RGB' # Define the colors of the rings
        rods=[[],[],[],[],[],[],[],[],[],[]] # Create a list of lists representing rods and their corresponding rings
        for i in range(0,len(rings),2): # Iterate through the input string in steps of 2
            # Extract the ring color and rod number from the current position in the string
            indx=int(rings[i+1])
            rods[indx].append(rings[i]) # Append the ring color to the corresponding rod list
        count=0# Initialize a variable to count the points where rings of three different colors intersect
        for i in range(len(rods)): # Iterate through each rod
            for j in ring: # Iterate through each color of the rings
                if j not in rods[i]: # If the current color is not present in the rings of the current rod, break the loop
                    break
            else: # If all three colors are present in the rings of the current rod, increment the count
                count+=1
        return count # Return the count of points where rings of three different colors intersect at the same rod

  def lc_2108(self, words):
        """
        Finds the first palindrome word in the given list of words.

        Iterates through each word in the list and checks if it is equal to its
        reverse. If a palindrome word is found, returns it. Otherwise, returns an
        empty string if no palindrome word is found.

        Parameters:
            words (List[str]): The list of words.

        Returns:
            str: The first palindrome word in the list, or an empty string if not found.

        Example :
            Input: words = ["abc","car","ada","racecar","cool"]
            Output: "ada"
        """
        palindromes = []
        for word in words:
            if word == word[::-1]:
                palindromes.append(word)
        if palindromes:
            return palindromes[0]
        else:
            return ""

  def lc_2114(self, sentences):
        """
        Find the sentence(s) with the maximum number of words in the given list of sentences.

        Parameters:
            sentences (List[str]): The list of sentences.

        Returns:
            int : the sentence(s) with the maximum count of words.

        Example:
            Input: sentences = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
            Output - 6
        """
        ls=[] # List to store the word counts of each sentence
        for i in sentences: # Iterate over each sentence in the list
            k=i.count(' ') # Count the number of words in the sentence
            ls.append(k+1) # Append the word count to the list
        return max(ls) # Return the maximum word count found in any sentence

  def lc_2124(self, s):
        """
        Checks if the characters in the given string are in non-decreasing order.

        Sorts the characters of the string in non-decreasing order and compares
        it with the original string. If they are equal, returns True indicating
        that the string is in non-decreasing order. Otherwise, returns False.

        Parameters:
            s (str): The input string.

        Returns:
            bool: True if the string is in non-decreasing order, False otherwise.

        Example :
            Input: s = "aaabbb"
            Output: true
        """
        sorted_str = "".join(sorted(s))
        return sorted_str == s

  def lc_2138(self, s, k, fill):
        """
        Divides a string s into substrings of length k and fills the last substring with a specified character fill if necessary.

        Parameters:
            s (str): The input string.
            k (int): The length of each substring.
            fill (str): The character to fill the last substring if its length is less than k.

        Returns:
            List[str]: A list of substrings after division.

        Example :
            Input: s = "abcdefghij", k = 3, fill = 'x'
            Output: ['abc', 'def', 'ghi', 'jxx']
        """
        res=[] # Initialize an empty list to store the resulting substrings
        i=0 # Initialize a variable to keep track of the starting index of each substring
        while i in range(len(s)): # Loop until the index is within the length of the input string
            l=len(s[i:]) # Calculate the length of the remaining substring
            if k>l: # Check if the remaining substring length is less than k
                #l=k-len(s[i:])
                f=s[i:]+(fill*(k-l)) # If so, fill the remaining substring with the specified character 'fill'
                res.append(f) # and append it to the result list
                break # Exit the loop as there are no more characters left to process
            else:
                # Otherwise, extract a substring of length k and append it to the result list
                res.append(s[i:i+k])
                i+=k # Move the index to the next substring
        return res # Return the list of resulting substrings

  def lc_2154(self, nums, original):
        """
        Finds the final value of the 'original' variable after performing operations specified by the 'nums' list.

        Continuously doubles the value of 'original' as long as it is present in the 'nums' list.
        This process is repeated until 'original' is no longer found in the list.

        Parameters:
            nums (List[int]): The list of integers representing operations.
            original (int): The initial value of the 'original' variable.

        Returns:
            int: The final value of the 'original' variable after all operations.

        Example :
            Input: nums = [5,3,6,1,12], original = 3
            Output: 24
        """
        while original in nums:
            for num in nums:
                if num == original:
                    original *= 2
        return original

  def lc_2160(self, num):
        """
        Finds the minimum sum of a four-digit number formed by rearranging the digits of the given number.

        Converts the given number to a string and sorts its digits in non-decreasing order.
        Then, forms two two-digit numbers by concatenating the first and last digit, and the
        second and third digit, respectively. Finally, returns the sum of these two two-digit numbers.

        Parameters:
            num (int): The input four-digit number.

        Returns:
            int: The minimum sum of two two-digit numbers formed by rearranging the digits of the input number.

        Example :
            Input: num = 2932
            Output: 52
        """
        digits = list(str(num))
        sorted_digits = sorted(digits)
        num1 = sorted_digits[0] + sorted_digits[3]
        num2 = sorted_digits[1] + sorted_digits[2]
        return int(num1) + int(num2)

  def lc_2169(self, num1, num2):
        """
        Counts the number of operations required to make both numbers equal using the given operations.

        Iteratively subtracts the smaller number from the larger number until both numbers become equal.
        Counts each subtraction operation performed and returns the total count.

        Parameters:
            num1 (int): The first integer.
            num2 (int): The second integer.

        Returns:
            int: The number of operations required to make both numbers equal.

        Example :
            Input: num1 = 2, num2 = 3
            Output: 3
        """
        operations_count = 0
        while num1 and num2:
            if num1 >= num2:
                num1 -= num2
                operations_count += 1
            else:
                num2 -= num1
                operations_count += 1
        return operations_count

  def lc_2176(self, nums, k):
        """
        Counts the number of pairs in the given list whose values are equal and the product of their indices is divisible by k.

        Iterates through all pairs of indices in the list and checks if the values at those indices are equal.
        If they are equal and the product of their indices is divisible by k, increments the count of pairs.
        Returns the total count of such pairs.

        Parameters:
            nums (List[int]): The list of integers.
            k (int): The divisor to check the product of indices against.

        Returns:
            int: The number of pairs satisfying the given conditions.

        Example :
            Input: nums = [3,1,2,2,2,1,3], k = 2
            Output: 4
        """
        pair_count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    pair_count += 1
        return pair_count

  def lc_2243(self, s: str, k: int) -> str:
        """
        Calculates the digit sum of a string s and repeats the process until the length of the string is less than or equal to k.

        Parameters:
            s (str): The input string.
            k (int): The target length of the string.

        Returns:
            str: The resulting string after digit sum calculation and repetition.

        Example :
            Input: s = "11111222223", k = 3
            Output: '135'
        """
        # Repeat the process until the length of the string is less than or equal to k
        while len(s)>k:
            lis=[] # Initialize an empty list to store substrings of length 'k'
            for i in range(0,len(s),k): # Split the string 's' into substrings of length 'k'
                if k>len(s[i:]): # Check if the remaining substring length is less than 'k'
                    lis.append(s[i:]) # If so, append the remaining substring to the list
                else:
                    lis.append(s[i:i+k])  # Otherwise, append a substring of length 'k' to the list
            x='' # Initialize an empty string to store the new string after digit sum calculation
            for l in lis: # Calculate the digit sum for each substring and concatenate the results
                digit_sum=str(sum(list(map(int,l)))) # Calculate the digit sum of the substring and convert it to a string
                x=x+digit_sum # Concatenate the digit sum to the new string
            s=x # Update the string 's' with the new string after digit sum calculation
        return s # Return the resulting string

  def lc_2278(self, s, letter):
        """
        Calculates the percentage of occurrences of a specific letter in a given string.

        Iterates through each character in the string and counts the occurrences of the specified letter.
        Calculates the percentage by dividing the count of occurrences of the letter by the total length of
        the string and multiplying by 100. Returns the integer value of the calculated percentage.

        Parameters:
            s (str): The input string.
            letter (str): The letter whose percentage of occurrences is to be calculated.

        Returns:
            int: The percentage of occurrences of the specified letter in the given string.

        Example :
            Input: s = "foobar", letter = "o"
            Output: 33
        """
        letter_count = 0
        for char in s:
            if char == letter:
                letter_count += 1

        percentage = (letter_count / len(s)) * 100
        return int(percentage)

  def lc_2283(self, num):
        """
        Checks if the count of each digit in the input number num matches the digit itself.

        Parameters:
            num (str): The input number.

        Returns:
            bool: True if the count of each digit matches the digit itself, False otherwise.

        Example :
            Input: num = '1210'
            Output: True
        """
        num_list=list(map(int,num)) # Convert the input number to a list of integers
        for i in range(len(num_list)): # Iterate over the indices of the list
            if num_list[i]!=num.count(str(i)): # Check if the digit at index i is equal to the count of digit i in the input number
                return False # If not, return False

        return True # If all counts match their corresponding digits, return True

  def lc_2315(self, s):
        """
        Counts the number of '*' characters in s, excluding those between pairs of '|'.

        Parameters:
            s (str): Input string containing substrings separated by '|'.

        Returns:
            int: Number of '*' characters excluding those between '|' pairs.

        Example:
            Input: s = "l|*e*et|c**o|*de|"
            Output: 2
        """

        ls=[] # Initialize an empty list to store counts of '*' characters.
        k=[] # Initialize an empty list to store substring counts of '*' characters.
        s=s.split('|') # Split the input string by '|' characters.
        for i in range(len(s)):  # Iterate through the substrings.
            if i%2==0: # Check if the index is even (outside '|' pairs).
                k.append(s[i].count('*')) # Count the number of '*' characters in the substring and append to the list.
        return sum(k) # Return the sum of counts of '*' characters.

  def lc_2357(self, nums):
        """
        Calculates the minimum number of operations required to make all elements of the list zero.

        Iteratively performs operations to make all elements of the list zero.
        In each iteration, finds the minimum non-zero element of the list and subtracts it from all elements.
        Increments the count of operations for each iteration until all elements become zero.
        Returns the total count of operations performed.

        Parameters:
            nums (List[int]): The list of integers.

        Returns:
            int: The minimum number of operations required to make all elements of the list zero.

        Example :
            Input: nums = [1,5,0,3,5]
            Output: 3
        """
        operations_count = 0
        while sum(nums) != 0:
            min_non_zero = min([num for num in nums if num != 0])
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= min_non_zero
            operations_count += 1
        return operations_count

  def lc_2413(self, n):
        """
        Finds the smallest even multiple of a given number.

        Iterates through integers from 1 to 2 * n (inclusive).
        Checks if the current integer is even and divisible by n.
        If such an integer is found, returns it as the smallest even multiple of n.

        Parameters:
            n (int): The given number.

        Returns:
            int: The smallest even multiple of the given number.

        Example :
            Input: n = 5
            Output: 10
        """
        for i in range(1, (n * 2) + 1):
            if i % 2 == 0 and i % n == 0:
                return i

  def lc_2418(self, names, heights):
        """
        Sorts people's names based on their heights in descending order.

        Parameters:
            names (List[str]): List of people's names.
            heights (List[int]): List of corresponding heights.

        Returns:
            List[str]: Sorted list of people's names based on their heights.

        Example:
            Input : names = ["Mary", "John", "Emma"], heights = [180, 165, 170]
            Output: ['Mary', 'Emma', 'John']
        """
        d={heights[i]:names[i] for i in range(len(names))} # Create a dictionary where heights are keys and names are values.
        k=sorted(d.keys(),reverse=True) # Sort keys (heights) in descending order.
        ls=[] # Initialize an empty list to store sorted names.
        for i in k: # Iterate through sorted keys.
            if i in d: # Check if the key exists in the dictionary.
                ls.append(d[i]) # Append the corresponding name to the list.
        return ls # Return the sorted list of names.

  def lc_2427(self, a: int, b: int) -> int:
        """
        Finds the number of common factors of two given integers.

        Parameters:
            a (int): The first integer.
            b (int): The second integer.

        Returns:
            int: Returns the number of common factors of the two integers.

        Example :
            Input: a = 12, b = 6
            Output: 4
        """
        res=0 # Initialize the variable to store the count of common factors
        for i in range(1,min(a,b)+1): # Iterate through numbers from 1 to the minimum of a and b
            if a%i==0 and b%i==0: # Check if both a and b are divisible by the current number
                res+=1 # If divisible, increment the count of common factors
        return res # Return the count of common factors

  def lc_2455(self, nums):
        """
        Calculates the average value of elements in a list that are divisible by 6.

        Parameters:
            nums (List[int]): A list of integers.

        Returns:
            int: Returns the average value of elements in the list that are divisible by 6.
                 If no elements are divisible by 6, returns 0.

        Example :
            Input: nums = [1,2,3,6,7,12]
            Output: 9
        """
        lis=[i for i in nums if i%6==0] # Filter elements in the list that are divisible by 6

        avg=0  # initialize a variable to store the average
        if len(lis)!=0: # Check if the length of list is not equal to 0
            avg = sum(lis)//len(lis) # Calculate the average of all the elements in the list
        return avg # return the average

  def lc_2469(self, celsius):
        """
        Converts a temperature in Celsius to Kelvin and Fahrenheit.

        Parameters:
            celsius (float): The temperature in Celsius.

        Returns:
            List[float]: Returns a list containing the temperature converted to Kelvin and Fahrenheit respectively.

        Example :
            Input: celsius = 36.50
            Output: [309.65, 97.7]
        """
        kelvin = celsius + 273.15 # Convert Celsius to Kelvin
        fahrenheit = (celsius * 1.80) + 32.00 # Convert Celsius to Fahrenheit
        return [kelvin,fahrenheit] # Return the temperatures in Kelvin and Fahrenheit as a list

  def lc_2496(self, strs):
        """
        Finds the maximum value from a list strs containing strings and integers.

        Parameters:
            strs (List[str]): A list of strings and integers.

        Returns:
            int: The maximum value found in the list.

        Example :
            Input: strs = ["alic3","bob","3","4","00000"]
            Output: 5
        """

        res=[] # Initialize an empty list to store converted integers or lengths of strings
        for s in strs: # Iterate through each element in the list
            if s.isdigit(): # Check if the element is a digit
                res.append(int(s)) # Convert the digit string to an integer and append it to the result list
            else:
                res.append(len(s)) # If the element is not a digit (i.e., a string), append its length to the result list

        return max(res) # Return the maximum value found in the result list

  def lc_2520(self, num):
        """
        Counts the number of digits in a given integer num that divide the original number num without any remainder.

        Parameters:
            num (int): The input integer.

        Returns:
            int: The count of digits that divide num without any remainder.

        Example:
            Input: num = 121
            Output: 2
        """
        n=num # Store the original number in a variable for reference
        count=0 # Initialize a variable to count the digits that divide num
        while num!=0:# Iterate through each digit of the number
            d=num%10 # Extract the last digit of the number
            if n%d==0: # Check if the original number divided by the digit or not
                count+=1 # If so, increment the count
            num//=10 # Remove the last digit from the number
        return count  # Return the count of digits that divide num

  def lc_2540(self, nums1, nums2):
        """
        Find the smallest common element between two lists.

        Parameters:
            nums1 (List[int]): The first list of integers.
            nums2 (List[int]): The second list of integers.

        Returns:
            int: The smallest common element, or -1 if there are no common elements.

        Example:
            Input: nums1 = [1, 2, 3], nums2 = [2, 4]
            Output: 2
        """
        nums1,nums2=set(nums1),set(nums2) # Convert both lists to sets to remove duplicates and improve lookup efficiency
        common=sorted(list(nums1.intersection(nums2))) # Find the common elements between the two sets
        # If there are no common elements, return -1
        # Otherwise, return the smallest common element
        return -1 if not len(common) else common[0]

  def lc_2544(self, n):
        """
        Calculates the alternating sum of digits of a given integer n.

        Parameters:
            n (int): The input integer.

        Returns:
            int: The alternating sum of digits.

        Example:
            Input: n = 234
            Output: 3
        """

        res=0 # Initialize a variable to store the alternating sum of digits
        n=str(n) # Convert the integer n to a string to easily access its digits
        for i in range(len(n)): # Iterate through each digit of the integer
            if i%2==0: # If the index is even, add the digit to the result
                res+=int(n[i])
            else: # If the index is odd, subtract the digit from the result
                res-=int(n[i])
        return res  # Return the alternating sum of digits

  def lc_2574(self, nums):
        """
        Calculates the absolute difference between the sum of elements to the left and to the right of each element in the list.

        Parameters:
            nums (List[int]): A list of integers.

        Returns:
            List[int]: A list containing the absolute differences for each element in the input list.

        Example:
            Input: nums = [10, 4, 8, 3]
            Output: [15, 1, 11, 22]
        """

        ls=[] # Initialize an empty list 'ls' to store differences.
        a=sum(nums) # Calculate the sum of all elements in the input list 'nums'.
        ls.append(a-nums[0]) # Calculate the difference between the total sum and the first element, then append it to 'ls'.
        for i in range(len(nums)-1): # Iterate through indices of 'nums' except the last one.
            ls.append(ls[i]-nums[i+1]-nums[i]) # Calculate the difference between the next element and the current element, then append it to 'ls'.
        k=[] # Initialize an empty list 'k' to store absolute differences.
        for i in ls: # Iterate through elements in 'ls'.
            k.append(abs(i)) # Append the absolute value of each element to 'k'.
        return k # Return the list of absolute differences.

  def lc_2651(self, arrivalTime: int, delayedTime: int) -> int:
        """
        Calculates the delayed arrival time given the arrival time and the delayed time.
        Parameters:
            arrivalTime (int): The original arrival time (in hours).
            delayedTime (int): The amount of delay (in hours).
        Returns:
            int: The delayed arrival time (in hours), wrapped around 24-hour clock.
        Example :
            Input: arrivalTime = 15, delayedTime = 5
            Output: 20
        """
        # Calculate the delayed arrival time by adding the original arrival time and delayed time
        time=arrivalTime+delayedTime

        # Wrap around the 24-hour clock by taking the modulus of the sum with 24 and return it
        return time%24

  def lc_2652(self, n):
        """
        Computes the sum of multiples of 3, 5, or 7 up to a given number.

        Parameters:
            n (int): The upper limit up to which multiples are considered.

        Returns:
            int: The sum of multiples of 3, 5, or 7 up to but excluding `n`.

        Example:
            Input: n = 10
            Output: 40
        """
        ls=[] # Initialize an empty list 'ls' to store the multiples.
        for num in range(1,n+1):  # Iterate through numbers from 1 up to 'n', inclusive.
            if num%3==0 or num%5==0 or num%7==0: # Check if the current number is a multiple of 3, 5, or 7.
                ls.append(num) # If so, append it to the list of multiples.
        return sum(ls) # Return the sum of all multiples of 3, 5, or 7 up to but excluding 'n'.

  def lc_2769(self, num, t):
        """
        Calculates the maximum achievable value of a number by incrementing it multiple times.

        Increments the given number 'num' by 1 't' times, where 't' is the target number of increments.
        Returns the sum of the incremented number and the target number of increments.

        Parameters:
            num (int): The initial value of the number.
            t (int): The target number of increments.

        Returns:
            int: The maximum achievable value of the number after 't' increments.


        Example :
            Input: num = 4, t = 1
            Output: 6
        """
        i = 1
        while i <= t:
            num += 1
            i += 1

        return num + t

  def lc_2798(self, hours, target):
        """
        Counts the number of employees who met or exceeded the target number of working hours.

        Iterates through the list of working hours for each employee.
        Increments the count for each employee whose working hours meet or exceed the target.
        Returns the total count of employees who met or exceeded the target.

        Parameters:
            hours (List[int]): The list of working hours for each employee.
            target (int): The target number of working hours.

        Returns:
            int: The number of employees who met or exceeded the target number of working hours.

        Example :
            Input: hours = [0,1,2,3,4], target = 2
            Output: 3
        """
        count = 0
        for hour in hours:
            if hour >= target:
                count += 1
        return count

  def lc_2896(self, n, m):
        """
        Calculates the difference between the sum of numbers from 0 to n (inclusive)
        excluding multiples of m and the sum of multiples of m from 0 to n (inclusive).

        Iterates through numbers from 0 to n (inclusive).
        Adds numbers to a list if they are not multiples of m (l1) and to another list if they are multiples of m (l2).
        Returns the difference between the sum of numbers in l1 and the sum of numbers in l2.

        Parameters:
            n (int): The upper limit for generating numbers.
            m (int): The divisor to identify multiples.

        Returns:
            int: The difference between the sum of numbers not divisible by m and the sum of multiples of m
            from 0 to n (inclusive).

        Example :
            Input: n = 10, m = 3
            Output: 19
        """
        l1 = []
        l2 = []
        for i in range(n + 1):
            if i % m != 0:
                l1.append(i)
            else:
                l2.append(i)
        return sum(l1) - sum(l2)

  def lc_2942(self, words, x):
        """
        Finds the indices of words in a list that contain a given substring.

        Iterates through each word in the list of words.
        Checks if the given substring 'x' is contained within each word.
        If the substring is found in a word, adds the index of that word to the result list.
        Returns the list of indices of words containing the given substring.

        Parameters:
            words (List[str]): The list of words.
            x (str): The substring to search for.

        Returns:
            List[int]: A list containing the indices of words in the input list that contain the given substring.

        Example :
            Input: words = ["leet","code"], x = "e"
            Output: [0,1]
        """
        indices = []
        for i in range(len(words)):
            if x in words[i]:
                indices.append(i)
        return indices


print(dir(Solution))