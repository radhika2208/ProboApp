from fastapi import APIRouter

from probo_app.order_book_service import OrderBook
from probo_app.request_model import Order

router = app = APIRouter(
    prefix="",
    tags=["PROBO"],
    responses={404: {"No resource found": "go to /docs for API documentation"}},
)
order_book = OrderBook()
"""
Post the orders
"""


@app.post("/orders/")
async def add_order(order: Order):
    order_book.add_order(order)
    return {"message": "Order added successfully"}


"""
Get real time matrix
"""


@app.get("/prices/")
async def get_all_prices():
    best_bid = order_book.get_best_bid()
    best_ask = order_book.get_best_ask()
    mid_price = order_book.get_mid_price()
    weighted_avg_price = order_book.get_weighted_avg_price()

    response = {
        "best_bid": best_bid if best_bid is not None else "No buy orders",
        "best_ask": best_ask if best_ask is not None else "No sell orders",
        "mid_price": (
            mid_price if mid_price is not None else "Cannot calculate mid price"
        ),
        "weighted_avg_price": (
            weighted_avg_price if weighted_avg_price is not None else "No orders found"
        ),
    }
    return response