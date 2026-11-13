from flask import Flask, render_template_string
import os
app = Flask(__name__)
HTML = """
<!DOCTYPE html>
<html>
<head><title>BiasharaSync</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:Arial;background:#0f172a;color:white;text-align:center;padding:20px}
.card{background:white;color:#0f172a;border-radius:16px;padding:20px;margin:15px auto;max-width:400px}
h1{color:#22c55e}
.btn{background:#22c55e;color:white;padding:12px 20px;border-radius:10px;display:block;margin:10px;text-decoration:none;font-weight:bold}
</style>
</head>
<body>
<h1>BiasharaSync</h1>
<p>Your Business, Synced.</p>
<div class="card"><h2>Today's Sales</h2><h1>KSh 12,450</h1><p>24 Transactions</p></div>
<div class="card"><h2>Stock Alert</h2><p>Maize Flour - Low Stock (3 left)</p><p>Sugar - In Stock (25)</p><p>Cooking Oil - In Stock (18)</p></div>
<div class="card">
<a class="btn" href="#">+ Add Sale</a>
<a class="btn" href="#" style="background:#3b82f6">View Stock</a>
<a class="btn" href="#" style="background:#f59e0b">Reports</a>
</div>
<p>Built by Jesse2583 - Live on Render</p>
</body></html>
"""
@app.route('/')
def home():
    return render_template_string(HTML)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
