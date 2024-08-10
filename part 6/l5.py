from abc import ABC, abstractmethod

class Confirmation(ABC):
    @abstractmethod
    def send_notification(self):
        pass

class EmailConfirmation(Confirmation):
    def send_notification(self):
        print("Email sent")

class SMSConfirmation(Confirmation):
    def send_notification(self):
        print("SMS sent")

class ConfirmationService:
    def __init__(self, notifier: Confirmation):
        self.notifier = notifier

    def send(self):
        self.notifier.send_notification()

if __name__ == "__main__":
    email = EmailConfirmation()
    sms = SMSConfirmation()

    email_service = ConfirmationService(email)
    sms_service  = ConfirmationService(sms)

    email_service.send()
    sms_service.send()