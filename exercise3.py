"""Exercise 3: Enforce a business rule.

Extend your Cart so invalid operations are rejected by the CART.

  ValueError        when qty < 1
  OutOfStockError   when the item's "available" field is False
  KeyError          when removing an item that is not in the cart

Then demonstrate each one with try/except.
"""

from exercise1 import load_menu


class OutOfStockError(Exception):
    """Raised when a customer tries to order an item that is unavailable."""
    pass


class Cart:
    def __init__(self) -> None:
        self.lines: list[dict] = []

    def add_item(self, item: dict, qty: int ) -> None:
        
        if qty <=0:
            raise ValueError("Invalid number quantatity input")
        if not item["available"]:
            raise OutOfStockError
        item_inline = {"item_id":item["id"],"name": item["name"],"price":item["price"],"qty":qty}
        
        if len(self.lines)!=0:
            for inCart in self.lines:
                if item["name"] in inCart["name"]:
                    inCart["qty"] +=qty
                    return
        self.lines.append(item_inline)                        
        # TODO: validate FIRST, then mutate.
        #   if qty < 1:                 raise ValueError(...)
        #   if not item["available"]:   raise OutOfStockError(...)
        

    def remove_item(self, item_id: int) -> None:
         if item_id not in self.lines:
             raise KeyError
        # TODO: raise KeyError if the item is not in the cart
        

    def total(self) -> float:
        return round(sum(line["price"] * line["qty"] for line in self.lines), 2)

    def __repr__(self) -> str:
        return f"<Cart {len(self.lines)} items, ${self.total():.2f}>"


if __name__ == "__main__":
    menu = load_menu()
    gyoza = menu[1]           # available
    miso = menu[3]            # NOT available

    cart = Cart()
    try:
        cart.add_item(gyoza,0)
        #cart.add_item(miso,3)
    except ValueError as e:
        print(f"rejected: {e}")
    # TODO: demonstrate each rejection with try/except and a readable message.
    # Example:
    # try:
    #     cart.add_item(gyoza, 0)
    # except ValueError as e:
    #     print(f"Rejected: {e}")

