import re

def equals_abc(string):
    if re.fullmatch("abc",string):
        return True

    return False

def equals_multiple_a(string):
    if re.fullmatch("a+",string):
        return True
    return False;

def equals_multi_abc(string):
    re.fullmatch("abc(abc)+",string)



def main():
    print(equals_abc("abc"))
    print(equals_multiple_a("a"))
    print(equals_multiple_a("aa"));
    print(equals_multiple_a("bbb"))


if __name__=="__main__":
    main()