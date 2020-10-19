from flask import Flask 
from flask_restful import  Api 
from recursos.hotel import Hoteis, Hotel

app = Flask(__name__)
api = Api(app)


api.add_resource(Hoteis, "/hoteis")
api.add_resource(Hotel, "/hoteis/<string:hotel_id>")

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)