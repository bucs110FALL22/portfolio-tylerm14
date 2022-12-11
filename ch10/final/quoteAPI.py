import requests

class getQuote:
  def __init__(self, title = None):
    self.url = f"https://animechan.vercel.app/api/random/anime?title={title}"

  def get(self):
    r = requests.get(self.url)
    response = r.json()
    return response
    