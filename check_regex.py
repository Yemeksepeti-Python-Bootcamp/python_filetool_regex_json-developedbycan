import re


def email_user_check(email="", username=""):
    """
    It helps to check that does the users' email contain at least 3 letters from part of the username
    email = simon_newton@undefined.gmx
    username = Simon Newton
    It will create a pattern like according the email and username already mentioned;
    pattern = [sim|simo|simon|simonn|simonne|simonnew|...]
    :param email: email
    :param username: username
    :return: 1 or 0
    """
    pattern = ""
    email = email.lower().split("@")[0]
    username = username.lower()
    for index, harf in enumerate(username):
        if index > 2:
            pattern += username[:index] + '|'

    if re.findall(pattern, email):
        return 1
    else:
        return 0


def user_name_check(user_name="", full_name=""):
    """
    This function helps to check that does user_name contain part of the user's first and last name
    :param user_name: user name => str
    :param full_name: full name => str
    :return: 1 or 0
    """
    pattern = ""
    user_name = user_name.lower()
    full_name = full_name.lower().replace(" ", "")

    for index, harf in enumerate(full_name):
        if index > 0:
            pattern += full_name[:index] + "|"

    if re.findall(pattern[:-1], user_name):
        return 1
    else:
        return 0


def extract_year(dob):
    """
    Extract year from date of birth
    :param dob: date of birth as a str like: "1992-03-26"
    :return: year 1992
    """
    yil = re.search(r'(\d{4})-(\d{2})-(\d{2})', dob)
    if yil:
        return yil.group(1)


def extract_month(dob):
    """
    Extract month from date of birth
    :param dob: date of birth as a str like: "1992-03-26"
    :return: month as str 03
    """
    yil = re.search(r'(\d{4})-(\d{2})-(\d{2})', dob)
    if yil:
        return yil.group(2)


def extract_day(dob):
    """
    Extract day from date of birth
    :param dob: date of birth as a str like: "1992-03-26"
    :return: day as a str 26
    """
    yil = re.search(r'(\d{4})-(\d{2})-(\d{2})', dob)
    if yil:
        return yil.group(3)


