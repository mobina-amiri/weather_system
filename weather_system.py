from linklist import LinkedList

class WeatherData:
    def __init__(self):
        self.observers = LinkedList()
        self.temp = 0
        self.pressure = 0
        self.humidity = 0

    def register_observer(self, observer):
        self.observers.insert(observer)
        print(f"Observer added: {observer}")

    def remove_observer(self, observer):
        self.observers.remove(observer)
        print(f"Observer removed: {observer}")

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temp, self.humidity, self.pressure)

    def set_measurements(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()
    
