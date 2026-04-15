import os
import subprocess
import time
import random
import pyautogui
import psutil
import threading
import sqlite3
import requests
from flask import Flask, render_template
from flask_socketio import SocketIO

# --- V2 ENTERPRISE SETUP ---
current_directory = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=current_directory)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode='threading')

# --- ENTERPRISE CONFIGURATION ---
DB_NAME = "retail_enterprise.db"
DISCORD_WEBHOOK_URL = "" 

CUSTOMER_NAMES = ["TechCorp Inc.", "Alice Smith", "Global Retail", "John Doe", "Sarah Connor"]

web_data = {
    "total_transactions": 0, "total_items": 0, "total_revenue": 0.0,
    "latest_name": "--", "latest_qty": 0, "latest_price": 0.0, 
    "latest_total": 0.0, "status": "System Online"
}

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions 
                 (txn_id TEXT PRIMARY KEY, customer TEXT, qty INTEGER, price REAL, total REAL, timestamp TEXT)''')
    conn.commit()
    conn.close()

def send_alert(message):
    print(f"⚠️ SRE ALERT: {message}")
    if DISCORD_WEBHOOK_URL:
        try:
            requests.post(DISCORD_WEBHOOK_URL, json={"content": f"🚨 **AutoHeal POS Alert:** {message}"})
        except:
            pass

def focus_window(app_name):
    for win in pyautogui.getAllWindows():
        if app_name.lower() in win.title.lower():
            try:
                if win.isMinimized: win.restore()
                win.activate()
                time.sleep(0.5) 
                return True
            except Exception: pass
    return False

def monitor_and_heal():
    if "calc.exe" not in (p.name().lower() for p in psutil.process_iter()):
        send_alert("Calculator process died. Executing Self-Healing restart...")
        subprocess.Popen("calc.exe")
        time.sleep(1)

    all_titles = [w.title for w in pyautogui.getAllWindows()]
    if not any("Notepad" in t for t in all_titles):
        send_alert("Visual Display (Notepad) closed. Executing Self-Healing restart...")
        subprocess.Popen("notepad.exe")
        time.sleep(1)

def run_retail_automation():
    global web_data
    
    # 1. Generate Data
    name = random.choice(CUSTOMER_NAMES)
    quantity = random.randint(1, 5) 
    avg_price = round(random.uniform(12.50, 89.99), 2) 
    total = round(quantity * avg_price, 2)
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    client_id = f"TXN-{random.randint(1000, 9999)}"

    # 2. SAVE TO SQL DATABASE
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?)", 
              (client_id, name, quantity, avg_price, total, timestamp))
    conn.commit()
    conn.close()

    # 3. UPDATE STATE
    web_data["total_transactions"] += 1
    web_data["total_items"] += quantity
    web_data["total_revenue"] += total
    web_data["latest_name"] = name
    web_data["latest_qty"] = quantity
    web_data["latest_price"] = avg_price
    web_data["latest_total"] = total
    web_data["status"] = "Processing..."

    # Pushes data instantly to the frontend.
    socketio.emit('update_data', web_data)

    # 4. VISUAL RPA (Calculator)
    if focus_window('calculator') or focus_window('calc'):
        pyautogui.press('esc') 
        time.sleep(0.5)
        pyautogui.write(str(quantity), interval=0.15)
        time.sleep(0.3)
        pyautogui.press('*')
        time.sleep(0.3)
        pyautogui.write(str(avg_price), interval=0.15)
        time.sleep(1.5) 
        pyautogui.press('enter')
        time.sleep(0.5) 

    # 5. VISUAL RPA (Notepad) - EXACT CHANGE APPLIED HERE
    if focus_window('notepad'):
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.1)
        pyautogui.press('backspace')
        time.sleep(0.1)
        
        # Failsafe: Ensures the shift key isn't virtually "stuck"
        pyautogui.keyUp('shift') 
        
        receipt = (
            f"=================================\n"
            f"      AUTOHEAL SMART KIOSK       \n"
            f"=================================\n"
            f"  TXN ID     : {client_id}\n"
            f"  Customer   : {name}\n"
            f"---------------------------------\n"
            f"  Quantity   : {quantity} items\n"
            f"  Unit Price : ${avg_price:.2f}\n"
            f"---------------------------------\n"
            f"  TOTAL DUE  : ${total:.2f}\n"
            f"=================================\n"
            f"     STATUS: SECURED IN SQL      \n"
        )
        
        # Slowed down from 0.005 to 0.02 to stop the Shift-Key glitch
        pyautogui.write(receipt, interval=0.02)

    time.sleep(1.5)
    web_data["status"] = "Waiting for next customer..."
    socketio.emit('update_data', web_data)

def bot_loop():
    init_db() 
    time.sleep(2) 
    while True:
        monitor_and_heal()
        run_retail_automation()
        time.sleep(4) 

@app.route('/')
def dashboard():
    return render_template('index.html')

if __name__ == "__main__":
    threading.Thread(target=bot_loop, daemon=True).start()
    print("AutoHeal POS Enterprise Started!")
    socketio.run(app, port=5001, debug=False, use_reloader=False)
