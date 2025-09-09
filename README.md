## **📊 IoT Dashboard (Flask + Tkinter Simulation)**

### 🚀 Project Overview
This project is an **IoT Dashboard** originally built with **Flask** and **MySQL** to visualize and log sensor/device data.  
Since the original codebase focused on a web dashboard, we extended it by adding a **Tkinter simulation file** so that the project can also display data in a **desktop GUI**.

---

## ⚙️** Setup Instructions**

### 1️⃣ Clone the Repository
git clone https://github.com/marthanjoel/IoT-Dashboard-iot.git
cd IoT-Dashboard-iot

###2️⃣ Create Virtual Environment & Install Dependencies
python3 -m venv venv
source venv/bin/activate
pip install flask mysql-connector-python passlib pillow
sudo apt-get install python3-tk

###3️⃣ Setup Database
Login to MySQL:
sudo mysql
Then run:
sql
CREATE DATABASE iot_dashboard;
CREATE USER 'aman'@'localhost' IDENTIFIED BY 'aman';
GRANT ALL PRIVILEGES ON iot_dashboard.* TO 'aman'@'localhost';
FLUSH PRIVILEGES;
EXIT;
Import schema:
mysql -u aman -p iot_dashboard < "Database Script.sql"

###4️⃣ Run the Flask App
python3 Arms.py
Visit http://localhost:5000 to see the web dashboard.

##**🖥️ Tkinter Simulation**
I created a new file tk_dashboard.py to visualize IoT sensor values in a desktop GUI.

Run Tkinter Simulation:
python3 tk_dashboard.py
This opens a Tkinter window that simulates:

🌡️ Temperature readings

💧 Humidity readings

📡 Real-time updates every 2 seconds

----
##🔍 **Challenges Faced**
1.Flask app originally failed due to version mismatches (werkzeug, flask, markupsafe).

2.Database login errors with MySQL users.

3.Had to downgrade Flask & dependencies to match project code.

4.Tkinter not part of the original repo — we had to install and code it manually.


##🛰️ **Devices / Sensors Emulated**
Temperature sensor (simulated values in Tkinter GUI)

Humidity sensor (simulated values in Tkinter GUI)

IoT device logs stored in MySQL (via Flask backend)


##**💡 Future Improvements**
Connect Tkinter GUI directly to live MySQL values.

Add more sensors (light, motion, fan control).

Build MQTT integration for real IoT devices.

Containerize with Docker for easy deployment.
