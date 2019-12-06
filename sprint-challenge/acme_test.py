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
        """Test stealability and explode for a custom product."""
        prod = Product('Test Product 3', price=2, weight=15, flammability=3.0)
        self.assertEqual(prod.stealability(), 'Not so stealable...')
        self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTest(unittest.TestCase):
    """Test the validity of the report"""
    def test_default_num_products(self):
        """Test the length of acme report to be 30."""
        gen_prod = generate_products()
        self.assertEqual(len(gen_prod), 30)

    def test_legal_names(self):
        """Test that the names used are valid"""
        gen_prod = generate_products()
        poss_names = ADJECTIVES + NOUNS
        words = []
        new_words = []
        for x in range(0, len(gen_prod)):
            words.append(gen_prod[x].name.split())
        for i in range(0, len(words)):
            new_words.append(words[i][0])
            new_words.append(words[i][1])
        for k in range(0, len(new_words)):
            self.assertIn(new_words[k], poss_names)


if __name__ == '__main__':
    unittest.main()
