import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTest(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product 2')
        self.assertEqual(prod.weight, 20)

    def test_nondefault_product_stealability_explode(self):
        """Test stealability and explode."""
        prod = Product('Test Product 3', price=2, flammability=3.0)
        self.assertEqual(prod.stealability, 'Very stealable!')
        self.assertEqual(prod.explode, '...BABOOM!')

class AcmeReportTest(unittest.TestCase):

    def test_default_num_products(self):


    def test_legal_names(self):



if __name__ == '__main__':
    unittest.main()
