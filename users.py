class User:
    def __init__(self, user_id, email, user_name,
                 name, emailuserlk=1, usernamelk=1,
                 year=1992, month=3, day=26, city=" ", ap=1):
        self.user_id = user_id
        self.email = email
        self.user_name = user_name
        self.name = name
        self.emailuserlk = emailuserlk
        self.usernamelk = usernamelk
        self.year = year
        self.month = month
        self.day = day
        self.city = city
        self.ap = ap


