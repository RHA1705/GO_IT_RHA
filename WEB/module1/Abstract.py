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
    
c_device = CommunicationDevice()

