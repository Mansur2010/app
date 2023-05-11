from tkinter import *
from parsing import *
import webbrowser
root = Tk()
root.title("chmosik")
def App():
    # dollar
    dollar_label = Label(root, text="Курс доллара:", font=("Arial", 15))
    dollar_label.grid(row=1, column=0, padx=10, pady=10)
    # euro
    euro_label = Label(root, text="Курс евро:", font=("Arial", 15))
    euro_label.grid(row=2, column=0, padx=10, pady=10)
    # ruble
    ruble_label = Label(root, text="Курс рубля:", font=("Arial", 15))
    ruble_label.grid(row=3, column=0, padx=10, pady=10)
    # weather
    weather_label1 = Label(root, text="температура:", font=("Arial", 15))
    weather_label1.grid(row=4, column=0, padx=10, pady=5)
    weather_label2 = Label(root, text="скорость ветра:", font=("Arial", 15))
    weather_label2.grid(row=5, column=0, padx=10, pady=5)
    weather_label3 = Label(root, text="влажность:", font=("Arial", 15))
    weather_label3.grid(row=6, column=0, padx=10, pady=5)
    weather_label4 = Label(root, text="вероятность осатков:", font=("Arial", 15))
    weather_label4.grid(row=7, column=0, padx=10, pady=5)
    def get_data():
        dollar = get_currency(DOLLAR_TENGE)
        euro = get_currency(EURO_TENGE)
        ruble = get_currency(RUBL_TENGE)
        youtube = get_subskr(YOUTUBE)
        weather = get_weather(WEATHER)
        All_data = [dollar, euro, ruble, youtube, weather]
        return All_data

    def add_values(ALL_DATA):
        global dollar_value, euro_value, ruble_value, youtube_value, weather_value

        dollar_value = Label(root, text=f"{ALL_DATA[0][0]} тг.", font=("Arial", 15))
        dollar_value.grid(row=1, column=1, padx=10, pady=10)
        euro_value = Label(root, text=f"{ALL_DATA[1][0]} тг.", font=("Arial", 15))
        euro_value.grid(row=2, column=1, padx=10, pady=10)
        ruble_value = Label(root, text=f"{ALL_DATA[2][0]} тг.", font=("Arial", 15))
        ruble_value.grid(row=3, column=1, padx=10, pady=10)
        weather_value1 = Label(root, text=f"{ALL_DATA[5][0]} {ALL_DATA[5][2]}.", font=("Arial", 15))
        weather_value1.grid(row=4, column=1, padx=10, pady=10)
        weather_value2 = Label(root, text=f"{ALL_DATA[5][4]}.", font=("Arial", 15))
        weather_value2.grid(row=5, column=1, padx=10, pady=10)
        weather_value3 = Label(root, text=f"{ALL_DATA[5][30]}.", font=("Arial", 15))
        weather_value3.grid(row=6, column=1, padx=10, pady=10)
        weather_value4 = Label(root, text=f"{ALL_DATA[5][8]}.", font=("Arial", 15))
        weather_value4.grid(row=7, column=1, padx=10, pady=10)
        youtube_value = Label(root, text=f"{ALL_DATA[3][0]}  подпищиков.", font=("Arial", 15))
        youtube_value.grid(row=8, column=1, padx=10, pady=10)

    def Label_destroy():
        dollar_value.destroy()
        euro_value.destroy()
        ruble_value.destroy()
        weather_value1.destroy()
        weather_value2.destroy()
        weather_value3.destroy()
        weather_value4.destroy()
        youtube_value.destroy()

    def refresh():
        ALL_DATA = get_data()
        destroy_label()
        add_values(ALL_DATA=ALL_DATA)
        
if __name__ =="__main__":
    App()
    root.mainloop()


