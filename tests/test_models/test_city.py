#!/usr/bin/python3
""" module to test city class """
import unittest
from models import city
from models.city import City


class TestCity(unittest.TestCase):
    """ class that test city module and City class """

    def test_module_doc(self):
        """ method test if there doc for module """
        doc = len(city.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_class_doc(self):
        """ method test if there is doc for class """
        doc = len(City.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_empty_attribute(self):
        """ method test if has class attributes empty """
        new = City()
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(len(new.name) == 0)
        self.assertTrue(hasattr(new, "state_id"))
        self.assertTrue(len(new.state_id) == 0)

    def test_type_attributes(self):
        """ method test type of value of attributes """
        new = City()
        self.assertIs(type(new.name), str)
        self.assertIs(type(new.state_id), str)

    def test_modify_attributes(self):
        """ method test of modified state """
        new = City()
        new.name = "cairo"
        new.state_id = "555"
        self.assertEqual(new.name, "cairo")
        self.assertEqual(new.state_id, "555")
        self.assertEqual(City.name, "")
        self.assertEqual(City.state_id, "")


if __name__ == '__main__':
    unittest.main()
