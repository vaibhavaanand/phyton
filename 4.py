# importing the requests library 
import requests 
  
# api-endpoint 
URL = https://www.google.com/maps/place/CMR+University+Main+Campus/@13.1175726,77.6532554,17z/data=!3m1!4b1!4m5!3m4!1s0x3bae1bd82408da43:0xeebaa35808847cd5!8m2!3d13.1175674!4d77.6554441
  
# location given here 
location = " CMR University"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
  
# extracting data in json format 
data = r.json() 
  
  
# extracting latitude, longitude and formatted address  
# of the first matching location 
latitude = data['results'][0]['geometry']['location']['lat'] 
longitude = data['results'][0]['geometry']['location']['lng'] 
formatted_address = data['results'][0]['formatted_address'] 
  
# printing the output 
print("Latitude:%s\nLongitude:%s\nFormatted Address:%s"
      %(latitude, longitude,formatted_address))
