import re

name = ''


def get_most_frequent(xx):
    if len(xx) == 0:
        return "未知"
    frequency = {}
    for string in xx:
        frequency[string] = frequency.get(string, 0) + 1
    max_frequency = max(frequency.values())
    most_frequent_strings = [string for string, count in frequency.items() if count == max_frequency]
    return most_frequent_strings[-1]


dic_canting_time = {'学二': '：\n7:00~20:00', '合一': '：\n7:00~21:00', '新北': '：\n7:00~23:00', 'Wings': '：\n7:00~22:00',
                    '美食苑': '：\n10:00~1:00'}

dic_canting_position = {'学二': '：\n校园东路与\n校园南路口', '合一': '：\n校园西路与\n校园南路口',
                        '新北': '：\n校园西路与\n校园北路口', 'Wings': '：\n新主楼旁/\n主楼五层/\n二教南/\n新北地下',
                        '美食苑': '：\n校园南路南端'}


def is_all_chinese(text):
    pattern = "^[\u4e00-\u9fa5]+$"
    return bool(re.match(pattern, text))


def has_chinese_characters(string):
    pattern = u'[\u4e00-\u9fa5]'
    return re.search(pattern, string) is not None


sett = {"合一", "学二", "新北", "美食苑", "Wings"}
arr = {7: "豆类", 5: "蔬菜", 1: "主食", 8: "鸡肉", 4: "猪肉", 3: "蛋类", 9: "鱼肉", 6: "牛肉",
       2: "西餐", 10: "饮料", 11: "咖啡", 12: '甜品'}
