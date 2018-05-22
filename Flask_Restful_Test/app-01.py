
from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
import boto3
from boto3.dynamodb.conditions import Key, Attr
from security import jwtAuth, jwtIdentify
#无需jonsify，flask_restful自动转换

app = Flask(__name__)
app.secret_key = "KK"
myApi = Api(app)
jwt = JWT(app, jwtAuth, jwtIdentify)
dynamodb = boto3.resource('dynamodb')

#从resource类继承，定义一个类然后重写get post等方法
class GetMyDynamoDB(Resource):
    #全局属性
    #重载类初始化
    def __init__(self):
        #supper().__init_()
        self.tableName = dynamodb.Table("Flask_Test_Stores")
    
    #重写get方法
    @jwt_required() #JWT auth
    def get(self, storeName):
        storeQueryResponse = self.tableName.query(KeyConditionExpression=Key('storeName').eq(storeName))
        items = storeQueryResponse['Items']
        return(items[0])
        
class PostMyDynamoDB(Resource):
    def __init__(self):
        self.tableName = dynamodb.Table("Flask_Test_Stores")
        
          #重写post方法
    def post(self):
        try:
            request_data = request.get_json()
        except Exception as error:
            return("something wrong in DynamoDB")
        else:
            self.tableName.put_item(
            Item={
                    'storeName': request_data["storeName"],
                    'storeOwner': request_data["storeOwner"],
                    'storeSize': request_data["storeSize"]
                }
            )
        return("record created !")

myApi.add_resource(GetMyDynamoDB, "/api/getStore/<string:storeName>")  #http:xxx.xxx.xxx.xxx:8080/api/getStore/store1
myApi.add_resource(PostMyDynamoDB, "/api/createStore")  #http:xxx.xxx.xxx.xxx:8080/api/getStore/store1


#用0.0.0.0 来作为host
#用8080端口，而不是5000
app.run(host="0.0.0.0", port=8080, debug=True) #启动app的调试模式
