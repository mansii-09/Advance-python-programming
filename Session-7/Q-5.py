class Notification:
    def send(self):
        print("Sending Notification")

class EmailNotification(Notification):
    def send(self):
        print("Sending Email Notification")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS Notification")

obj1 = EmailNotification()
obj2 = SMSNotification()

obj1.send()
obj2.send()