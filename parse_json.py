import json
import os
from users import User
from check_regex import email_user_check, user_name_check, extract_year, extract_month, extract_day


class ParseJson:
    """
    This class helps to read json file and create a user object come from users.py
    """
    def __init__(self, json_file):
        """
        For this method, all that needs to be done is to store the json_file parameter value
        into  a self.json_file variable
        :param json_file: json_file as json type
        :return use it in the readJson() method in order to read
        """
        self.json_file = json_file

    def readJson(self):
        """
        Convert from Json to Python
        :return: users list from json file
        """
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r', encoding='utf-8') as file:
                json_list = json.load(file)
        return json_list

    def get_list(self):
        """
        This method helps to extract user information from list
        :return: user object as a list type
        """
        users_list = self.readJson()
        liste = []
        for user in users_list:
            user_id = user["id"]
            email = user["email"]
            user_name = user["username"]
            name = user["profile"]["name"]
            emailuserlk = email_user_check(email, user_name)
            usernamelk = user_name_check(user_name, name)
            year = extract_year(user["profile"]["dob"])
            month = extract_month(user["profile"]["dob"])
            day = extract_day(user["profile"]["dob"])
            city = user["profile"]["address"].split()[-1]
            ap = 1
            user_obj = User(user_id, email, user_name, name, emailuserlk, usernamelk, year, month, day, city, ap)
            liste.append(user_obj)
        return liste



