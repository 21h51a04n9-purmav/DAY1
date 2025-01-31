from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
class Child(Father):
    def disp(self):
        print("Child class")
        print("defining abstract method")
class Relative(Father):
    def disp(self):
        print("relative class")
        print("defining relative method")
r=Relative()
c=Child()
c.disp()
r.disp()


#Mail ==> Interface
   # ==> send() Abstract
# Email
# SMS
# Whatsapp

from abc import ABC,abstractmethod
class Mail(ABC):
    @abstractmethod
    def send(self):
        pass
class Email(Mail):
    def send(self):
        print("send an email to client")
class SMS(Mail):
    def send(self):
        print("send an SMS to the user")
class Whatsapp(Mail):
    def send(self):
        print("send a whatsapp message")
e=Email()
s=SMS()
w=Whatsapp()
e.send()
s.send()
w.send()

           