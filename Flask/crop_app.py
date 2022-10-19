# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask,render_template ,request

app = Flask(__name__) #interface between webserver and web application

import pickle
#model1 = pickle.load(open("knnmodel.pkl","rb"))
#model2 = pickle.load(open("logisticregressionmodel.pkl","rb"))
model3 = pickle.load(open("naivebayesmodel.pkl","rb"))
#model4 = pickle.load(open("svmmodel.pkl","rb"))
#model5 = pickle.load(open("decisiontreemodel.pkl","rb"))

 #We can use any of the model above ,  here i am using naive bayes theorem for the prediction



@app.route("/")#URL binding

def hello():
    return render_template("index.html")


@app.route("/login",methods  = ["POST"]) #URL binding

def user():
    p = request.form['nitro']
    q =  request.form['phos']
    r = request.form['potash']
    s = request.form['temp']
    t = request.form['hum']
    u = request.form['ph']
    v = request.form['rain']
    # in the input we have given name as a so we are taking 
    #here a otherwise according to the written value 
    #return "Hello bhai ! Kya haal h tere "
    

        
    temp =[[int(p),int(q),int(r),float(s),float(t),float(u),float(v)]]    
    
    y = model3.predict(temp)
    return render_template("index.html", y = ""+str(y[0]))


@app.route("/templates/dataSet.html")  

def dataset():
    return render_template("dataSet.html")
    



@app.route("/templates/model.html")  

def model():
    return render_template("model.html")


@app.route("/templates/index.html")  


def home():
    return render_template("index.html")
if __name__ =="__main__":
    app.run(debug=True)