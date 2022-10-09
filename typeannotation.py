def total_price_1item(unit_price: int, quantity: int,) -> int:
  total_price = unit_price * quantity
  return total_price
total_price = total_price_1item(130, 3)
print(total_price)