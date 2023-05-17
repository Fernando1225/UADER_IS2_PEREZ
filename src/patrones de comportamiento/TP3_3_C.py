class Observer:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def notify(self, message, observer_id = False):
        if (observer_id):
            if (self.observer_id in message):
                print(f"Observer {self.observer_id} received message: {message}")
        else:
            print(f"Observer {self.observer_id} received message: {message}")


class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify_all(self, message, observer_id = False):
        for observer in self.observers:
            if observer_id:
                observer.notify(message, True)
            else:
                observer.notify(message)


# Crear las clases con sus respectivos IDs
class Class1(Observer):
    def __init__(self):
        super().__init__("ID01")

class Class2(Observer):
    def __init__(self):
        super().__init__("ID02")

class Class3(Observer):
    def __init__(self):
        super().__init__("ID03")

class Class4(Observer):
    def __init__(self):
        super().__init__("ID04")

class Class5(Observer):
    def __init__(self):
        super().__init__("ID05")

# Crear el objeto Subject y suscribir las clases
subject = Subject()
subject.subscribe(Class1())
subject.subscribe(Class2())
subject.subscribe(Class3())
subject.subscribe(Class4())
subject.subscribe(Class5())

# Emitir 9 IDs y notificar a los observadores
IDs = ["ID01", "ID02", "ID03", "ID04", "ID05", "ID06", "ID07", "ID08", "ID09"]

for ID in IDs:
    subject.notify_all(ID, True)




subject.notify_all("Hello, world!")