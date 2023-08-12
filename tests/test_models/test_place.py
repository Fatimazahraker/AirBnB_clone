#!/usr/bin/python3
""" module to test place class """
import unittest
from models import place
from models.place import Place


class TestPlace(unittest.TestCase):
    """ class that test place module and Place class """

    def test_module_doc(self):
        """ method test if there doc for module """
        doc = len(place.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_class_doc(self):
        """ method test if there is doc for class """
        doc = len(Place.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_empty_attribute(self):
        """ method test if has class attributes empty """
        new = Place()
        self.assertTrue(hasattr(new, "city_id"))
        self.assertTrue(len(new.city_id) == 0)
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(len(new.user_id) == 0)
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(len(new.name) == 0)
        self.assertTrue(hasattr(new, "description"))
        self.assertTrue(len(new.description) == 0)
        self.assertTrue(hasattr(new, "number_rooms"))
        self.assertTrue(new.number_rooms == 0)
        self.assertTrue(hasattr(new, "number_bathrooms"))
        self.assertTrue(new.number_bathrooms == 0)
        self.assertTrue(hasattr(new, "max_guest"))
        self.assertTrue(new.max_guest == 0)
        self.assertTrue(hasattr(new, "number_rooms"))
        self.assertTrue(new.number_rooms == 0)
        self.assertTrue(hasattr(new, "price_by_night"))
        self.assertTrue(new.price_by_night == 0)
        self.assertTrue(hasattr(new, "latitude"))
        self.assertTrue(new.latitude == 0.0)
        self.assertTrue(hasattr(new, "longitude"))
        self.assertTrue(new.longitude == 0.0)
        self.assertTrue(hasattr(new, "amenity_ids"))
        self.assertTrue(new.amenity_ids == [])

    def test_type_attributes(self):
        """ method test type of value of attributes """
        new = Place()
        self.assertIs(type(new.city_id), str)
        self.assertIs(type(new.user_id), str)
        self.assertIs(type(new.name), str)
        self.assertIs(type(new.description), str)
        self.assertIs(type(new.number_rooms), int)
        self.assertIs(type(new.number_bathrooms), int)
        self.assertIs(type(new.max_guest), int)
        self.assertIs(type(new.price_by_night), int)
        self.assertIs(type(new.latitude), float)
        self.assertIs(type(new.longitude), float)
        self.assertIs(type(new.amenity_ids), list)

    def test_modify_attributes(self):
        """ method test of modified place """
        new = Place()
        new.name = "cairo"
        self.assertEqual(new.name, "cairo")
        self.assertEqual(Place.name, "")
        new.max_guest = 4
        self.assertEqual(new.max_guest, 4)
        self.assertEqual(Place.max_guest, 0)
        new.longitude = 88.9
        self.assertEqual(new.longitude, 88.9)
        self.assertEqual(Place.longitude, 0.0)
        new.amenity_ids = ["66", "55"]
        self.assertEqual(new.amenity_ids, ["66", "55"])
        self.assertEqual(Place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
