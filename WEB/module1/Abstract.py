from abc import ABC, abstractmethod, ABCMeta
#
#
# class Abs:
#     def pay(self):
#         raise NotImplementedError
#
# class System(Abs):
#     pass
#
#
# class AbsAbstract(metaclass=ABCMeta):
#     @abstractmethod
#     def pay(self):
#         pass
#
# class SystemAbs(AbsAbstract):
#     pass
#
# if __name__ == '__main__':
#     p = System()
#     p1 = SystemAbs()

class CommunicationDevice(ABC):
    @abstractmethod
    def send_message(self):
        pass

    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def browsing(self):
        pass

class DeviceWithCall(ABC):
    @abstractmethod
    def call(self):
        pass

class DeviceWithBrowsing(ABC):
    @abstractmethod
    def browsing(self):
        pass

class DeviceWithMessage(ABC):
    @abstractmethod
    def send_message(self):
        pass
class SmartPhone(DeviceWithBrowsing, DeviceWithCall, DeviceWithMessage):
    def send_message(self):
        return "Send Message"

    def call(self):
        return "Call"

    def browsing(self):
        return "Go to Google"

class DiscPhone(DeviceWithCall):
    def call(self):
        return "Call on disc phone"

dp = DiscPhone()
print(dp.call())

sm = SmartPhone()
print(sm.call())
print(sm.send_message())
