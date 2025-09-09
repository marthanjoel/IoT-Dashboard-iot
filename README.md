### **IoT Dashboard**

A simple IoT Dashboard built with **Flask** (backend) and **Tkinter** (desktop UI) that allows monitoring and controlling IoT devices.  
The system integrates **MySQL** for data storage and provides real-time visualization of temperature, humidity, and device states.

---

## **🚀 Features**
- 📊 Real-time monitoring of temperature & humidity  
- 💡 Control devices like Fan & LED (ON/OFF)  
- 🗄️ MySQL database integration for storing sensor data  
- 📈 Graphs for temperature trends  
- 🖥️ Tkinter GUI for local visualization  
- 🌐 Flask-based web interface for remote access  




## **⚙️ Tech Stack**
- **Python 3**  
- **Flask**  
- **Tkinter**  
- **MySQL**  
- **Matplotlib**  
- **Passlib** (for authentication)  




## **🛠️ Setup Instructions**
1. Clone the repository:

   git clone https://github.com/marthanjoel/IoT-Dashboard-iot.git
   cd IoT-Dashboard-iot
Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate   # Linux/Mac

Install dependencies:
pip install -r requirements.txt
Setup MySQL:

CREATE DATABASE iot_dashboard;
CREATE USER 'aman'@'localhost' IDENTIFIED BY 'aman';
GRANT ALL PRIVILEGES ON iot_dashboard.* TO 'aman'@'localhost';
FLUSH PRIVILEGES;

Import tables:
mysql -u aman -p iot_dashboard < "Database Script.sql"
Run Flask app:

python3 Arms.py
Open browser at:
👉 http://127.0.0.1:5000

⚡ How the Simulation Works
Sensors are emulated: Random values are generated for temperature and humidity.

Database storage: Each reading is stored inside MySQL for historical tracking.

Actuator control: Buttons simulate controlling a Fan and LED light (status is shown as ON/OFF).

Visualization: Tkinter + Matplotlib display a real-time graph of temperature trends.

Web dashboard: Flask serves the same data through a browser interface.



##**🔧 Challenges Faced**
Compatibility issues between Flask and newer versions of Werkzeug and MarkupSafe.

MySQL authentication errors (Access denied for user 'aman'@'localhost') fixed by updating user permissions.

Installing missing Python libraries (passlib, mysql-connector-python, Pillow).

Permission issues when running Flask on port 80 (solved by switching to port 5000).



##**🛰️ Sensors & Devices Emulated**
🌡️ Temperature Sensor (random values between 20°C – 40°C)

💧 Humidity Sensor (random values between 40% – 80%)

🌀 Fan (Actuator) — ON/OFF simulation

💡 LED (Actuator) — ON/OFF simulation



##**💡 Future Improvements**
Integrate with real hardware (ESP32, Arduino, or Raspberry Pi).

Use MQTT protocol to stream sensor data instead of random values.

Add user authentication & roles for secure dashboard access.

Store long-term data in a time-series database (e.g., InfluxDB).

Deploy with Docker for easy portability.

Improve UI/UX with React or Vue for the web frontend.

👨‍💻 Author
Joel Marthan Lutwama
GitHub: @marthanjoel

yaml
Copy code
