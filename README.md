# Probo Market Price Calculation

This project simulates market pricing logic for a binary opinion market (YES/NO) like Probo. It maintains a live order book and computes metrics like Best Bid, Best Ask, Mid Price, and Weighted Average Price.

---

##  How to Run the Script

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/radhika2208/ProboApp.git
   ```

2. **(Optional) Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the FastAPI Server (if backend):**

   ```bash
   uvicorn main:app --reload
   ```

5. **Open the HTML UI:**

   Open `index.html` in a browser (it interacts with the FastAPI backend).

---

##  Structure of Input

Each order has the following fields:

```json
{
  "price": 10000,
  "quantity": 5,
  "side": "buy",
  "option": "YES"
}
```

Orders are submitted via POST `/orders/`.

---

## Sample Output

On hitting GET `/prices/`, the response looks like:

```json
{
  "best_bid": 10000,
  "best_ask": null,
  "mid_price": null,
  "weighted_avg_price": 10000.0
}
```

- The HTML UI displays these values and updates a real-time chart.

---

## Assumptions & Models Used

- The market operates on a simple **order book** model.
- **Best Bid**: The Best Bid is the highest price at which there is an outstanding buy order. This is the maximum price from all active buy orders in the order book.
- **Best Ask**: The Best Ask is the lowest price at which there is an outstanding sell order. This is the minimum price from all active sell orders in the order book.
- **Mid price** is calculated as the average of Best Bid and Best Ask.
- **Weighted Average Price**: The Weighted Average Price is calculated from all matched buy and sell orders, considering the volume of each order.
---

## 📁 File Structure

```
Probo_project/
│
├── .venv/                           # Virtual environment
│
├── probo_app/                       # Main application package
│   ├── __init__.py
│   ├── order_book_route.py         # API route definitions for order book
│   ├── order_book_service.py       # Core logic for order book operations
│   ├── request_model.py            # Pydantic models for request validation
│
│   ├── static/                      # Static files
│   │   └── style.css               # css styles
│
│   ├── templates/                   # HTML templates
│   │   └── index.html              # UI for order entry and live metrics
│
│   ├── application.py              # FastAPI app startup file
│   ├── README.md                   # Project documentation
│   └── requirements.txt            # Python dependencies
│
├── External Libraries/            
└── Scratches and Consoles/ 
```

---

## Example

### 1. Submit Order:
```bash
POST /orders/
{
  "price": 10000,
  "quantity": 5,
  "side": "buy",
  "option": "YES"
}
```

### 2. Get Price Metrics:
```bash
GET /prices/
```

---

## 🛠️ Technologies Used

- **Python 3**
- **FastAPI** (backend)
- **Chart.js** (frontend graph)
- **HTML/CSS/JS** (UI)

---