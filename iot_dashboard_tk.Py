import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# -----------------------
# Simulated Sensor Updates
# -----------------------
def update_values():
    global time_counter
    temperature = random.randint(20, 35)
    humidity = random.randint(30, 70)
    light = random.choice(["ON", "OFF"])

    temp_label.config(text=f"Temperature: {temperature} °C")
    hum_label.config(text=f"Humidity: {humidity} %")
    light_label.config(text=f"Light: {light}")

    # Update graph data
    time_counter += 1
    times.append(time_counter)
    temps.append(temperature)

    if len(times) > 10:  # keep last 10 points
        times.pop(0)
        temps.pop(0)

    # Update graph
    ax.clear()
    ax.plot(times, temps, marker="o", color="blue")
    ax.set_title("Temperature Over Time")
    ax.set_xlabel("Time (ticks)")
    ax.set_ylabel("Temp (°C)")
    canvas.draw()

    # Call again after 2 seconds
    root.after(2000, update_values)

# -----------------------
# Device Control
# -----------------------
def toggle_fan():
    if fan_btn["text"] == "Turn Fan ON":
        fan_btn.config(text="Turn Fan OFF")
        fan_status.config(text="Fan: ON", foreground="green")
    else:
        fan_btn.config(text="Turn Fan ON")
        fan_status.config(text="Fan: OFF", foreground="red")

def toggle_led():
    if led_btn["text"] == "Turn LED ON":
        led_btn.config(text="Turn LED OFF")
        led_status.config(text="LED: ON", foreground="green")
    else:
        led_btn.config(text="Turn LED ON")
        led_status.config(text="LED: OFF", foreground="red")

# -----------------------
# Main Window
# -----------------------
root = tk.Tk()
root.title("IoT Dashboard (Tkinter)")
root.geometry("600x500")

title = ttk.Label(root, text="IoT Dashboard", font=("Arial", 18))
title.pack(pady=10)

# Sensor labels
temp_label = ttk.Label(root, text="Temperature: -- °C", font=("Arial", 14))
temp_label.pack(pady=5)

hum_label = ttk.Label(root, text="Humidity: -- %", font=("Arial", 14))
hum_label.pack(pady=5)

light_label = ttk.Label(root, text="Light: --", font=("Arial", 14))
light_label.pack(pady=5)

# Device Controls
frame = ttk.Frame(root)
frame.pack(pady=10)

fan_btn = ttk.Button(frame, text="Turn Fan ON", command=toggle_fan)
fan_btn.grid(row=0, column=0, padx=10)

fan_status = ttk.Label(frame, text="Fan: OFF", font=("Arial", 12), foreground="red")
fan_status.grid(row=0, column=1)

led_btn = ttk.Button(frame, text="Turn LED ON", command=toggle_led)
led_btn.grid(row=1, column=0, padx=10, pady=5)

led_status = ttk.Label(frame, text="LED: OFF", font=("Arial", 12), foreground="red")
led_status.grid(row=1, column=1)

# Graph
fig, ax = plt.subplots(figsize=(5, 3))
times, temps = [], []
time_counter = 0
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(pady=10)

# Start updating
update_values()

root.mainloop()
