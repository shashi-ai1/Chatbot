
import model
from flask import Flask, render_template, request
app = Flask(__name__)

# load model
import pickle
pickle.load(open('infile','rb'))

@app.route("/")
def home():
    return render_template("index.html")
  
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')
    #out=request.post(chat(userText))
    return str(model.chat(userText))
   


#**************** Server ***********


if __name__ == '__main__':
   app.run(debug=True) 
