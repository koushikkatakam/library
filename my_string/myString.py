class MyString:
  '''This is a class containing string methods'''

  def __init__(self,s):
    assert type(s)==str,"ValueError: string is needed "
    self.s=s

  #length
  def length(self,s):
    '''Get the length of a String.
        Parameters:
          sring - The string to find length
        Returns:
          int: The length of the value in the String.

        Example:
         s='Hello'
         length(s)
         output- 5
    '''
    l=0
    for i in s:
      l+=1
    return l

  #split
  def split_(self,delimiter=' ',max_split=-1):
    '''Split a string into a list of substrings based on a specified separator.
    Parameters:
    - string - The string to be split.
    - delimiter(str, Optional) - Specifies the delimiter character or substring.
      If not provided or set to None, the default is to split at whitespace characters.
    - maxsplit (int, optional): Specifies the maximum number of splits to perform.
      If provided, the string is split at most maxsplit times, and the remaining part of the string
      is returned as the last element of the resulting list. Default is -1, indicating no limit.

    Returns:
      list of str: A list of substrings obtained by splitting the original string based on the specified separator.
    Example:
      s="a,b,c,d,e"
      s.split_(',',2)
      Output - ['a','b','c,d,e']
    '''
    split_list=[]
    n=self.length(delimiter)
    w=''
    j,k=-1,-1
    for i in range(self.length(self.s)):
      if self.s[i:i+n]==delimiter and max_split!=0:
        split_list.append(w)
        w=''
        max_split-=1
        j,k=i,i+n
      if i in range(j,k):
        continue
      else:
        w+=self.s[i]
    split_list.append(w)
    return split_list

  #rsplit
  def r_split(self,sep=" ",max_split=-1):
    '''Split a string into a list of substrings starting from the right based on a specified separator.
  Parameters:
    - input_string (str): The string to be split.
    - separator (str, optional): Specifies the delimiter character or substring.
      If not provided or set to None, the default is to split at whitespace characters.
    - maxsplit (int, optional): Specifies the maximum number of splits to perform.
      If provided, the string is split at most maxsplit times, and the remaining part of the string
      is returned as the first element of the resulting list. Default is -1, indicating no limit.
    Returns:
      list of strings: A list of substrings obtained by splitting the original string based on the specified separator.
    Example:
      s="a,b,c,d,e"
      s.r_split(',',2)
      Output - ['a,b,c','d','e']
  '''
    split_list=[]
    n=self.length(sep)
    w=''
    j=k=-1
    for i in range(self.length(self.s)-1,-1,-1):
      if self.s[i-n+1:i+1]==sep and max_split!=0:
        split_list.insert(0,w)
        w=''
        max_split-=1
        j,k=i,i-n
      if i in range(k+1,j+1):
        continue
      else:
        w=self.s[i]+w
    split_list.insert(0,w)
    return split_list

  #splitlines
  def split_lines(self,keepends=False):
    '''
    Return a list of lines from the input string, breaking at line boundaries.
    Parameters:
    - input_string (str): The string to be split into lines.
    - keepends (bool, optional): If True, line breaks are included in the resulting lines.
      If False (default), line breaks are stripped from the lines.
    Returns:
      list of str: A list of lines obtained by splitting the original string at line boundaries.
    Example:
    - s = "First line\n Second line\n Third line"
      s.split_lines()
      Output - ['First line','Second line','Third line]
    - s.split_lines(keepends=True)
      Output - ['First line\n','Second line\n','Third line\n']
    '''
    lines_list=[]
    sentance=''
    for i in range(self.length(self.s)):
      if self.s[i:i+2]=='\n' or self.s[i]=='\n':
        if keepends==True:
          sentance+='\n'
        lines_list.append(sentance)
        sentance=''
      else:
        sentance+=self.s[i]
    lines_list.append(sentance)
    return lines_list

  #count
  def count_(self,sub,start=0,end=-1):
    '''
    Count the occurrences of a substring in the given string within the specified range.
    Parameters:
    - input_string (str): The string to search for occurrences of the substring.
    - sub (str): The substring to count within the input string.
    - start (int, optional): The starting index for the search. Default is 0.
    - end (int, optional): The ending index for the search. Default is None,
      meaning the search continues to the end of the string.
    Returns:
    - int: The number of occurrences of the substring in the specified range.
    Example:
     s='hello all'
     s.count_('l')
     Output - 4
     s.count('l',3,5)
     Output - 1
    '''
    n=self.length(sub)
    if end==-1:end=self.length(self.s)
    count=0
    for i in range(start,end):
      if sub==self.s[i:i+n]:
        count+=1
    return count

  #find
  def find_(self,sub,start=0,end=-1):
    '''
    Find the index of the first occurrence of a substring in the given string within the specified range.
     Parameters:
    - input_string (str): The string to search for the first occurrence of the substring.
    - sub (str): The substring to find within the input string.
    - start (int, optional): The starting index for the search. Default is 0.
    - end (int, optional): The ending index for the search. Default is None,
      meaning the search continues to the end of the string.
    Returns:
      int: The index of the first occurrence of the substring, or -1 if not found.
    Example:
    s='Hello World'
    s.find_('ll')
    Output - 2
    s.find_('z')
    Output - -1
    '''
    n=self.length(sub)
    if end==-1:end=self.length(self.s)
    for i in range(start,end):
      if sub==self.s[i:i+n]:
        return i
    else:
      return -1

  #rfind
  def rfind_(self,sub,start=0,end=-1):
    '''
    Find the index of the last occurrence of a substring in the given string within the specified range.
    Parameters:
    - input_string (str): The string to search for the last occurrence of the substring.
    - sub (str): The substring to find within the input string.
    - start (int, optional): The starting index for the search. Default is 0.
    - end (int, optional): The ending index for the search. Default is None,
      meaning the search continues to the end of the string.
    Returns:
      int: The index of the last occurrence of the substring, or -1 if not found.
    Example:
      s='Hello World'
      s.rfind_('l')
      output - 9
      s.rfind_('z')
      Output - -1
    '''
    n=self.length(sub)
    if end==-1:end=self.length(self.s)
    for i in range(end-1,start-1,-1):
      if sub==self.s[i:i+n]:
        return i
    else:
      return -1

  # index
  def index_(self,sub,start=0,end=-1):
    '''
    Find the index of the first occurrence of a substring in the given string within the specified range.
    Parameters:
    - input_string (str): The string to search for the first occurrence of the substring.
    - sub (str): The substring to find within the input string.
    - start (int, optional): The starting index for the search. Default is 0.
    - end (int, optional): The ending index for the search. Default is None,
      meaning the search continues to the end of the string.
    Returns:
      int: The index of the first occurrence of the substring.
    Raises:
      ValueError: If the substring is not found in the specified range.
    Example:
      s='Hello World'
      s.index_('e')
      output-1
      s.index_('z')
      output- "ValueError: substring not found "
    '''
    n=self.length(sub)
    if end==-1:end=self.length(self.s)
    indx=-1
    for i in range(start,end):
      if sub == self.s[i:i+n]:
        indx=i
        break
    assert indx != -1, 'ValueError: substring not found '
    return indx

  #rindex
  def rindex_(self,sub,start=0,end=-1):
    '''
    Find the index of the last occurrence of a substring in the given string within the specified range.
    Parameters:
    - input_string (str): The string to search for the last occurrence of the substring.
    - sub (str): The substring to find within the input string.
    - start (int, optional): The starting index for the search. Default is 0.
    - end (int, optional): The ending index for the search. Default is None,
      meaning the search continues to the end of the string.
    Returns:
      int: The index of the last occurrence of the substring.
    Raises:
      ValueError: If the substring is not found in the specified range.
    Example:
      Example:
      s='Hello World'
      s.index_('o')
      output-7
      s.index_('z')
      output- "ValueError: substring not found "
    '''
    n=self.length(sub)
    if end==-1:end=self.length(self.s)
    indx=-1
    for i in range(end-1,start-1,-1):
      if sub == self.s[i:i+n]:
        indx=i
        break
    assert indx != -1, 'ValueError: substring not found '
    return indx

  #upper
  def upper_(self):
    '''
    Convert all lowercase characters in the given string to uppercase.
    Parameters:
    - input_string (str): The string to convert to uppercase.
    Returns:
      str: A new string with all lowercase characters converted to uppercase.
    Example:
      s='Hello World @123'
      s.upper_()
      Output - HELLO WORLD @123
    '''
    s_upper=''
    for i in self.s:
      if ord(i) in range(97,123):
        s_upper+=chr(ord(i)-32)
      else:
        s_upper+=i
    return s_upper

  #lower
  def lower_(self):
    '''
    Convert all uppercase characters in the given string to lowercase.
    Parameters:
    - input_string (str): The string to convert to lowercase.
    Returns:
      str: A new string with all uppercase characters converted to lowercase.
    Example:
      s='Hello World @123'
      s.upper_()
      Output - hello world @123
    '''
    s_lower=''
    for i in self.s:
      if ord(i) in range(65,91):
        s_lower+=chr(ord(i)+32)
      else:
        s_lower+=i
    return s_lower
  #swap_case
  def swap_case(self):
    '''
    Swap the case of each character in the given string.
    Parameters:
    - input_string (str): The string to swap the case.
    Returns:
      str: A new string with uppercase characters converted to lowercase
         and lowercase characters converted to uppercase.
    Example:
      s='HeLLo WorLd @123'
      s.upper_()
      Output - hEllO wORlD @123
    '''
    s_swap=''
    for i in self.s:
      if ord(i) in range(97,123):
        s_swap+=chr(ord(i)-32)
      elif ord(i) in range(65,91):
        s_swap+=chr(ord(i)+32)
      else:
        s_swap+=i
    return s_swap

  #title
  def title_(self):
    '''
    Return a titlecased version of the given string.
    The titlecased version of a string is where the first character of each word is
    capitalized and the rest of the characters are lowercase.

    Parameters:
    - input_string (str): The string to be titlecased.
    Returns:
      str: A new string with the first character of each word capitalized.
    Example:
      s='hello @123welcome'
      s.title_()
      output - Hello @123Welcome
    '''
    s=[]
    str_list=self.split_(self.s)
    for word in str_list:
      w=''
      c=0
      for i in word:
        if ord(i) in range(97,123) and c==0:
          w+=chr(ord(i)-32)
          c+=1
        elif (ord(i) in range(65,91)) and c==0:
          w+=i
          c+=1
        elif ord(i) in range(65,91):
          w+=chr(ord(i)+32)
        else:
          w+=i
      s.append(w)
    z=' '.join(s)
    return z

  #capitalize
  def capitalize_(self):
    '''
    Return a copy of the given string with its first character capitalized and the rest lowercase.
    Parameters:
    - input_string (str): The string to be capitalized.
    Returns:
      str: A new string with the first character capitalized and the rest in lowercase.
    Example:
      s= 'HELLO WorLd'
      s.capitalize()
      output- Hello world
    '''
    s_capital=''
    c=0
    for i in self.s:
      if ord(i) in range(97,123) and c==0:
        s_capital+=chr(ord(i)-32)
        c+=1
      elif (ord(i) in range(65,91) and c==0) or (ord(i) in range(48,58)):
        s_capital+=i
        c+=1
      elif ord(i) in range(65,91):
        s_capital+=chr(ord(i)+32)
        c+=1
      else:
        s_capital+=i
    return s_capital

   #isascii
  def is_ascii(self):
    """
    Check if all characters in the given string are ASCII characters.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are ASCII, False otherwise.
    Example:
      s='hello'
      s.is_ascii()
      output - True
    """
    for i in self.s:
      if ord(i) not in range(0,128):
        return False
    else:
      return True

  #isalpha
  def is_alpha(self):
    """
    Check if all characters in the given string are alphabetic (letters).
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are alphabetic, False otherwise.
    Example:
      s='hello'
      s.is_alpha()
      output - True
      s='Hello World
      s.is_alpha()
      output - False
    """
    for i in self.s:
      if ord(i) not in range(65,91) and ord(i) not in range(97,123):
        return False
    else:
      return True

  #isalnum
  def is_alnum(self):
    '''
    Check if all characters in the given string are alphabetic (letters).
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are alphabetic, False otherwise.
    Example:
      s='Hello123'
      s.is_alnum()
      output - True
      s='Hello 123'
      s.is_alnum()
      output - False
    '''
    for i in self.s:
      if ord(i) not in range(65,91) and ord(i) not in range(97,123) and ord(i) not in range(48,58):
        return False
    else:
      return True

  #islower
  def is_lower(self):
    '''
    Check if all characters in the given string are lowercase.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are lowercase, False otherwise.
    Example:
      s='hello all'
      s.is_lower()
      output - True
      s='Hello all'
      s.is_lower()
      output - False
    '''
    for i in self.s:
      if ord(i) in range(65,91):
        return False
    else:
      return True

  # isupper
  def is_upper(self):
    '''
    Check if all characters in the given string are uppercase.
    Parameters:
    - input_string (str): The string to check.
    Returns:
    bool: True if all characters are uppercase, False otherwise.
    Example:
      s='HELLO ALL'
      s.is_upper()
      output - True
      s='HELLO All'
      s.is_upper()
      output - False
    '''
    for i in self.s:
        if ord(i) in range(97,123):
          return False
    else:
      return True

  #istitle
  def is_title(self):
    '''
      Check if the given string is titlecased.
    A string is considered titlecased if it consists of words separated by spaces,
    and each word starts with an uppercase character, followed by lowercase characters.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if the string is titlecased, False otherwise.
    Example:
      s='Hello All'
      s.is_title()
      output - True
      s='Hello ALL'
      s.is_title()
      output - False
    '''
    s=self.split_(self.s)
    for word in s:
      c=0
      for i in word:
        if ord(i) in range(65,91) and c==0:
          c+=1
        elif (ord(i) in range(97,123) and c==0) or ord(i) in range(65,91):
          return False
    else:
      return True

  #isdigit
  def is_digit(self):
    '''
    Check if all characters in the given string are digits.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are digits, False otherwise.
    Example:
      s='1234567'
      s.is_digit()
      output - True
      s='123 456'
      s.is_digit()
      output - False
    '''
    for i in self.s:
      if ord(i) not in range(48,58):
        return False
    else:
      return True

  #isdecimal
  def is_decimal(self):
    '''
      Check if all characters in the given string are decimal characters.
    Decimal characters are those that can be used to represent numbers in base 10.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are decimal, False otherwise.
    Example:
      s='123'
      s.is_decimal()
      output - True
      s='12.56'
      s.is_decimal()
      output - False
    '''
    for i in self.s:
      if ord(i)not in range(48,58):
        return False
    else:
      return True

  #isnumeric
  def is_numeric(self):
    '''
    Check if all characters in the given string are numeric characters.
    Numeric characters include digits, numeric characters from other scripts,
    and characters that represent numeric values (like fractions).
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are numeric, False otherwise.
    Example:
      s='2345'
      s.is_numeric()
      output - True
      s='12abc'
      s.is_numeric()
      output - False
    '''
    for i in self.s:
      if ord(i) not in range(48,58):
        return False
    else:
      return True

  #isspace
  def is_space(self):
    '''
    Check if all characters in the given string are whitespace characters.
    Whitespace characters include spaces, tabs, and newline characters.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are whitespace, False otherwise.
    Example:
      s='   '
      s.is_space()
      output - True
      s=' \n '
      s.is_space()
      output - True
    '''
    for i in range(self.length(self.s)):
      if self.s[i] != ' ' and self.s[i:i+2]!="\n" and self.s[i:i+2]!="\t" and self.s[i:i+2]!="\r" and self.s[i:i+2]!='\f':
        return False
    else:
      return True

  #startswith
  def starts_with(self,prefix,start=0,end=None):
    '''
    Check if the given string starts with a specified prefix.
    Parameters:
    - input_string (str): The string to check.
    - prefix (str): The prefix to check for at the beginning of the string.
    - start (int, optional): The starting index for the check. Default is 0.
    - end (int, optional): The ending index for the check. Default is None,
      meaning the check continues to the end of the string.
    Returns:
      bool: True if the string starts with the specified prefix, False otherwise.
    Example
      s='Hello World'
      s.starts_with('Hello')
      output - True
    '''
    if end==None : end=self.length(self.s)
    n=self.length(prefix)
    for i in range(start,end):
      if i+n>end:
        return False
      elif prefix == self.s[i:i+n]:
        return True
      else:
        return False


  #endswith
  def ends_with(self,suffix,start=0,end=None):
    '''
    Check if the given string ends with a specified suffix.
    Parameters:
    - input_string (str): The string to check.
    - suffix (str): The suffix to check for at the end of the string.
    - start (int, optional): The starting index for the check. Default is 0.
    - end (int, optional): The ending index for the check. Default is None,
      meaning the check continues to the end of the string.
    Returns:
      bool: True if the string ends with the specified suffix, False otherwise.
    Example:
      s="Hello World"
      s.ends_with('d')
      output - True
    '''
    if end==None:end=self.length(self.s)
    n=self.length(suffix)
    for i in range(end,start-1,-1):
      if i-n<start:
        return False
      elif suffix == self.s[i-n:i]:
        return True
      else:
        return False

  #partition
  def partition_(self,sep):
    '''
    Partition the given string into three parts based on the first occurrence of a separator.
    Parameters:
    - input_string (str): The string to be partitioned.
    - separator (str): The separator used to split the string.
    Returns:
      tuple: A tuple containing three parts of the string: the text before the separator,
           the separator itself, and the text after the separator.
    Example:
      s='Hello World'
      s.partition('l')
      output - ('Hel','l','o World')
    '''
    str_list=[]
    w=''
    n=self.length(sep)
    c=0
    j,k=-1,-1
    for i in range(self.length(self.s)):
      if self.s[i:i+n] == sep and c==0:
        str_list.extend((w,sep))
        w=''
        c+=1
        j,k=i,i+n
      elif i in range(j,k):
        continue
      else:
        w+=self.s[i]
    str_list.append(w)
    if len(str_list)==3:
      return tuple(str_list)
    elif len(str_list)==2:
      str_list.append('')
      return tuple(str_list)
    else:
      str_list.extend(['',''])
      return tuple(str_list)

  #rpartition
  def r_partition(self,sep):
    '''
    Partition the given string into three parts based on the last occurrence of a separator.
    Parameters:
    - input_string (str): The string to be partitioned.
    - separator (str): The separator used to split the string.
    Returns:
      tuple: A tuple containing three parts of the string: the text before the last separator,
           the last separator itself, and the text after the last separator.
    Example
      s='abcdedcba'
      s.r_partition('c')
      output - ('abcded','c','ba)
    '''
    str_list=[]
    w=''
    n=self.length(sep)
    c=0
    j,k=0,0
    for i in range(self.length(self.s)-1,-1,-1):
      if self.s[i-n+1:i+1] == sep and c==0:
        str_list.extend((sep,w))
        w=''
        c+=1
        j,k=i,i-n
      elif i in range(k+1,j+1):
        continue
      else:
        w=self.s[i]+w
    str_list.insert(0,w)
    if len(str_list)==3:
      return tuple(str_list)
    elif len(str_list)==2:
      str_list.insert(0,'')
      return tuple(str_list)
    else:
      new_list=('','',w)
      return new_list

  #replace
  def replace_(self,old,new,count=-1):
    '''
    Replace occurrences of a specified substring with another substring in the given string.
    Parameters:
    - input_string (str): The string in which replacements will be performed.
    - old_str (str): The substring to be replaced.
    - new_str (str): The substring to replace occurrences of `old_str`.
    - count (int, optional): Maximum number of occurrences to replace. Default is -1,
      meaning all occurrences will be replaced.
    Returns:
      str: A new string with replacements.
    Example:
      s='Python Programming Language'
      s.replace('ng',z)
      output - Python Programmiz Lazuage
   '''
    r_string=''
    n=self.length(old)
    j,k=-1,-1
    for i in range(self.length(self.s)):
      if self.s[i:i+n]==old and count!=0:
        r_string+=new
        count-=1
        j,k=i,i+n
      elif i in range(j,k):
        continue
      else:
        r_string+=self.s[i]
    return r_string

  #center
  def center_(self,width,fillchar=' '):
    '''
    Return a centered string within a specified width.
    Parameters:
    - input_string (str): The string to be centered.
    - width (int): The total width of the resulting string.
    - fillchar (str, optional): The character used for filling the spaces around the string.
      Default is a space (' ').
    Returns:
      str: A new string centered within the specified width.
    Example:
      s='Hello'
      s.center_(10,'*')
      output - **Hello***
    '''
    str_len=self.length(self.s)
    n=width-str_len
    str_center=fillchar*(n//2)+self.s+fillchar*(n-n//2)
    return str_center

  #ljust
  def l_just(self,width,fillchar=' '):
    '''
    Return a left-justified string within a specified width.
    Parameters:
    - input_string (str): The string to be left-justified.
    - width (int): The total width of the resulting string.
    - fillchar (str, optional): The character used for filling the spaces to the right of the string.
      Default is a space (' ').
    Returns:
      str: A new string left-justified within the specified width.
    Example:
      s='Hello'
      s.l_just(10,'*')
      output - Hello*****
    '''
    str_len=self.length(self.s)
    n=width-str_len
    str_left=self.s+fillchar*n
    return str_left

  #rjust
  def r_just(self,width,fillchar=' '):
    '''
    Return a right-justified string within a specified width.
    Parameters:
    - input_string (str): The string to be right-justified.
    - width (int): The total width of the resulting string.
    - fillchar (str, optional): The character used for filling the spaces to the left of the string.
      Default is a space (' ').
    Returns:
      str: A new string right-justified within the specified width.
    Example:
      s='Hello'
      s.r_just(10,'*')
      output - *****Hello
    '''
    str_len=self.length(self.s)
    n=width-str_len
    str_right=fillchar*n+self.s
    return str_right

  #Casefold
  def case_fold(self):
    '''
    Return a casefolded version of the given string.
        Casefolding is similar to lowercase conversion but more aggressive, removing
    all case distinctions from the string. It is suitable for case-insensitive
    comparisons.
    Parameters:
    - input_string (str): The string to be casefolded.
    Returns:
      str: A new string with all case distinctions removed.
    Example:
      s= 'HELLO World'
      s.case_fold()
      output - hello world
    '''
    y=""
    for char in self.s:
      if ord(char) in range(65,91):
        y+=chr(ord(char)+32)
      else:
        y+=char
    return y

  #removeprefix:
  def remove_prefix(self,prefix):
    '''
    Remove a specified prefix from the given string.
    Parameters:
    - input_string (str): The string from which the prefix will be removed.
    - prefix (str): The prefix to be removed.
    Returns:
      str: A new string with the specified prefix removed.
    Example:
      s='@@@@Hello'
      s.remove_prefix('@@@@')
      output - Hello
    '''
    length=self.length(prefix)
    if self.s[:length]==prefix:
      return self.s[length:]
    else:
      return self.s

  #removesuffix:
  def remove_suffix(self,suffix):
    '''
    Remove a specified suffix from the given string.
    Parameters:
    - input_string (str): The string from which the suffix will be removed.
    - suffix (str): The suffix to be removed.
    Returns:
      str: A new string with the specified suffix removed.
    Example:
      s='Hello###'
      s.remove_suffix("###")
      output - Hello
    '''
    length=self.length(suffix)
    if self.s[-length:]==suffix:
      return self.s[:len(self.s)-length]
    else:
      return self.s

  #zfill
  def z_fill(self,width):
    '''
    Pad the given string with zeros on the left to achieve a specified width.
    Parameters:
    - input_string (str): The string to be padded.
    - width (int): The minimum width of the resulting string.
    Returns:
      str: A new string padded with zeros on the left.
    Example:
      s='234'
      s.z_fill(6)
      output - '00234'
    '''
    str_len=self.length(self.s)
    n=width-str_len
    new_str='0'*n+self.s
    return new_str

  #join
  def join_(self,iter,sep=''):
    '''
    Concatenate the elements of an iterable with a specified separator.
    Parameters:
    - iterable (iterable): An iterable containing elements to be joined.
    - separator (str): The string used to join the elements.
    Returns:
      str: A new string created by concatenating the elements with the specified separator.
    Example:
      s='abcde'
      join_(s,'-')
      output - a-b-c-d

      join(['1', '2', '3', '4', '5'],'-')
      output- 1-2-3-4-5

    '''
    s=''
    for i in range(self.length(iter)):
      if i==self.length(iter)-1:
        s+=iter[i]
        break
      s+=iter[i]+sep
    return s

  #strip
  def strip_(self,char=' '):
    '''
    Return a copy of the given string with leading and trailing characters removed.
    Parameters:
    - input_string (str): The string to be stripped.
    - chars (str, optional): A string specifying the set of characters to be removed.
      If not provided, whitespaces are removed.
    Returns:
      str: A new string with leading and trailing characters removed.
    Example:
      s='    hello    '
      s.strip_()
      output - 'hello'
    '''
    new_str=''
    start=-1
    end=self.length(self.s)
    for i in range(self.length(self.s)):
      if self.s[i] in char:
        start=i
        continue
      else:
        break
    for i in range(self.length(self.s)-1,-1,-1):
      if self.s[i] in char:
        end=i
        continue
      else:
        break
    new_str=self.s[start+1:end:]
    return new_str

  #lstrip
  def l_strip(self,char=' '):
    '''
    Return a copy of the given string with leading characters removed.
    Parameters:
    - input_string (str): The string to be left-stripped.
    - chars (str, optional): A string specifying the set of characters to be removed.
      If not provided, whitespaces are removed.
    Returns:
      str: A new string with leading characters removed.
    Example:
      s='    Hello   '
      s.l_strip()
      output - 'Hello   '
    '''
    new_str=''
    start=-1
    end=self.length(self.s)
    for i in range(self.length(self.s)):
      if self.s[i] in char:
        start=i
        continue
      else:
        break
    new_str=self.s[start+1:end:]
    return new_str

  #rstrip
  def r_strip(self,char=' '):
    '''
    Return a copy of the given string with trailing characters removed.
    Parameters:
    - input_string (str): The string to be right-stripped.
    - chars (str, optional): A string specifying the set of characters to be removed.
      If not provided, whitespaces are removed.
    Returns:
      str: A new string with trailing characters removed.
    Example:
      s='   Hello   '
      s.r_strip()
      output-'   Hello'
    '''
    new_str=''
    start=-1
    end=self.length(self.s)
    for i in range(self.length(self.s)-1,-1,-1):
      if self.s[i] in char:
        end=i
        continue
      else:
        break
    new_str=self.s[start+1:end:]
    return new_str

  #isprintable
  def is_printable(self):
    '''
   Check if all characters in the given string are printable.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if all characters are printable, False otherwise.
    Example:
      s='Hello World'
      s.is_printable()
      output-True
      s="Hello \n World"
      s.is_printable()
      output-False
    '''
    pList='''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ '''
    for i in self.s:
      if i not in pList:
        return False
    else:
      return True

  #isidentifier
  def is_identifier(self):
    '''
    Check if the given string is a valid identifier.
      An identifier in Python is a sequence of letters, digits, and underscores,
    starting with a letter or an underscore. It cannot be a reserved word.
    Parameters:
    - input_string (str): The string to check.
    Returns:
      bool: True if the string is a valid identifier, False otherwise.
    Example:
      'number1'.is_identifier() -- True
      '1number'.is_identifier() -- False
    '''
    id_list='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
    if ord(self.s[0]) in range(48,58):
      return False
    else:
      for i in self.s:
        if i not in id_list:
          return False
      else:
        return True

  #maketrans
  def make_trans(self,from_chars,to_chars,delete_chars=''):
    '''
    Create a translation table for use with the translate() method.
    Parameters:
    - from_chars (str): A string containing characters to be replaced.
    - to_chars (str): A string containing corresponding replacement characters.
    - delete_chars (str, optional): A string containing characters to be deleted.
      Default is an empty string.
    Returns:
      dict: A translation table mapping each character in from_chars to the
          corresponding character in to_chars, and deleting characters in delete_chars.
    Example:
      from_chars='abcd'
      to_chars='wxyz'
      make_trans(from_chars,to_chars)
      output- {97: 119, 98: 120, 99: 121, 100: 122}
    '''
    assert self.length(from_chars)==self.length(to_chars),"'ValueError': the first two maketrans arguments must have equal length"
    dic={}
    for i in range(self.length(from_chars)):
      dic[ord(from_chars[i])]=ord(to_chars[i])
    for i in delete_chars:
      dic[ord(i)]=None
    return dic

  #translate
  def translate_(self,dic):
    '''
    Translate the characters in the given string using a translation table.
    Parameters:
    - input_string (str): The string to be translated.
    - translation_table (dict): A translation table created by the maketrans() function.
    Returns:
      str: A new string with characters translated based on the provided table.
    Example:
      s='a boy with car'
      dic={97: 119, 98: 120, 99: 121, 100: 122}
      output- 'w xoy with yar'
    '''
    str_trans=''
    for i in self.s:
      if ord(i) in dic:
        if dic[ord(i)] == None:
          continue
        str_trans+=chr(dic[ord(i)])
      else:
        str_trans+=i
    return str_trans

  #contains
  def __contains__(self,value):
    '''
    Check if the given substring is present in the CustomString instance.
      Parameters:
      - substring (str): The substring to check for.
      Returns:
        bool: True if the substring is present, False otherwise.
      Example:
        s='HEllo WOrld'
        'o' in s --> True
        'h' in s --> False
    '''
    return value in self.s

  #concat
  def __add__(self,other):
    '''
    Concatenate the value of two CustomString instances.
      Parameters:
      - other (CustomString or str): The object to be concatenated.
      Returns:
        CustomString: A new CustomString instance with the concatenated value.
      Example:
        str1='Hello'
        str2='World'
        str1 +str2
        Output - 'Hello World'
    '''
    if isinstance(other,MyString):
      return self.s+other.s
    else:
      return "Error"

  #multiply
  def __mul__(self,n):
    '''
    Repeat the value of the CustomString instance a specified number of times.
      Parameters:
      - n (int): The number of times to repeat the value.
      Returns:
        CustomString: A new CustomString instance with the repeated value.
      Example:
        s='Holla'
        s * 3
        output - 'HollaHollaHolla'
    '''
    if isinstance(n,int):
      return self.s*n
    else:
      return 'Error'


   #in
  def __eq__(self,other):
    '''
    Check if the value of two CustomString instances is equal.
      Parameters:
      - other (CustomString or any): The object to compare for equality.
      Returns:
        bool: True if the values are equal, False otherwise.
      Example :
        str1='hello'
        str2='hello'
        str3='Hello'
        str1==str2 ---> True
        str1==str3 ---> False
    '''
    assert self.length(self.s) == self.length(other.s), False
    for i,j in zip(self.s,other.s):
      if i==j:
        continue
      else:
        return False
    else:
      return True