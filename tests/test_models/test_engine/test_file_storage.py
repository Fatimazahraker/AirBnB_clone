#!/usr/bin/python3
""" unittest module to test file storage module with base_model module """
import unittest
import models
from models.engine import file_storage
import pep8
import os


class TestFileStorage(unittest.TestCase):
    """ class inherit from unittest to test file storage module """

    def setUp(self):
        """ method that initiate at first of each test """
        self.new = models.BaseModel()

    def tearDown(self):
        """ method that intiate at end of each test """
        del self.new
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style(self):
        """method test style of module file"""
        style = pep8.StyleGuide()
        result = style.check_files(['models/engine/file_storage.py'])
        errors = result.total_errors
        self.assertEqual(errors, 0, "fix pep8")

    def test_doc_module(self):
        """ method test if there doc for module """
        doc = len(file_storage.__doc__.strip())
        self.assertTrue(doc > 0)
        doc = len(models.__init__.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_class(self):
        """ method test if there doc for class """
        doc = len(file_storage.FileStorage.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_all_method(self):
        """ method test if there doc for all method """
        doc = len(file_storage.FileStorage.all.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_new_method(self):
        """ method test if there doc for new method """
        doc = len(file_storage.FileStorage.new.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_save_method(self):
        """ method test if there doc for save method """
        doc = len(file_storage.FileStorage.save.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_doc_reload_method(self):
        """ method test if there doc for reload method """
        doc = len(file_storage.FileStorage.reload.__doc__.strip())
        self.assertTrue(doc > 0)

    def test_file_path(self):
        """test present of file """
        self.new.x = "amgad"
        self.new.save()
        result = os.path.isfile('file.json')
        self.assertTrue(result)

    def test_object_attr(self):
        """ test object attribute instance"""
        all_obj = models.storage.all()
        self.assertTrue(isinstance(all_obj, dict))
        self.assertEqual(type(all_obj), dict)

    def test_has_attr(self):
        """ test has attr if present or not"""
        self.assertTrue(hasattr(models.storage, "reload"))
        self.assertTrue(hasattr(models.storage, "all"))
        self.assertTrue(hasattr(models.storage, "new"))
        self.assertTrue(hasattr(models.storage, "save"))

    def test_instance(self):
        """ test is instance or not"""
        self.assertTrue(isinstance(models.storage,
                                   models.engine.file_storage.FileStorage))

    def test_check_save(self):
        """ check save of 'new' instance of base model """
        all_obj = models.storage.all()
        new_obj = all_obj[f"BaseModel.{self.new.id}"]
        self.assertEqual(new_obj, self.new)

    def test_update_instance_save(self):
        """ method test update instance and save it """
        self.new.name = "new"
        self.new.age = 10
        self.new.save()
        all_obj = models.storage.all()
        new_obj = all_obj[f"BaseModel.{self.new.id}"]
        self.assertEqual(new_obj, self.new)

    def test_new_instance(self):
        """ check new instance in storage """
        new2 = models.BaseModel()
        all_obj = models.storage.all()
        new_obj = all_obj[f"BaseModel.{self.new.id}"]
        self.assertEqual(new_obj, self.new)
        new_obj = all_obj[f"BaseModel.{new2.id}"]
        self.assertEqual(new_obj, new2)


if __name__ == '__main__':
    unittest.main()
