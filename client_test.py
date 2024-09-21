import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      expected_price = (bid_price + ask_price) / 2
      self.assertEqual(price, expected_price, f"Failed on quote {quote}")



  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      stock, bid_price, ask_price, price = getDataPoint(quote)
      expected_price = (bid_price + ask_price) / 2
      self.assertEqual(price, expected_price, f"Failed on quote {quote}")

def test_getRatio(self):
  # Normal scenario where price_b is not zero
  price_a = 120.5
  price_b = 121.0
  self.assertAlmostEqual(getRatio(price_a, price_b), price_a / price_b, places=5, msg="Ratio calculation failed for normal case")

  # Edge case where price_b is zero
  price_a = 120.5
  price_b = 0
  self.assertIsNone(getRatio(price_a, price_b), "Ratio should be None when price_b is zero")

def test_getRatio_reverse(self):
  # Check if ratio calculation handles reversed values
  price_a = 121.0
  price_b = 120.5
  self.assertAlmostEqual(getRatio(price_a, price_b), price_a / price_b, places=5, msg="Ratio calculation failed for reversed case")


if __name__ == '__main__':
    unittest.main()
