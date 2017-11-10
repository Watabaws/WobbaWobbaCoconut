#Adam Abbas
#SoftDev Period 7
#HW13 -- A RESTful Journey Skyward
#2017-11-9

from flask import Flask, render_template #The neccessary stuffs y'know
import urllib2, json

app = Flask(__name__) #Get that app pointed at the right thang

@app.route("/") #Our singular route
def dis_my_werk(): #Dis my werk:
	nasa_stuff = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=BjWaBwYhx6IOhy86vfeb6FHHZTvyzroI645oN2IE") #Get some info from the URL
	#print nasa_stuff.read() #Funny story this print statement stopped my code from working...
	nasa_dict = json.loads(nasa_stuff.read()) #Read the JSON data at said URL
	ttl1 = nasa_dict["title"] #Get the title
	url1 = nasa_dict["url"] #Git the image url
	desc1 = nasa_dict["explanation"] #Gut the explanation for the image
	return render_template("randpic.html", img1_url = url1, img1_desc = desc1, img1_title = ttl1) #Send it all off to our lovely and very conveniant template

#The usua
if __name__ == "__main__":
    app.debug = True
    app.run()
