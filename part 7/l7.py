import base64

class CheckSignature:
    def check(self, message) -> bool:
        if message.endswith("_secure_sign"):
            print("Signature valid")
            return True
        else:
            print("Signature invalid")
            return False

class EncryptMessage:
    def encrypt(self, message):
        result = base64.b64encode(message.encode("utf-8"))
        print(f"Message {message} - secret [{result}]")
        return result


class Sender:
    def send(self, message):
        print(f"Message {message} sent")


class Client:
    def __init__(self):
        self.__signature = CheckSignature()
        self.__encrypt = EncryptMessage()
        self.__sender = Sender()

    def send_message(self, message):
        if self.__signature.check(f"{message}_secure_sign"):
            encrypt_message = self.__encrypt.encrypt(message)
            self.__sender.send(encrypt_message)


if __name__ == "__main__":
    user = Client()
    user.send_message("Hello World")
