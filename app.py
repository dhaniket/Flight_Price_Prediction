from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        
        Source = request.form['Departure_Time']
        if(Source == 'Evening'):
            departure_time=2
        elif(Source == 'Early_Morning'):
            departure_time=1
        
        elif(Source == 'Morning'):
            departure_time=4

        elif(Source == 'Afternoon'):
            departure_time=0

        elif(Source == 'Night'):
            departure_time=5

        elif(Source == 'Late_Night'):
            departure_time=3
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Source = request.form['Arrival_Time']
        if(Source == 'Evening'):
            arrival_time=2
        elif(Source == 'Early_Morning'):
            arrival_time=1
        
        elif(Source == 'Morning'):
            arrival_time=4

        elif(Source == 'Afternoon'):
            arrival_time=0

        elif(Source == 'Night'):
            arrival_time=5

        elif(Source == 'Late_Night'):
            arrival_time=3

        # print("Arrival : ", Arrival_hour, Arrival_min)
        
        ## Days LEft
        days_left = request.form['days']

        # Duration
        duration = request.form['text']

        # print("Duration : ", dur_hour, dur_min)


        # Class
        Source = request.form['Class']
        if(Source == 'Economy'):
            sclass=1
        elif(Source == 'Business'):
            sclass=0

        # Total Stops
        stops = int(request.form["Stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        Source=request.form['Source']
        if(Source=='SpiceJet'):
            airline=4

        elif (Source=='IndiGo'):
            airline=3

        elif (Source=='AirAsia'):
            airline=0

        elif (Source=='Vistara'):
            airline=5

        elif (Source=='GO_FIRST'):
            airline=2

        elif (Source=='Air India'):
            airline=1

        # Source
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'Mumbai'):
            source_city=5
        
        elif (Source == 'Delhi'):
            source_city=2

        elif (Source == 'Bangalore'):
            source_city=0

        elif (Source == 'Hyderabad'):
            source_city=3

        elif (Source == 'Kolkata'):
            source_city=4
        
        elif (Source == 'Chennai'):
            source_city=1

        Source = request.form["Destination"]
        if (Source == 'Mumbai'):
            destination_city=5
        
        elif (Source == 'Delhi'):
            destination_city=2

        elif (Source == 'Bangalore'):
            destination_city=0

        elif (Source == 'Hyderabad'):
            destination_city=3

        elif (Source == 'Kolkata'):
            destination_city=4
        
        elif (Source == 'Chennai'):
            destination_city=1

        query = np.array([
            airline,
            source_city,
            departure_time,
            stops,
            arrival_time,
            destination_city,
            sclass,
            duration,
            days_left
        ])
        query = query.reshape(1,9)

        prediction = model.predict(query)

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)