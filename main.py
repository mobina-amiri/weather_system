from weather_system import WeatherData
from display import CurrentConditionsDisplay, StatisticsDisplay

def main():
    # ایجاد ایستگاه هواشناسی
    weather_data = WeatherData()
    
    # ایجاد نمایشگرها
    current_display = CurrentConditionsDisplay()
    statistics_display = StatisticsDisplay()

    # ثبت نمایشگرها به عنوان Observer
    weather_data.register_observer(current_display)
    weather_data.register_observer(statistics_display)

    # تغییرات وضعیت هوا
    print("First measurement:")
    weather_data.set_measurements(25, 65, 1013)
    
    print("\nSecond measurement:")
    weather_data.set_measurements(28, 70, 1012)

    # حذف یک نمایشگر
    weather_data.remove_observer(statistics_display)

    print("\nThird measurement (after removing statistics display):")
    
    weather_data.set_measurements(30, 75, 1011)

if __name__ == "__main__":
    main()