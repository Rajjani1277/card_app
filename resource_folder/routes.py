from .card import *

def initialize_routes(api):
    api.add_resource(Show, '/show')
    api.add_resource(add_card, '/add_card')
    api.add_resource(edit_card, '/edit_card')
    api.add_resource(delete_card, '/delete')
    api.add_resource(SignupApi, '/register')
    api.add_resource(LoginApi, '/login')
    api.add_resource(Show_by_id, '/show_card/<id>')
    api.add_resource(search, '/search')