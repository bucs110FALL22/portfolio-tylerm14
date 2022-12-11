import requests

class jikan:
  def __init__(self, search = None):
    self.url = f"https://api.jikan.moe/v4/characters?q={search}&limit=1&order_by_favorites"

  def get(self):
    r = requests.get(self.url)
    response = r.json()
    return response