import string


# 用户名只能由数字,字母,下划线组成
# 5-18 个字符
# 首字符不能是下划线
def username_check(username: str):
    fonts = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + ['_']
    if not (5 <= len(username) <= 18):
        return False
    if username[0] == '_':
        return False
    for c in username:
        if c not in fonts:
            return False
    return True


def username_error_message():
    return "* The username can only consist of numbers, letters, and underscores.\n"\
        + "* 5-18 characters.\n"\
        + "* The first character cannot be an underscore."


# 密码只能由数字,字母以及特殊字符 "()`!@#$%^&*_-+=|{}[]:;'<>,.?" 组成
# 8-30 个字符
def password_check(password: str):
    print(password)
    fonts = list(string.ascii_lowercase)\
            + list(string.ascii_uppercase)\
            + list(string.digits)\
            + list(r"()`!@#$%^&*_-+=|{}[]:;'<>,.?")
    for c in password:
        if c not in fonts:
            return False
    return 5 <= len(password) <= 18


def password_error_message():
    return "* The password can only consist of numbers, letters, and special characters: "\
        + r"()`!@#$%^&*_-+=|{}[]:;'<>,.?" + "\n"\
        + "* 8-30 characters."
