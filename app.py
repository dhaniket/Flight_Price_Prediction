from email.mime import application
from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd
import numpy as np
import sklearn

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

        # Departure
        Source = request.form['Departure']
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

        # Arrival
        Source = request.form['Arrival']
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

        # Destination
        # Banglore = 0 (not in column)
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

        duration_flight = (request.form['duration'])
        days_left = int(request.form['days'])

        Source=request.form['Airline']
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

        elif (Source=='Air_India'):
            airline=1

        Source = request.form['Class']
        if(Source == 'Economy'):
            sclass=1
        elif(Source == 'Business'):
            sclass=0

        # Total Stops
        stops = int(request.form["Stops"])

        arr = [airline,
            source_city,
            departure_time,
            stops,
            arrival_time,
            destination_city,
            sclass,
            duration_flight,
            days_left]
        
        query = np.array([arr])

        query = pd.to_numeric(arr)
        query = query.reshape(1,9)
        prediction=model.predict(query)
        result = round(prediction[0],2)
        return render_template('home.html',prediction_text="Flight price: Rs. {}".format(result))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
