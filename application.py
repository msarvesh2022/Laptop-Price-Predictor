from flask import Flask , render_template , url_for , request

app = Flask(__name__)

import os
import pickle

# Get the absolute path to the pkl file
pkl_file_path = os.path.join(os.path.dirname(__file__), 'newlaptop.pkl')

# Load the model using the absolute path
model = pickle.load(open(pkl_file_path, 'rb'))

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/predict',methods= ['GET','POST'])

def pred():
    
    
    Company= request.form.get('Company')
    TypeName= request.form.get('TypeName')
    Inches= float(request.form.get('Inches'))
    Ram= float(request.form.get('Ram'))
    Weight= float(request.form.get('Weight'))
    HD_Display= int(request.form.get('HD_display'))
    cpu_brand= request.form.get('cpu_brand')
    memory= float(request.form.get('memory'))
    gpu_brand= request.form.get('gpu_brand')
    operating_system= request.form.get('operating_system')
    
    
    output= model.predict([[Company,TypeName,Inches,Ram,Weight,HD_Display,cpu_brand,memory,gpu_brand,operating_system]])
    output= output[0]
    
    return f"<h1>Price of laptop will be {output}</h1>"

if __name__=="__main__":
    app.run(debug=True)