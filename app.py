
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api


from app.config import mysqlconfig
from app.models.item import ItemModel
from app.models.store import StoreModel
from app.models.user import UserModel

#print(mysqlconfig)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=mysqlconfig
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
app.config["JWT_SECRTE_KEY"]="my.secrete.key"

jwt=JWTManager(app)
api=Api(app)

@app.before_first_request
def create_table():
    pass

#app.add_resource(classname,'/item')

if __name__=='__main__':
    app.run(debug=True)