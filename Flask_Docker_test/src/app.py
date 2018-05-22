from flask import Flask

app = Flask(__name__)     

@app.route("/")
def home():
    return 'Hello World from AWS cloud 9 Docker !!' 
app.run(host="0.0.0.0", port=8080, debug=False) 
