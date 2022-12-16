from flask import Flask, request, Response
from database_folder.database import initialize_db
from database_folder.models import Card, User
from bson import ObjectId
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask_jwt_extended import create_access_token
import datetime

# show card API
class Show(Resource):
    # Using GET method
    def get(self):
        cards = Card.objects().order_by('-id').to_json()
        return Response(cards, mimetype="application/json", status=200)
    
# Show Individual Card API
class Show_by_id(Resource):
    # Using GET method
    def get(self,id):
        # handling the error with try...catch
        try:
        # body = request.get_json()
            cards = Card.objects.get(id=ObjectId(id))
            print(cards.to_json())
            return Response(cards.to_json(), mimetype="application/json", status=200) 
        except:
            return 'Card is not exist.', 200

# Add Card API
class add_card(Resource):
    # using POST method
    # JWT token authentication is required
    @jwt_required()
    def post(self):
        body = request.get_json()
        card = Card(**body).save()
        id = card.id
        return {'id': str(id)}, 200

# Edit Card API
class edit_card(Resource):
    # using POST method
    # JWT token authentication is required
    @jwt_required()
    def put(self):
        body = request.get_json()
        Card.objects.get(id=ObjectId(body["id"])).update(**body)
        return 'Successfully updated card', 200

# Delete Card API
class delete_card(Resource):
    # using POST method
    # JWT token authentication is required
    @jwt_required()
    def delete(self,id):
        # body = request.get_json()
        Card.objects.get(id=ObjectId(id)).delete()
        return 'Successfully deleted card', 200

# Register API
class SignupApi(Resource):
    # Using POST method
    def post(self):
        # handling error with try...catch
        try:
            body = request.get_json()
            user = User(**body).save()
            id = user.id
            return {'id': str(id)}, 200
        except:
            return {'error' :'Email is not in correct format.'}, 401

# Login API
class LoginApi(Resource):
    # Using POST method
    def post(self):
        body = request.get_json()
        try:
            # validating the login form.
            user = User.objects.get(email=body.get('email'))
            if user.password != body.get("password"):
                return {'error': 'Email or password invalid'}, 401
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {'access': access_token}, 200
        except:
            return {'error': 'Email or password is not correct.'}, 401
        
# Search Card API
class search(Resource):
    # Using POST method
    def post(self):
        body = request.get_json()
        search_result = Card.objects(Name__icontains=body.get("search")).to_json()
        
        return Response(search_result, mimetype="application/json", status=200)
        
