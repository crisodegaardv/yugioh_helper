class Card():
  def __init__(self, name, description, card_type, card_id=None):
    self.id = card_id
    self.name = name
    self.description = description
    self.card_type = card_type
    
  def show_card_data(self):
    print(f"Card Name: {self.name} | Card Description: {self.description} | Card Type: {self.card_type}")
    
