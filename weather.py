from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root = Tk()
root.title("Weather Monitor")
root.geometry("600x300")

def zipLookup():
	#zip.get()
	#zipLabel = Label(root, text=zip.get())
	#zipLabel.grid(row=1, column=0, columnspan=2)
	try:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=8B7D8FD9-66A2-4233-A611-787744ED27AD")
		api = json.loads(api_request.content)
		city = api[0]['ReportingArea']
		quality = api[0]['AQI']
		category = api[0]['Category']['Name']

		if category == "Good":
			weather_color = "#0C0"
		elif category == "Moderate":
			weather_color = "#FFFF00"

		elif category == "Unhealthy for Sensitive Groups":
			weather_color = "#ff9900"

		elif category == "Unhealthy":
			weather_color = "FF0000"


		elif category == "Very Unhealthy":
			weather_color = "#990066"


		elif category == "Hazardous":
			weather_color = "#660000"

		root.configure(background=weather_color)

		myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
		myLabel.pack()
	except Exception as e:
		api = "Error..."

# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=49504&distance=5&API_KEY=8B7D8FD9-66A2-4233-A611-787744ED27AD

lookup_frame = LabelFrame(root, text="Lookup Air Quality", padx=5, pady=5)
lookup_frame.pack(padx=10, pady=10)


zip = Entry(lookup_frame)
zip.pack()





submitButton = Button(lookup_frame, text="Lookup", command=zipLookup)
submitButton.pack()
mainloop()
