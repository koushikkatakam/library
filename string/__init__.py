import myString
if __name__ == '__main__':
    s = "The quick brown fox jumps over the lazy dog."
    # Creating object for MyString class and passing a string
    strObj = myString.MyString(s)
    
    l = strObj.length(s)
    print("Length of string is :", l)
    c = strObj.count_('a')
    print("Count of 'a':", c)
    f = strObj.find_('l')
    print("Find of 'l' :", f)
    rf = strObj.rfind_('r')
    print("Right Find of 'r' :", rf)
    i = strObj.index_('i')
    print("Index of 'i' :", i)
    ri = strObj.rindex_('a')
    print("Right index of 'a' :",ri)
    
    lis = strObj.split_()
    print("Split :",lis)
    rlis = strObj.r_split()
    print("rsplit :", rlis)
    lines = strObj.split_lines()
    print("Split lines :", lines)
    res = strObj.join_(lis)
    print("Join :",res)
    
    u = strObj.upper_()
    print("Uppercase :", u)
    l = strObj.lower_()
    print("Lowercase :",l)
    sc = strObj.swap_case()
    print("Swapcase :",sc)
    t = strObj.title_()
    print("Title :",t)
    c = strObj.capitalize_()
    print("Capitalize :",c)
    cf = strObj.case_fold()
    print("Casefold :",cf)
    
    asci = strObj.is_ascii()
    print("Is ascii :",asci)
    alpha = strObj.is_alpha()
    print("Is alpha :",alpha)
    alnum = strObj.is_alnum()
    print("Alnum :",alnum)
    decimal = strObj.is_decimal()
    print("Is decimal :",decimal)
    digit = strObj.is_digit()
    print("Is digit :",digit)
    numeric = strObj.is_numeric()
    print("Is numeric :",numeric)
    identifier = strObj.is_identifier()
    print("Is identifier :",identifier)
    upper_ = strObj.is_upper()
    print("Is upper :",upper_)
    lower_ = strObj.is_lower()
    print("IS lower :",lower_)
    title_ = strObj.is_title()
    print("Is title :",title_)
    space = strObj.is_space()
    print("Is space :",space)
    printable = strObj.is_printable()
    print("Is printable :",printable)
    
    sw = strObj.starts_with('I')
    print("Starts with :",sw)
    ew = strObj.ends_with('e')
    print("Ends with :", ew)

    parts = strObj.partition_('i')
    print("Partition :", parts)
    rparts = strObj.r_partition(' ')
    print("R partition :",rparts)
    rep = strObj.replace_('o','e')
    print("Replace :",rep)
    
    c = strObj.center_(20)
    print("Center :",c)
    lj = strObj.l_just(20)
    print("Left just :",lj)
    rj = strObj.r_just(20)
    print("Right just :",rj)
    zf = strObj.z_fill(10)
    print("Zfill :",zf)
    
    prefix = strObj.remove_prefix('@')
    print("Remove prefix :", prefix)
    suffix = strObj.remove_suffix('*')
    print("Remove suffix",suffix)
    strp = strObj.strip_()
    print("Strip :",strp)
    lstrp = strObj.l_strip()
    print("Left strip :",lstrp)
    rstrp = strObj.r_strip()
    print("Right strip :",rstrp)
    
    dic = strObj.make_trans('abcd','wxyz')
    print("Make transe :",dic)
    trans = strObj.translate_(dic)
    print("Translate :",trans)
    
    str2=myString.MyString(s)
    print("Contains :",'a' in strObj)
    print("Concat :",strObj + str2)
    print("Multiply :",strObj * 3)
    print("Equal :",strObj == str2)