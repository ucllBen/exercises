import re

def one_or_more_abc(string):
    re.fullmatch("(abc)+",string)