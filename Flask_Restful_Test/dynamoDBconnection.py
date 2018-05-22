import boto3
from boto3.dynamodb.conditions import Key, Attr


class noSQLDB:
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')
    def __init__(self, tableName):
        # Instantiate a table resource object without actually
        # creating a DynamoDB table. Note that the attributes of this table
        # are lazy-loaded: a request is not made nor are the attribute
        # values populated until the attributes
        # on the table resource are accessed or its load() method is called.
        self.tableName = self.dynamodb.Table(tableName)
        
    def printTableInfo(self, tableName):
        # Print out some data about the table.
        # This will cause a request to be made to DynamoDB and its attribute
        # values will be set based on the response.
        return self.tableName.creation_date_time
    
    #query by key's value of key "storeName", 返回时个list
    def queryByStoreNameKeyValue(self, storeNameValue):
        storeQueryResponse = self.tableName.query(KeyConditionExpression=Key('storeName').eq(storeNameValue))
        items = storeQueryResponse['Items']
        return(items)
        
    #create store item in DynamoDB
    def createStore(self, storeName, storeOwner, storeSize):
        try:
            self.tableName.put_item(
           Item={
                'storeName': storeName,
                'storeOwner': storeOwner,
                'storeSize': storeSize
            }
        )
        except Exception as error:
            return("something wrong in DynamoDB")
        
        else:
            return("record created !")
        
'''
    #query method for items
    def queryByItemNameKeyValue(self, storeItemValue):
        itemQueryResponse = self.tableName.query(KeyConditionExpression=Key('storeItems').eq(storeItemValue))
        items = itemQueryResponse['Items']
        return(items)
    
    #query by item's key and value #返回是dictionary,而且必须指定所有的primary key ！！！
    def getItemsByStoreName(self, itemName, storeName):
        itemGetResponse = self.tableName.get_item(
            Key={
                    "storeItems": itemName,
                    "storeName": storeName
                    }
                )
        item = itemGetResponse['Item']
        return(item)
'''

'''
storeTable = noSQLDB("Flask_Test_Stores")
print(storeTable.printTableInfo("Flask_Test_Stores"))
print(storeTable.queryByStoreNameKeyValue("firstStore"))

itemTable = noSQLDB("Flask_Test_Store_Items")
print(itemTable.printTableInfo("Flask_Test_Store_Items"))
print(itemTable.queryByItemNameKeyValue("firstItem"))
print(itemTable.getItemsByStoreName("firstItem", "firstStore"))
'''



'''
#update item
storeTable.update_item(
    Key={'storeName': 'firstStore'},
    UpdateExpression='SET storeOwner = :val1',
    ExpressionAttributeValues={
        ':val1': "KK"
    }
)
'''