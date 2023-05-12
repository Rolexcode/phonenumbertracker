from flask import Flask, render_template, request
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    number = request.form['number']
    phone_number = phonenumbers.parse(number)
    location = geocoder.description_for_number(phone_number, 'en')
    carrier_name = carrier.name_for_number(phone_number, 'en')
    time_zone = timezone.time_zones_for_number(phone_number)
    return render_template('result.html', location=location, carrier_name=carrier_name, time_zone=time_zone)

if __name__ == '__main__':
    app.run(debug=True)
