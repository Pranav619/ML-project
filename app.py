from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Starting Machine learning project"

  
if __name__=="__main__":
    app.run(debug=True)    

#Heroku_api_name= ml-summer-app
#heroku_api_key = 
#heroku_email = pranav619vashisth@gmail.com