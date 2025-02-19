import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        # Test the getDataPoint function for calculating price based on bid and ask prices
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        
        # Arrange
        expected_data_point = ('ABC', 120.48, 121.2, 120.84)  # Expected output

        # Act
        data_point = getDataPoint(quotes[0])  # Call the method with a quote

        # Assert
        self.assertEqual(data_point, expected_data_point)  # Check if the actual output matches the expected output

    
    
    
    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        # Test the getDataPoint function for calculating price when bid price is greater than ask price
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        
        # Arrange
        expected_data_point = ('ABC', 120.48, 119.2, 119.84)  # Expected output

        # Act
        data_point = getDataPoint(quotes[0])  # Call the method with a quote

        # Assert
        self.assertEqual(data_point, expected_data_point)  # Check if the actual output matches the expected output

    
    
    
    #additional test cases:
    
    def test_getRatio_priceBZero(self):
        # Test case for calculating ratio when price B is zero
        # Arrange
        price_a = 120.48
        price_b = 0
        expected_ratio = float('inf')  # Expected output

        # Act
        ratio = getRatio(price_a, price_b)  # Call the method with the given prices

        # Assert
        self.assertEqual(ratio, expected_ratio)  # Check if the actual output matches the expected output

    def test_getRatio_priceAZero(self):
        # Test case for calculating ratio when price A is zero
        # Arrange
        price_a = 0
        price_b = 121.2
        expected_ratio = 0  # Expected output

        # Act
        ratio = getRatio(price_a, price_b)  # Call the method with the given prices

        # Assert
        self.assertEqual(ratio, expected_ratio)  # Check if the actual output matches the expected output
        
if __name__ == '__main__':
    unittest.main()
    
    
    
