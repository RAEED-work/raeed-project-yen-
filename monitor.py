import os
import subprocess
import time
import random
import pyautogui
import psutil
import threading
from flask import Flask, render_template, jsonify

# --- FLASK SETUP (Flat Folder) ---
current_directory = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=current_directory)

# --- FILE CONFIGURATION ---
RETAIL_DATA = "retail_data.txt"
SYSTEM_LOGS = "system_logs.txt"

# --- LOGICAL DATA ASSETS ---
# To make the data realistic and logical as requested
CUSTOMER_NAMES = ["TechCorp Inc.", "Alice Smith", "Global Retail", "John Doe", "Sarah Connor", "Wayne Enterprises", "Local Cafe", "David Wilson"]

# --- WEB DASHBOARD STATE ---
web_data = {
    "total_transactions": 0,
    "total_items": 0,
    "total_revenue": 0.0,
    "latest_name": "--",
    "latest_qty": 0,
    "latest_price": 0.0,
    "latest_total": 0.0,
    "status": "System Online"
}

def monitor_and_heal():
    """Self-Healing: Ensures ONLY Calculator and ONE Notepad are open."""
    # 1. Check Calculator
    if "calc.exe" not in (p.name().lower() for p in psutil.process_iter()):
        subprocess.Popen("calc.exe")
        time.sleep(0.5)

    # 2. Check for ONE Notepad (Live Display)
    all_titles = [w.title for w in pyautogui.getAllWindows()]
    if not any("Notepad" in t for t in all_titles):
        subprocess.Popen("notepad.exe")
        time.sleep(0.5)

def run_retail_automation():
    """Generates logical data, types it visually, saves it silently, and sends to Web."""
    global web_data
    
    # 1. GENERATE LOGICAL DATA
    name = random.choice(CUSTOMER_NAMES)
    quantity = random.randint(1, 20)
    avg_price = round(random.uniform(15.0, 99.99), 2)
    total = round(quantity * avg_price, 2)
    timestamp = time.strftime('%H:%M:%S')

    # 2. SILENT BACKGROUND SAVING (No windows pop up for these)
    with open(RETAIL_DATA, "a") as f:
        f.write(f"[{timestamp}] Customer: {name} | Qty: {quantity} | Avg Price: ${avg_price} | Total: ${total}\n")
    with open(SYSTEM_LOGS, "a") as f:
        f.write(f"[{timestamp}] Processed transaction for {name} successfully.\n")

    # 3. UPDATE WEB DASHBOARD STATE
    web_data["total_transactions"] += 1
    web_data["total_items"] += quantity
    web_data["total_revenue"] += total
    web_data["latest_name"] = name
    web_data["latest_qty"] = quantity
    web_data["latest_price"] = avg_price
    web_data["latest_total"] = total
    web_data["status"] = "Processing..."

    # 4. VISUAL RPA (Calculator)
    calc_wins = [w for w in pyautogui.getAllWindows() if 'Calculator' in w.title]
    if calc_wins:
        calc_wins[0].activate()
        pyautogui.write(str(quantity))
        pyautogui.press('*')
        pyautogui.write(str(avg_price))
        pyautogui.press('enter')

    # 5. VISUAL RPA (The single Live Notepad)
    notepad_wins = [w for w in pyautogui.getAllWindows() if 'Notepad' in w.title]
    if notepad_wins:
        notepad_wins[0].activate()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('backspace')
        pyautogui.write(f"=== PROJECT 36 LIVE KIOSK ===\n")
        pyautogui.write(f"Customer Name : {name}\n")
        pyautogui.write(f"Items Bought  : {quantity}\n")
        pyautogui.write(f"Average Price : ${avg_price}\n")
        pyautogui.write(f"-----------------------------\n")
        pyautogui.write(f"FINAL TOTAL   : ${total}\n")
        pyautogui.write(f"=============================\n")

    time.sleep(1)
    web_data["status"] = "Waiting for next customer..."

def bot_loop():
    """The background thread running the visual bot."""
    time.sleep(2) # Give web server a moment to start
    while True:
        monitor_and_heal()
        run_retail_automation()
        time.sleep(5) # 5 seconds between transactions

# --- FLASK WEB ROUTES ---
@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/data')
def api_data():
    return jsonify(web_data)

if __name__ == "__main__":
    threading.Thread(target=bot_loop, daemon=True).start()
    print("Project 36 Monitor Started!")
    print("Open your browser to: http://127.0.0.1:5001")
    app.run(port=5001, debug=False, use_reloader=False)