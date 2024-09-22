import json
import requests
import tkinter as tk
KEY = 'aba96a35e497408eac0164520240308'
degree = '\u00B0'


def weather(city: str) -> None:
    url: str = f'http://api.weatherapi.com/v1/current.json?key={
        KEY}&q={city}&aqi=no'
    # print(data)
    try:
        response: requests.Response = requests.get(url)
        data: dict = json.loads(response.text)
        weather_: str = data['current']['condition']['text']
        temp: str = f"{data['current']['temp_c']}{degree}C"
    except:
        weather_ = 'Not Found'
        temp = 'Not Found'
    finally:
        tk.Label(root, text=f'Weather: {weather_}', font=(
            'JetBrains Mono', 18)).place(x=10, y=250, width=390, height=30)
        tk.Label(root, text=f'Temperature: {temp}', font=(
            'JetBrains Mono', 18)).place(x=10, y=300, width=390, height=25)


root = tk.Tk()
root.geometry('450x500')
root.maxsize(400, 600)
root.minsize(400, 600)
label = tk.Label(root, text='Enter City Name',
                 font=('Fira Code Retina', 20, 'bold'))
label.place(x=50, y=50, width=300, height=50)
s = tk.StringVar()
e = tk.Entry(root, textvariable=s, font=('JetBrains Mono', 18))
e.place(x=50, y=105, width=300, height=50)
btn = tk.Button(root, text='Submit', command=lambda: weather(s.get()),
                font=('JetBrains Mono', 18))
btn.place(x=150, y=160, width=100, height=50)
root.mainloop()
