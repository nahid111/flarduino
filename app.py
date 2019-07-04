import serial, time
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	port = request.form['serialport']
	baudrate = request.form['baudrate']
	ser = serial.Serial(port, baudrate = baudrate, timeout=1)
	t_end = time.time() + 60 * 0.1
	lst = []
	while time.time() < t_end:
		arduinoData = ser.readline().decode('ascii')
		lst.append(arduinoData)
	return render_template('index.html', lst=lst)



if __name__=='__main__':
	app.run( host='0.0.0.0', port=5000, debug=True )


