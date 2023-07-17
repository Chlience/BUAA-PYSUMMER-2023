import re

global Data, Data2


def set1(i):
    global Data
    Data = i


def set2(i):
    global Data2
    Data2 = i


def get1():
    global Data
    return Data


def get2():
    global Data2
    return Data2

def get_most_frequent(xx):
    if len(xx) == 0:
        return "未知"
    frequency = {}
    for string in xx:
        frequency[string] = frequency.get(string, 0) + 1
    max_frequency = max(frequency.values())
    most_frequent_strings = [string for string, count in frequency.items() if count == max_frequency]
    return most_frequent_strings[-1]

def is_all_chinese(text):
    pattern = "^[\u4e00-\u9fa5]+$"
    return bool(re.match(pattern, text))

def has_chinese_characters(string):
    pattern = u'[\u4e00-\u9fa5]'
    return re.search(pattern, string) is not None
