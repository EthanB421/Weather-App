import tkinter as tk
import requests

HEIGHT = 700
WIDTH = 850

def format_response(weather):
    try:
        name = (weather['name'])
        description = (weather['weather'][0]['description'])
        temp = (weather['main']['temp'])

        final_str = 'City: %s \nConditions: %s \nTemperature ℉: %s' % (name, description, temp)
    except:
        final_str = 'There was a problem with your request. '
        
    return final_str

def get_weather(city):
    weather_key = '2dc4f1cf0e755704cec3687b5970898b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

root = tk.Tk()

def test_function(entry):
    print("This is the entry", entry)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


frame = tk.Frame(root, bg="#8ae6c1")
frame.place(relwidth=1, relheight=1)


button = tk.Button(frame, text="Get weather", bg='#8ac4e6', font=15, command=lambda: get_weather(entry.get()))
button.place(relx=0.67, rely=0.15, relwidth=0.15, relheight=0.08)


entry = tk.Entry(frame, bg="#8ac4e6")
entry.place(relx=0.22, rely=0.15, relwidth=0.45, relheight=0.08)

label = tk.Label(frame, bg="#8ac4e6",fg="white", font=('Times New Roman', 28))
label.place(relx=0.22, rely=0.3, relwidth=0.6, relheight=0.55)

root.mainloop()