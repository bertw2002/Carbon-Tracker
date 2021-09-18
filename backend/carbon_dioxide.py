#Base Python
import requests
import sys
#Extended Python
from pprint import pprint
from session import get_rest

class Carbon():
    def __init__(self, location_list):
        super().__init__()
        self.rest = get_rest()
        self.url = "https://maps.googleapis.com/maps/api/directions/json"
        self.headers = {"Content-Type": "application/json"}
        self.locations = location_list
        self.mode = "driving"
        self.key = "AIzaSyA5f6zNPcu302hvENF_rxbRzf8x0rHRQPA"
        self.building_geo_mappings = {'Martel' : '29.7217,-95.3977', 'Brown': '29.7215,-95.3963', 'Hanszen': '29.7158,-95.4002',
            'Lovett':'29.7163,-95.3980', 'Wiess':'29.7147,-95.3998','Jones':'29.7215, -95.3698',
            'Duncan':'29.7218,-95.3985', 'McMurtry':'29.7204,-95.3978', 'Sid Richardson':'29.7151,-95.3991',
            'Baker': '29.7170,-95.3991', 'Will Rice': '29.7164,-95.3987', 'Herzstein Hall':'29.7187531,-95.3993396','Sewall Hall':'29.71716,-95.4003', 'Keck Hall': '29.71716, -95.4003274', 
            'RMC':'29.71716,-95.4003', 'Fondren':'29.7171619,-95.4003274', 'Cambridge Office Building':'29.7166941, -95.3988713', 
            'Brockman Hall': '29.7170462,-95.4045214', 'Dell Butcher Hall':'29.7170462,-95.4045214', 'Rec center':'29.7165576,-95.4048481', 
            'Shepherd School of Music':'29.7165576,-95.4048481'}

    def total_distance(self):
        ttl_distance = 0.0
        for i in range(len(self.locations)-1):
            start_point = self.locations[i]
            end_point = self.locations[i+1]
            if start_point in self.building_geo_mappings.keys() and end_point in self.building_geo_mappings.keys():
                api_url = self.url + "?origin=" + self.building_geo_mappings[start_point] + "&destination=" + self.building_geo_mappings[end_point] + "&mode="+self.mode+"&key="+self.key
                response = self.rest.get(api_url)
                if response.status_code not in range(200,300):
                    print(f"Failed to get data on {api_url}")
                    return
                json_response = response.json()
                curr_dist = json_response['routes'][0]['legs'][0]['distance']['text']
                distances = curr_dist.split(" ")
                if "mi" in curr_dist:
                    distance = float(distances[0]) * 5280
                else:
                    distance = float(distances[0])
                ttl_distance+=distance
        return ttl_distance/5280  

    def carbon_dioxide_saved(self):
        return .9061 * self.total_distance()         


                
    
                
if __name__ == "__main__":
    carbon = Carbon(['Martel', 'Wiess', 'Herzstein Hall'])
    print("Carbon saved: " + str(carbon.carbon_dioxide_saved()) + " pounds")
    
