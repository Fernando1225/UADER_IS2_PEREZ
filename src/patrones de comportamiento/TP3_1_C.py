from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def handle(self, number):
        pass

class PrimoHandler(Handler):
    def handle(self, number):
        if number <= 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        print("Numero primo:", number)
        return True

class ParHandler(Handler):
    def handle(self, number):
        if number == 2:
            print("Numero par y primo:", number)
            return True
        elif number % 2 == 0:
            print("Numero par:", number)
            return True
        return False

class NumberSequence:
    def __init__(self):
        self.handlers = [PrimoHandler(), ParHandler()]

    def process(self, number):
        consumed = False
        for handler in self.handlers:
            if handler.handle(number):
                consumed = True
                break
        if not consumed:
            print("Numero no consumido:", number)

sequence = NumberSequence()
for i in range(1, 101):
    sequence.process(i)


print('Finished processing')
