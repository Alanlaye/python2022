import unittest
from city_functions import city_country_names

class FormTestCase(unittest.TestCase):
    def test_city_country_names(self):
        city_country_name =  city_country_names('aa','bb')
        self.assertEqual(city_country_name,'Aa,Bb')

    def test_city_country_names(self):
        city_country_name = city_country_names('cc','dd',5000)
        self.assertEqual(city_country_name,'Cc,Dd-population5000')

unittest.main()