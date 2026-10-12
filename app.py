from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def home():
    return """<!DOCTYPE html><html><head><title>FRM Rice Mill - Keeri Samba, Naadu, White, Samba</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{font-family:Arial;background:#fdfcf5;margin:0}.nav{padding:16px 5%;display:flex;justify-content:space-between;background:white;box-shadow:0 1px 0 #eee;align-items:center} .hero{background:linear-gradient(135deg,#1b5e20,#2e7d32);color:white;text-align:center;padding:80px 20px} .btn{background:#d4af37;color:#000;padding:12px 24px;border-radius:25px;text-decoration:none;font-weight:bold;display:inline-block;margin:10px} .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;padding:40px 5%} .card{background:white;border-radius:16px;overflow:hidden;box-shadow:0 8px 20px rgba(0,0,0,0.08)} .card img{width:100%;height:200px;object-fit:cover} .card div{padding:16px}</style></head><body>
<div class="nav"><b style="color:#1b5e20">FRM RICE MILL - EST 2010</b><a href="https://wa.me/94764915323" style="background:#25D366;color:white;padding:8px 16px;border-radius:20px;text-decoration:none;font-weight:600">WhatsApp</a></div>
<div class="hero"><h1>Keeri Samba, Naadu, White & Samba Rice</h1><p>Direct From Mill - Pure Ceylon Rice Since 2010</p><a href="https://wa.me/94764915323" class="btn">Order on WhatsApp →</a></div>
<div class="grid">
<div class="card"><img src="https://images.unsplash.com/photo-1586201375761-83865001e31c?w=400"><div><h3>Keeri Samba</h3><p>Fragrant Wedding Rice</p><b>Rs. 420/kg</b></div></div>
<div class="card"><img src="https://images.unsplash.com/photo-1536304929831-ee1ca9d44906?w=400"><div><h3>Naadu Rice</h3><p>Daily Healthy Rice</p><b>Rs. 280/kg</b></div></div>
<div class="card"><img src="https://images.unsplash.com/photo-1616684004084-68c93db45211?w=400"><div><h3>White Raw Rice</h3><p>Clean Family Favorite</p><b>Rs. 300/kg</b></div></div>
<div class="card"><img src="https://images.unsplash.com/photo-1608198093002-ad4e005484ec?w=400"><div><h3>Samba Rice</h3><p>Traditional & Nutritious</p><b>Rs. 350/kg</b></div></div>
</div>
<div style="text-align:center;padding:40px;background:#0f1d0f;color:white"><h2>FRM RICE MILL</h2><p>📱 +94 76 4915323 | Island-wide Delivery</p><p>Keeri Samba • Naadu • White Rice • Samba</p><br><a href="https://wa.me/94764915323" class="btn" style="background:#25D366;color:white">💬 WhatsApp Order</a></div>
</body></html>"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8000)))
