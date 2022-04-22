from flask import Flask,request
from flask_restful import Resource,Api
from apis.address_details_api import AddressDetails


app = Flask(__name__)
app.secret_key = "1sdcmk4lkml42"
api = Api(app)


api.add_resource(AddressDetails, "/getAddressDetails")

if __name__ == "__main__":
    app.run(debug=True)