import copy

class Services:
    def __init__(self, servicename, ptice):
        self.servicename = servicename
        self.ptice = ptice
    def __str__(self):
        return f"{self.servicename}: {self.ptice}"

class User:
    def __init__(self, name, services):
        self.name = name
        self.services = services

    def __str__(self):
        return f"{self.name}: {self.services}"

class UserFactory:
    ubuntu_server = User("", Services("ubuntu-server", 1))
    windows_server = User("", Services("windows-server", 2))

    @staticmethod
    def __create_services(prototype, name):
        result = copy.deepcopy(prototype)
        result.name = name
        return result

    @staticmethod
    def create_ubuntu_server(name):
        return UserFactory.__create_services(prototype=UserFactory.ubuntu_server, name=name)


    @staticmethod
    def create_windows_server(name):
        return UserFactory.__create_services(UserFactory.windows_server, name)


if __name__ == "__main__":
    user_1 = UserFactory.create_ubuntu_server("Test_12")
    user_2 = UserFactory.create_windows_server("Test_34")

    print(user_1)
    print(user_2)