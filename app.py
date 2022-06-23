from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Starting Machine learning project"

  
if __name__=="__main__":
    app.run(debug=True)    

#Heroku_api_name= ml-summer-app
#heroku_api_key = 377fb4fd-ad47-4cfa-90d9-583a2b25d93a
#heroku_email = pranav619vashisth@gmail.com