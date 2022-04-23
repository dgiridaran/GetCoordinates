from flask import Response
import requests

class Address:

    valid_outputformat = ['json', 'xml']
    url = "https://maps.googleapis.com/maps/api/geocode/json?"
    key = "AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw"

    def __init__(self, address, output_format):
        self.address = address
        self.output_format = output_format

    
    def __str__(self):
        return f"return coordinates of this addess {self.address} in {self.output_format}"

    def get_address_coordinates(self):
        if type(self.address) != str:
            return {"error":"Invalid Address"}, 400
        if type(self.output_format) != str:
            return {"error":"Invalid Output Format"}, 400
        if self.output_format not in Address.valid_outputformat:
            return {"error":f"Output Format must be with in  {Address.valid_outputformat}"}, 400
        params = {
                "key":Address.key,
                "address":self.address
        }
        result = requests.get(Address.url, params=params)
        data = result.json()
        coordinates = data['results'][0]['geometry']['location']
        if self.output_format == "json":
            return {"address": self.address,
                     "coordinates": coordinates}, 200
        elif self.output_format == "xml":
            xml = f"<root><address>{self.address}</address><coordinates><lat>{coordinates['lat']}</lat><lng>{coordinates['lng']}</lng></coordinates></root>"
            return Response(xml, mimetype='text/xml')
