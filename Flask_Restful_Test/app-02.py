from flask import Flask, jsonify, request #impost JSON function
from dynamoDBconnection import noSQLDB

app = Flask(__name__)     #创建一个wsgi应用

@app.route("/")           #添加路由：根
def home():
    return 'Hello World from AWS cloud 9 !' #输出一个字符串

#post - 创建一个store
@app.route("/api/createStore", methods=["POST"]) #默认是GET，需要指定为POST
def createStore():
    storeTable = noSQLDB("Flask_Test_Stores")
    request_data = request.get_json()
    return jsonify(storeTable.createStore(request_data["storeName"], request_data["storeOwner"], request_data["storeSize"]))

#get - 根据资源名得到一个store内容
@app.route("/api/getStore/<string:storeName>", methods=["GET"])
def getStore(storeName):
    storeTable = noSQLDB("Flask_Test_Stores")
    return jsonify((storeTable.queryByStoreNameKeyValue(storeName)))

#post - 创建某个store下面的item
@app.route("/api/createStoreItem/<string:storeName>/<string:itemName>", methods=["POST"])
def createStoreItem(storeName, itemName):
    pass

#get - 得到某个store下面的item，根据资源名
@app.route("/api/getStoreItem/<string:storeName>/<string:itemName>", methods=["GET"])
def getStoreItem(storeName, itemName):
    pass


#用0.0.0.0 来作为host
#用8080端口，而不是5000
app.run(host="0.0.0.0", port=8080, debug=False) #启动app的调试模式
