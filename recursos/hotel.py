from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
  {
    "hotel_id":"Alpha",
    "nome": "La Salles Hotel Alpha",
    "estrelas": 5,
    "diaria":540.00,
    "cidade": "Rio de Janeiro"
  },
  {
    "hotel_id":"Beta",
    "nome": "Hotel Beta",
    "estrelas": 3,
    "diaria":440.00,
    "cidade": "Malibu"
  },
  {
    "hotel_id":"Kube",
    "nome": "La Kube Hotel",
    "estrelas": 5,
    "diaria":740.00,
    "cidade": "Malibu"
  },
  {
    "hotel_id":"Gine",
    "nome": "Gina Hotel Stars",
    "estrelas": 3,
    "diaria":240.00,
    "cidade": "Rio de Janeiro"
  },
]





class Hoteis(Resource):
    def get(self):

      return {"hoteis":hoteis}

class Hotel(Resource):

  argumentos = reqparse.RequestParser()
  argumentos.add_argument("nome")
  argumentos.add_argument("estrelas")
  argumentos.add_argument("diaria")
  argumentos.add_argument("cidade")
  
  def find_hotel(hotel_id):
    for hotel in hoteis:
      if hotel['hotel_id'] == hotel_id:
         return hotel
    return None

  def get(self, hotel_id):
    hotel = Hotel.find_hotel(hotel_id)
    if hotel: 
       return hotel 
    return {"message": "Hotel não encontrado !"} , 404 

  def post(self, hotel_id):
    dados = Hotel.argumentos.parse_args()
    hotel_obj = HotelModel(hotel_id,**dados)
    novo_hotel = hotel_obj.json()
    hoteis.append(novo_hotel)
    return novo_hotel, 200
  
  def put(self, hotel_id):
    dados = Hotel.argumentos.parse_args()
    hotel_obj = HotelModel(hotel_id,**dados)
    novo_hotel = hotel_obj.json()
    hotel = Hotel.find_hotel(hotel_id)
    if hotel:
       hotel.update(novo_hotel)
       return novo_hotel, 200

    hoteis.append(novo_hotel)
    return novo_hotel,201
  
  def delete(self, hotel_id):
    global hoteis 
    hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
    return {"message": "Hotel Deletado"}
    

