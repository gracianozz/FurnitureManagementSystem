# Artifact Name: support_request_class.py
# Description: Entity class for creating and tracking support request message logs.
# Authors: Gustavo, Mohanad, Nate, Ashfaqh, JaQuan
# Date: April 25, 2026

from datetime import datetime

class SupportRequest:
  _id_counter = 0

  def __init__(self, request_status="Open"):
    SupportRequest._id_counter += 1
    self.request_id = SupportRequest._id_counter
    self.request_status = request_status
    self.message_log = []
    self.date_sent = datetime.now()

  def add_message(self, message):
    timestamp = datetime.now().srftime("%Y-%m-%d %H: %M: %S")
    self.message_log.append(f"[{timestamp}] {message}")
