from flask import Flask, request, Response
from database_folder.database import initialize_db
from database_folder.models import Card, User
from bson import ObjectId
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask_jwt_extended import create_access_token
import datetime


class Show(Resource):
    def get(self):
        cards = Card.objects().order_by('-id').to_json()
        return Response(cards, mimetype="application/json", status=200)
    
class Show_by_id(Resource):
    def get(self,id):
        try:
        # body = request.get_json()
            cards = Card.objects.get(id=ObjectId(id))
            print(cards.to_json())
            return Response(cards.to_json(), mimetype="application/json", status=200) 
        except:
            return 'Card is not exist.', 200

class add_card(Resource):
    @jwt_required()
    def post(self):
        body = request.get_json()
        card = Card(**body).save()
        id = card.id
        return {'id': str(id)}, 200

class edit_card(Resource):
    @jwt_required()
    def put(self):
        body = request.get_json()
        Card.objects.get(id=ObjectId(body["id"])).update(**body)
        return 'Successfully updated card', 200

class delete_card(Resource):
    @jwt_required()
    def delete(self,id):
        # body = request.get_json()
        Card.objects.get(id=ObjectId(id)).delete()
        return 'Successfully deleted card', 200

class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User(**body).save()
            id = user.id
            return {'id': str(id)}, 200
        except:
            return {'error' :'Email is not in correct format.'}, 401

class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        try:
            user = User.objects.get(email=body.get('email'))
            if user.password != body.get("password"):
                return {'error': 'Email or password invalid'}, 401
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {'access': access_token}, 200
        except:
            return {'error': 'Email or password is not correct.'}, 401
        
class search(Resource):
    def post(self):
        body = request.get_json()
        search_result = Card.objects(Name__icontains=body.get("search")).to_json()
        
        return Response(search_result, mimetype="application/json", status=200)
        