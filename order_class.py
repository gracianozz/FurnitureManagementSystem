# Artifact Name: order_class.py
# Description: Entity class representing individual furniture orders and tracking data.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026

from datetime import datetime, timedelta
import csv

class Order:
  _id_counter = 0

  def __init__(self, customer_id, sku_id, quantity=0, order_status="Pending"):
    Order._id_counter += 1
    self.order_id = Order._id_counter
    self.customer_id = customer_id
    self.sku_id = sku_id
    self.quantity = quantity
    self.order_status = order_status
    self.purchase_date = datetime.now()
    self.estimated_delivery = self.purchase_date + timedelta(days=7)

  # Prints all orders made by the selected customer
  @classmethod
  def viewOrders(cls, customer_id):
    found = []
    with open("Orders/orders.csv", "r") as file:
      reader = csv.DictReader(file)
      for row in reader:
        if int(row["CustomerID"]) == customer_id:
          found.append(row)

    if not found:
      print("You have no orders.")
      return

    print(f"\n--- Your Orders ({len(found)} found) ---")
    for order in found:
      print(f"Order ID:           {order['OrderID']}")
      print(f"Item (SKU):         {order['SKU_ID']}")
      print(f"Status:             {order['OrderStatus']}")
      print(f"Purchase Date:      {order['PurchaseDate']}")
      print(f"Estimated Delivery: {order['EstimatedDelivery']}")
      print("-" * 35)
    
