class UserInfo:
    def __init__(self, UserID, UserName):
        self.UserID = UserID
        self.UserName = UserName

    def __str__(self):
        return f"{self.UserID}:{self.UserName}"

class UserFactory:
    _id = 0

    @staticmethod
    def create_user(UserName):
        UserFactory._id += 1

        return UserInfo(UserFactory._id, UserName)

if __name__ == "__main__":
    user1 = UserFactory.create_user("Alice")
    user2 = UserFactory.create_user("Bob")
    print(user1)
    print(user2)

