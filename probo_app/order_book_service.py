from probo_app.request_model import Order


class OrderBook:
    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []
        self.yes_bets = 0
        self.no_bets = 0
        self.weight_factor = 1

    def add_order(self, order: Order):
        """
        order added to order book and updating the total sell,buy price
        along with the yes/no bets
        :param order: BaseModel Order
        :return: None
        """
        if order.side == "buy":
            self.buy_orders.append(order)
        elif order.side == "sell":
            self.sell_orders.append(order)
        if order.option.upper() == "YES":
            self.yes_bets = self.yes_bets + order.quantity
        if order.option.upper() == "NO":
            self.no_bets = self.no_bets + order.quantity

    def get_best_bid(self):
        """
        get best bid as maximum price of order buy
        :return: best bid
        """
        best_bid = max(self.buy_orders, key=lambda order: order.price, default=None)
        return best_bid.price if best_bid else None

    def get_best_ask(self):
        """
        get best ask as minimum price of order sell
        :return: best ask
        """
        best_ask = min(self.sell_orders, key=lambda order: order.price, default=None)
        return best_ask.price if best_ask else None

    def get_spread(self):
        """
        get spread as best bid - best ask
        :return: spread
        """
        bid = self.get_best_bid()
        ask = self.get_best_ask()
        return round(ask - bid, 1) if bid and ask else None

    def get_mid_price(self):
        """
        get mid price as average of best bid and best ask
        :return: mid price
        """
        best_bid = self.get_best_bid()
        best_ask = self.get_best_ask()
        if best_bid is not None and best_ask is not None:
            return (best_bid + best_ask) / 2
        return None

    def get_weighted_avg_price(self):
        """
        calculates the weighted average price of all orders (both buy and sell).
        The weighted average price is determined by:
        (sum of price * quantity for all orders) / (sum of quantities)
        :return: weighted average price
        """
        total_value = 0
        total_quantity = 0
        for order in self.buy_orders + self.sell_orders:
            total_value = total_value +(order.price * order.quantity)
            total_quantity = total_quantity + order.quantity
        return total_value / total_quantity if total_quantity > 0 else None

    def get_yes_price(self):
        """
        get yes price on the scale of 10
        :return: yes price
        """
        total = self.yes_bets + self.no_bets
        if total == 0:
            return 5.0
        yes_prob = self.yes_bets / total
        return round(yes_prob * 10, 1)

    def get_no_price(self):
        """
        get no price on the scale of 10
        :return: no price
        """
        total = self.yes_bets + self.no_bets
        if total == 0:
            return 5.0
        no_prob = self.no_bets / total
        return round(no_prob * 10, 1)