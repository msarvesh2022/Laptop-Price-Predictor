from flask import Flask , render_template , url_for 

app = Flask(__name__)

@app.route('/')

def home():
    return "This is Home Page"



if __name__=="__main__":
    app.run(debug=True)