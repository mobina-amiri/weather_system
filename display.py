from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass  

class CurrentConditionsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Current conditions: {temperature}°C, {humidity}%, {pressure} hPa")


class StatisticsDisplay(Observer):
    def __init__(self):
        self.temperature_sum = 0  # مجموع دماها
        self.num_readings = 0  # تعداد خواندن‌ها
        self.max_temperature = float('-inf')  # حداکثر دما
        self.min_temperature = float('inf')  # حداقل دما
    
    def update(self, temperature, humidity, pressure):
        self.temperature_sum += temperature  # افزودن دما به مجموع
        self.num_readings += 1  # افزایش تعداد خواندن‌ها
        self.max_temperature = max(self.max_temperature, temperature)  # به‌روزرسانی حداکثر دما
        self.min_temperature = min(self.min_temperature, temperature)  # به‌روزرسانی حداقل دما
        
        average_temperature = self.temperature_sum / self.num_readings  # محاسبه میانگین دما
        print(f"Avg/Max/Min temperature: {average_temperature}/{self.max_temperature}/{self.min_temperature}")