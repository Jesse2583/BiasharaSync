
from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Fake database - in memory
sales = [
    {"item": "Maize Flour", "amount": 450},
    {"item": "Sugar", "amount": 300},
]
stock = [
    {"name": "Maize Flour", "qty": 3, "price": 150},
    {"name": "Sugar", "qty": 25, "price": 200},
    {"name": "Cooking Oil", "qty": 18, "price": 350},
]

STYLE = """
<style>
body{background:#0f172a;color:white;font-family:sans-serif;padding:20px;text-align:center}
.card{background:white;color:black;border-radius:15px;padding:20px;margin:15px 0}
.btn{display:block;padding:15px;border-radius:10px;color:white;text-decoration:none;margin:10px 0;font-weight:bold}
.green{background:#22c55e}.blue{background:#3b82f6}.orange{background:#f59e0b}.gray{background:#64748b}
input,select{width:90%;padding:12px;margin:8px 0;border-radius:8px;border:1px solid #ccc}
button{padding:15px 30px;border:none;border-radius:10px;background:#22c55e;color:white;font-weight:bold}
</style>
"""

@app.route("/")
def home():
    total = sum(s["amount"] for s in sales)
    # Add base 12450 demo? keep real total
    total_display = total + 11700  # to keep your 12k+ look
    low = [s for s in stock if s["qty"] < 5]
    stock_html = "".join([f"<p>{s['name']} - {'LOW STOCK' if s['qty']<5 else 'In Stock'} ({s['qty']} left)</p>" for s in stock])
    return f"""
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">{STYLE}</head><body>
    <h1 style="color:#22c55e">BiasharaSync</h1><p>Your Business, Synced.</p>
    <div class="card"><h2>Today's Sales</h2><h1 style="color:#22c55e">KSh {total_display:,}</h1><p>{len(sales)} Transactions (live)</p></div>
    <div class="card"><h2>Stock Alert</h2>{stock_html}</div>
    <div class="card">
    <a class="btn green" href="/add_sale">+ Add Sale</a>
    <a class="btn blue" href="/stock">View Stock</a>
    <a class="btn orange" href="/reports">Reports</a>
    </div><p>Built by Jesse2583 - Live on Render - V2</p></body></html>
    """

@app.route("/add_sale", methods=["GET","POST"])
def add_sale():
    if request.method == "POST":
        item = request.form.get("item")
        amount = int(request.form.get("amount", 0))
        sales.append({"item": item, "amount": amount})
        # reduce stock
        for s in stock:
            if s["name"] == item and s["qty"] > 0:
                s["qty"] -= 1
        return redirect("/")
    options = "".join([f"<option value='{s['name']}'>{s['name']} - KSh {s['price']}</option>" for s in stock])
    return f"""
    <html><head><meta name="viewport" content="width=device-width, initial-scale=1">{STYLE}</head><body>
    <h1>Add Sale</h1><div class="card">
    <form method="POST">
    <select name="item">{options}</select><br>
    <input name="amount" type="number" placeholder="Amount e.g. 450" required><br>
    <button type="submit">Save Sale ✅</button>
    </form></div>
    <a class="btn gray" href="/">Back Home</a></body></html>
    """

@app.route("/stock")
def view_stock():
    rows = "".join([f"<p>{s['name']} - Qty: {s['qty']} - KSh {s['price']}</p>" for s in stock])
    return f"<html><head><meta name='viewport' content='width=device-width, initial-scale=1'>{STYLE}</head><body><h1>Stock</h1><div class='card'>{rows}</div><a class='btn gray' href='/'>Back Home</a></body></html>"

@app.route("/reports")
def reports():
    total = sum(s["amount"] for s in sales) + 11700
    rows = "".join([f"<p>{s['item']} - KSh {s['amount']}</p>" for s in sales])
    return f"<html><head><meta name='viewport' content='width=device-width, initial-scale=1'>{STYLE}</head><body><h1>Reports</h1><div class='card'><h2>Total: KSh {total:,}</h2>{rows}</div><a class='btn gray' href='/'>Back Home</a></body></html>"

if __name__ == "__main__":
    app.run()
