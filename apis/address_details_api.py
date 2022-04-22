from flask import Flask,request, jsonify
from flask_restful import Resource
from methords.address_details import Address


class AddressDetails(Resource):

    def post(self):
        data = request.get_json()
        result = Address(**data)
        return result.get_address_coordinates()
        
