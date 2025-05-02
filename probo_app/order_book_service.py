from probo_app.request_model import Order


class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []

    def add_order(self, order: Order):
        if order.side == "buy":
            self.buy_orders.append(order)
        elif order.side == "sell":
            self.sell_orders.append(order)

    def get_best_bid(self):
        best_bid = max(self.buy_orders, key=lambda order: order.price, default=None)
        return best_bid.price if best_bid else None

    def get_best_ask(self):
        best_ask = min(self.sell_orders, key=lambda order: order.price, default=None)
        return best_ask.price if best_ask else None

    def get_mid_price(self):
        best_bid = self.get_best_bid()
        best_ask = self.get_best_ask()
        if best_bid is not None and best_ask is not None:
            return (best_bid + best_ask) / 2
        return None

    def get_weighted_avg_price(self):
        total_value = 0
        total_quantity = 0
        for order in self.buy_orders + self.sell_orders:
            total_value = total_value +(order.price * order.quantity)
            total_quantity = total_quantity + order.quantity
        return total_value / total_quantity if total_quantity > 0 else None