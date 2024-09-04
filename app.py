from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import os
import ssl

app = Flask(__name__, template_folder="template", static_url_path='/static')

def connect_to_database():
    try:
        client = MongoClient('mongodb+srv://Amala203145:Amala2031456@cluster0.t9ibfge.mongodb.net/?retryWrites=true&w=majority')
        db = client['Cluster0']
        print("Database connection successful")
        return db  # Return the database client
    except Exception as e:
        print("Failed to connect to database:", e)
        return None

def save_booking_details(booking_details):
    try:
        db = connect_to_database()
        if db:
            collection = db['bookings']
            result = collection.insert_one(booking_details)
            if result.inserted_id:
                print("Booking details saved successfully")
                return True
            else:
                print("Failed to save booking details")
                return False
    except Exception as e:
        print("Error saving booking details:", e)
        return False

def get_booking_details():
    try:
        db = connect_to_database()
        if db is not None:
            collection = db['bookings']
            booking_details = collection.find_one()
            if booking_details:
                return booking_details
            else:
                print("No booking details found")
                return {}
        else:
            print("Failed to connect to database")
            return {}
    except Exception as e:
        print("Error getting booking details:", e)
        return None
    
@app.route('/')
def home():
    return render_template("index.html")
    
@app.route('/confirmation')
def confirmation():
    booking_details = get_booking_details() 
    return render_template('confirmation.html', booking_details=booking_details)
    
@app.route('/tc')
def tc():
    return render_template('tc.html')

@app.route('/paid_payment')
def paid_payment():
    return render_template('paidpayment.html')

@app.route('/vehicle_payment')
def vehicle_payment():
    return render_template('vehicle_payment.html')

@app.route('/room_payment')
def room_payment():
    return render_template('room_payment.html')
    
@app.route('/roombooking')
def roombooking():
    return render_template('roombooking.html')
    
@app.route('/kanaka_durgamma')
def kanaka_durgamma():
    return render_template("kanaka_durgamma.html")

@app.route('/tirupathi_deva')
def tirupathi_deva():
    return render_template("tirupathi_deva.html")

@app.route('/srilakshmitirupathiamma')
def srilakshmitirupathiamma():
    return render_template("srilakshmitirupathiamma.html")

@app.route('/paiddarshan')
def paid_darshan():
    return render_template("paiddarshan.html")

@app.route('/free_darshan')
def free_darshan():
    return render_template("free_darshan.html")

@app.route('/vehicle')
def vehicle_parking():
    return render_template("vehicle.html")

@app.route('/roombooking')
def room_booking():
    return render_template("roombooking.html")

@app.route('/prasadbooking')
def prasad_booking():
    return render_template("prasadbooking.html")

@app.route('/vip_darshan')
def vip_darshan():
    return render_template("vip_darshan.html")

@app.route('/foodbooking')
def food_booking():
    return render_template("foodbooking.html")

@app.route('/taxibooking')
def taxi_booking():
    return render_template("taxibooking.html")

@app.route('/save_booking', methods=['POST'])
def save_booking():
    try:
        booking_details = request.json
        if save_booking_details(booking_details):
            return jsonify({'message': 'Booking details saved successfully!'}), 200
        else:
            return jsonify({'error': 'Failed to save booking details.'}), 500
    except Exception as e:
        print("Error saving booking:", e)
        return jsonify({'error': 'Failed to save booking details. Invalid data format.'}), 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4450))
    app.run(host='0.0.0.0', port=port, debug=True)
