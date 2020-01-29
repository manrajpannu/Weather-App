import tkinter as tk
import requests

height = 500
width  = 600


def get_words(words):
	print(words)

def format_weather(weather):
	try:
		location = [weather['name'],weather['sys']['country']]
		weather_desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		output = 'Location: {}\nConditions: {}\nTemperature (celsius): {}'.format(str(' '.join(location)), str(weather_desc),str(temp))

	except: 
		output = 'There was a problem retrieving that information'

	return output

def get_icon(weather):
	try:
		icon = weather['weather'][0]['icon']
	except:
		icon = 'error'

	return icon



def get_weather(city):
	key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'APPID':key, 'q':city,'units':'Metric'}
	response = requests.get(url,params=params)

	weather = response.json()

	weather_output['text'] = format_weather(weather)
	
	# icon = get_icon(weather)
	# icon_image = tk.PhotoImage(file=('img/{}.png'.format(icon)))
	# icon_label = tk.Label(text_frame,image=icon_image)
	# icon_label.place(relwidth=0.5,relheight=0.5)








root = tk.Tk()

canvas = tk.Canvas(root, height=height,width=width)
canvas.pack()



bg_image = tk.PhotoImage(file='cloud.png')
bg_label = tk.Label(root,image=bg_image)
bg_label.place(relwidth=1,relheight=1)



search_frame = tk.Frame(root,bg='#98FAFF')
search_frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)

location_entry = tk.Entry(search_frame)
location_entry.place(relx=0.01, rely= 0.1 , relwidth = 0.7,relheight = 0.75)


button = tk.Button(search_frame, text='Get Weather',font=('Arial',12),command = lambda: get_weather(location_entry.get()))
button.place(relx=0.75,rely=0.1,relwidth=0.24,relheight=0.75)

text_frame = tk.Frame(root,bg='#98FAFF')
text_frame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.65)

weather_output = tk.Label(text_frame,font=('Arial',18),anchor='nw',justify='left',bd=4)
weather_output.place(relx=0.03, rely= 0.03 , relwidth = 0.94,relheight = 0.94)




root.mainloop()
