#!/usr/bin/python3
""" module to test amenity class """
import unittest
from models import amenity
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ class that test amenity module and amenity class """

    def test_module_doc(self):
        """ method test if there doc for module """
        doc = len(amenity.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_class_doc(self):
        """ method test if there is doc for class """
        doc = len(Amenity.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_empty_attribute(self):
        """ method test if has class attributes empty """
        new = Amenity()
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(len(new.name) == 0)

    def test_type_attributes(self):
        """ method test type of value of attributes """
        new = Amenity()
        self.assertIs(type(new.name), str)

    def test_modify_attributes(self):
        """ method test of modified amenity """
        new = Amenity()
        new.name = "sea"
        self.assertEqual(new.name, "sea")
        self.assertEqual(Amenity.name, "")


if __name__ == '__main__':
    unittest.main()
