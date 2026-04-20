from datetime import datetime, timedelta

class Order:
  _id_counter = 0

  def __init__(self, customer_id, sku_id, quantity=0, order_status="Pending"):
    Order.id_counter += 1
    self.order_id = Order.id_counter
    self.customer_id = customer_id
    self.sku_id = sku_id
    self.quantity = quantity
    self.order_status = order_status
    self.purchase_date = datetime.now()
    self.estimated_delivery = self.purchase_date + timedelta(days=7)
