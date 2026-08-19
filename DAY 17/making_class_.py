#Using capital letter in class is known as PascalCase.
#there is also camelCase and snake_case .

class User:
    pass

    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1

user_01 = User("001", "Kunal")
user_02 = User("001","Sonu")

user_01.follow(user_02)
print(user_01.followers)
print(user_01.following)
print(user_02.followers)
print(user_02.following)


