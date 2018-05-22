def jwtAuth(userName, userCode):
    if userName == "raiden" and userCode == "KK":
        return "raiden"
        
def jwtIdentify(payload):
    userName = payload["userName"]
    return "raiden"