from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from app.config import mysqlConfig
from app.models.item import ItemModel
from app.models.store import StoreModel
from app.models.user import UserModel
from app.resources.item import Item, ItemList
from app.resources.store import Store, StoreList
from app.resources.user import User, UserRegister


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = mysqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "my.secret.key"

jwt = JWTManager(app)
api = Api(app)

@app.before_first_request
def create_tables():
    from app.db import db
    print("inside before first request")
    db.init_app(app)
    db.create_all()


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User, '/user')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(debug=True)