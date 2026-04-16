<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">   
    <title>AegisPOS</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
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
        
        /* 📥 UPGRADE 2: Button Styling */
        .btn-download { background: #10b981; color: white; padding: 10px 15px; text-decoration: none; border-radius: 5px; font-weight: bold; transition: 0.3s; }
        .btn-download:hover { background: #059669; }
        .header-controls { text-align: right; }
        .header-controls div { margin-bottom: 8px; color: #64748b; font-size: 0.9rem; }
    </style>
</head>
<body>
    <div class="header">
        <div>
            <h1>AutoHeal POS <span class="badge">v2.0 Enterprise</span></h1>
            <div id="sys-status" class="status">Connecting to WebSockets...</div>
        </div>
        <div class="header-controls">
            <div>SRE Alerting: 🟢 Active | SQL DB: 🟢 Connected</div>
            <a href="/download_report" class="btn-download">⬇️ Download Shift Report</a>
        </div>
    </div>
    
    <div class="grid">
        <div class="card">
            <h2>🔴 Live Kiosk Display</h2>
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

        <div class="card" style="grid-column: 1 / -1;">
            <h2>📈 Live Revenue Analytics</h2>
            <canvas id="revenueChart" height="60"></canvas>
        </div>
    </div>

    <script>
        // 📈 UPGRADE 1: Initialize the Graph
        const ctx = document.getElementById('revenueChart').getContext('2d');
        const revenueChart = new Chart(ctx, {
            type: 'line',
            data: { labels: [], datasets: [{ label: 'Transaction Value ($)', data: [], borderColor: '#3b82f6', backgroundColor: 'rgba(59, 130, 246, 0.2)', borderWidth: 2, fill: true, tension: 0.4 }] },
            options: { responsive: true, scales: { y: { beginAtZero: true, grid: { color: '#334155' }, ticks: { color: '#94a3b8' } }, x: { grid: { color: '#334155' }, ticks: { color: '#94a3b8' } } }, plugins: { legend: { labels: { color: '#f8fafc' } } } }
        });

        const socket = io();
        let lastTxnCount = 0; // Ensures we only plot new transactions

        socket.on('update_data', function(data) {
            document.getElementById('sys-status').innerText = "Status: " + data.status;
            document.getElementById('c-name').innerText = data.latest_name;
            document.getElementById('c-qty').innerText = data.latest_qty;
            document.getElementById('c-price').innerText = "$" + data.latest_price.toFixed(2);
            document.getElementById('c-total').innerText = "$" + data.latest_total.toFixed(2);
            document.getElementById('g-tx').innerText = data.total_transactions;
            document.getElementById('g-items').innerText = data.total_items;
            document.getElementById('g-rev').innerText = "$" + data.total_revenue.toFixed(2);

            // 📈 UPGRADE 1: Add dot to graph if a new transaction occurred
            if (data.total_transactions > lastTxnCount) {
                lastTxnCount = data.total_transactions;
                
                const timeNow = new Date().toLocaleTimeString();
                revenueChart.data.labels.push(timeNow);
                revenueChart.data.datasets[0].data.push(data.latest_total);
                
                // Keep the graph from getting too squished (max 15 dots)
                if(revenueChart.data.labels.length > 15) {
                    revenueChart.data.labels.shift();
                    revenueChart.data.datasets[0].data.shift();
                }
                revenueChart.update();
            }
        });
    </script>
</body>
</html>
