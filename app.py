from flask import Flask,render_template,request
import pandas as pd,pickle

app=Flask(__name__,template_folder='./templates',static_folder='./static')

model=pickle.load(open('./models/model.pkl','rb'))
preprocesor=pickle.load(open('./models/preprocessor.pkl','rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=["POST"])
def predict():
    if request.method=="POST":
        Delivery_person_Age=int(request.form['Delivery_person_Age'])
        Delivery_person_Ratings=float(request.form['Delivery_person_Ratings'])
        Weatherconditions=request.form['Weatherconditions']
        Road_traffic_density=request.form['Road_traffic_density']
        Vehicle_condition=int(request.form['Vehicle_condition'])
        Type_of_order=request.form['Type_of_order']
        Type_of_vehicle=request.form['Type_of_vehicle']
        multiple_deliveries=int(request.form['multiple_deliveries'])
        Festival=int(request.form['Festival'])
        City=request.form['City']

        
        from datetime import datetime

        order_time = datetime.strptime(request.form["Time_Orderd"], "%H:%M")

        Ordered_Hour = order_time.hour
        Ordered_Minutes = order_time.minute

        picked_time=datetime.strptime(request.form['Time_Order_picked'],"%H:%M")

        Picked_Hour=picked_time.hour
        Picked_Minutes=picked_time.minute

        order_date=datetime.strptime(request.form['Order_Date'],"%Y-%m-%d")

        Order_Day=order_date.day
        Order_Month=order_date.month
        Order_Day_of_Week=order_date.weekday()

        Distance=float(request.form['Distance'])

        data = pd.DataFrame([{
            "Delivery_person_Age": Delivery_person_Age,
            "Delivery_person_Ratings": Delivery_person_Ratings,
            "Weatherconditions": Weatherconditions,
            "Road_traffic_density": Road_traffic_density,
            "Vehicle_condition": Vehicle_condition,
            "Type_of_order": Type_of_order,
            "Type_of_vehicle": Type_of_vehicle,
            "multiple_deliveries": multiple_deliveries,
            "Festival": Festival,
            "City": City,
            "Ordered_Hour": Ordered_Hour,
            "Ordered_Minutes": Ordered_Minutes,
            "Picked_Hour": Picked_Hour,
            "Picked_Minutes": Picked_Minutes,
            "Order_Day": Order_Day,
            "Order_Month": Order_Month,
            "Order_Day_of_Week": Order_Day_of_Week,
            "Distance": Distance
        }])

        data=preprocesor.transform(data)
        prediction = round(model.predict(data)[0], 2)

        return render_template('index.html',prediction=prediction)
    else :
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)