<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AutoHeal POS Enterprise</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #0f172a; color: #f8fafc; padding: 2rem; margin: 0; }
        .header { background: #1e293b; padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem; border-left: 6px solid #3b82f6; display: flex; justify-content: space-between; align-items: center;}
        .header h1 { margin: 0; font-size: 1.8rem; }
        .badge { background: #3b82f6; color: white; padding: 5px 10px; border-radius: 5px; font-size: 0.9rem; margin-left: 10px;}
        .status { color: #10b981; font-weight: bold; }
        .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
        .card { background: #1e293b; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
        .card h2 { margin-top: 0; color: #94a3b8; font-size: 1.2rem; border-bottom: 1px solid #334155; padding-bottom: 10px; }
        .receipt-row { display: flex; justify-content: space-between; margin: 15px 0; font-size: 1.2rem; }
        .receipt-total { display: flex; justify-content: space-between; margin-top: 20px; font-size: 1.8rem; font-weight: bold; color: #3b82f6; border-top: 2px dashed #475569; padding-top: 20px; }
        .stat-box { background: #0f172a; padding: 15px; border-radius: 8px; margin-bottom: 15px; text-align: center; }
        .stat-value { font-size: 2rem; font-weight: bold; color: #10b981; margin-top: 5px; }
    </style>
</head>
<body>
    <div class="header">
        <div>
            <h1>AutoHeal POS <span class="badge">v2.0 Enterprise</span></h1>
            <div id="sys-status" class="status">Connecting to WebSockets...</div>
        </div>
        <div style="text-align: right; color: #64748b; font-size: 0.9rem;">
            <div>SRE Alerting: 🟢 Active</div>
            <div>SQL Database: 🟢 Connected</div>
        </div>
    </div>
    <div class="grid">
        <div class="card">
            <h2>🔴 Live Kiosk Display (WebSocket Sync)</h2>
            <div class="receipt-row"><span>Customer Name:</span><span id="c-name">--</span></div>
            <div class="receipt-row"><span>Items Bought:</span><span id="c-qty">0</span></div>
            <div class="receipt-row"><span>Average Price:</span><span id="c-price">$0.00</span></div>
            <div class="receipt-total"><span>FINAL TOTAL:</span><span id="c-total">$0.00</span></div>
        </div>
        <div class="card">
            <h2>📊 Overall Shift Metrics</h2>
            <div class="stat-box"><div>Total Transactions</div><div class="stat-value" id="g-tx" style="color: #f59e0b;">0</div></div>
            <div class="stat-box"><div>Total Items Sold</div><div class="stat-value" id="g-items" style="color: #a855f7;">0</div></div>
            <div class="stat-box"><div>Gross Revenue</div><div class="stat-value" id="g-rev" style="color: #10b981;">$0.00</div></div>
        </div>
    </div>

    <script>
        // Connect to the WebSocket server
        const socket = io();

        // Listen for the 'update_data' event from Python
        socket.on('update_data', function(data) {
            document.getElementById('sys-status').innerText = "Status: " + data.status;
            document.getElementById('c-name').innerText = data.latest_name;
            document.getElementById('c-qty').innerText = data.latest_qty;
            document.getElementById('c-price').innerText = "$" + data.latest_price.toFixed(2);
            document.getElementById('c-total').innerText = "$" + data.latest_total.toFixed(2);
            document.getElementById('g-tx').innerText = data.total_transactions;
            document.getElementById('g-items').innerText = data.total_items;
            document.getElementById('g-rev').innerText = "$" + data.total_revenue.toFixed(2);
        });
    </script>
</body>
</html>
