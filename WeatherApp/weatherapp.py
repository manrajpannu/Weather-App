import tkinter as tk
import requests

# control the height and width of the window
height = 500
width  = 600

# function to take the json file and extract the important information
def format_weather(weather):

	try:
		# if a request is succesful
		# then we extract the location. weather description, and temperuature from the json file
		location = [weather['name'],weather['sys']['country']]
		weather_desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		# format it so it looks nice
		output = 'Location: {}\nConditions: {}\nTemperature (celsius): {}'.format(str(' '.join(location)), str(weather_desc),str(temp))

	except: 
		#outputs error if request is invalid
		output = 'There was a problem retrieving that information'

	return output


# function to output weather information based on a given location, area code, or postal code
def get_weather(city):
	
	# openweathermap api key and url to query requests
	key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'APPID':key, 'q':city,'units':'Metric'}

	# get request from openweather map in json format
	response = requests.get(url,params=params)
	weather = response.json()

	#outputs the formatted text to the text box on the gui
	weather_output['text'] = format_weather(weather)
	


# Initlize the main tk window 
# we will place all of our components in
main = tk.Tk()


# create a blank canvas based on the height and width we defined before
canvas = tk.Canvas(main, height=height,width=width)
canvas.pack()


# place the image on the canvas
# image is centered
bg_image = tk.PhotoImage(file='cloud.png')
bg_label = tk.Label(main,image=bg_image)
bg_label.place(relwidth=1,relheight=1)


# create a container on the screen with a blue fill
# we will place the search bar and submit button inside of it
search_frame = tk.Frame(main,bg='#98FAFF')
search_frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.1)

# create the search bar 
# users can enter locations, area codes, postals code
location_entry = tk.Entry(search_frame)
location_entry.place(relx=0.01, rely= 0.1 , relwidth = 0.7,relheight = 0.75)

# creates the submit button with 'Get Weather' written inside of it
# each time the button is clicked the text inside of the search bar taken and run with the get_weather() function
button = tk.Button(search_frame, text='Get Weather',font=('Arial',12),command = lambda: get_weather(location_entry.get()))
button.place(relx=0.75,rely=0.1,relwidth=0.24,relheight=0.75)

# creates the container with blue fill
# we will place a text box inside of it
# used for outputing the weather information
text_frame = tk.Frame(main,bg='#98FAFF')
text_frame.place(relx=0.1,rely=0.25,relwidth=0.8,relheight=0.65)

# create a text box for outputing weather information
# text starts from the top left and is justified left
weather_output = tk.Label(text_frame,font=('Arial',15),anchor='nw',justify='left',bd=4)
weather_output.place(relx=0.03, rely= 0.03 , relwidth = 0.94,relheight = 0.94)




main.mainloop()
