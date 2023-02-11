#!/usr/bin/python3

from models.base_model import BaseModel
import unittest, os
from datetime import datetime
from time import sleep

class TestBaseModel(unittest.TestCase):

    """Unittests for testing instantation of the BaseModel class."""
    
    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_id(self):
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_two_differents_base_model_created_at(self):
        base_model1 = BaseModel()
        sleep(0.05)
        base_model2 = BaseModel()
        self.assertLess(base_model1.created_at, base_model2.created_at)

    def test_two_differents_base_model_updated_at(self):
        base_model1 = BaseModel()
        sleep(0.05)
        base_model2 = BaseModel()
        self.assertLess(base_model1.updated_at, base_model2.updated_at)

    def test_str_representation(self):
        dte = datetime.today()
        bm = BaseModel()
        bm.id = "00000"
        bm.created_at = bm.update_at = dte
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (00000)", bmstr)
        self.assertIn("'id': '00000'", bmstr)
        self.assertIn("'created_at': " + repr(dte), bmstr)
        self.assertIn("'updated_at': " + repr(dte), bmstr)


    def test_args_unused(self):
        base_model = BaseModel()
        self.assertNotIn(None, base_model.__dict__.values())
    
    def test_instantiation_with_kwargs(self):
        dte = datetime.today()
        dte_iso = dte.isoformat()
        base_model = BaseModel(id='1234', created_at=dte_iso, updated_at=dte_iso)
        self.assertEqual(base_model.id, '1234')
        self.assertEqual(base_model.created_at, dte)
        self.assertEqual(base_model.updated_at, dte)

    def test_instantiation_with_args_and_kwargs(self):
        dte = datetime.today()
        dte_iso = dte.isoformat()
        base_model = BaseModel("12",id='1234', created_at=dte_iso, updated_at=dte_iso)
        self.assertEqual(base_model.id, '1234')
        self.assertEqual(base_model.created_at, dte)
        self.assertEqual(base_model.updated_at, dte)


    """Unittest for testing save method of the BaseModel class"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json","tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp","file.json")
        except IOError:
            pass  

    def test_one_save(self):
        base_model = BaseModel()
        sleep(0.05)
        old_updated_at = base_model.updated_at
        base_model.save()
        self.assertLess(old_updated_at, base_model.updated_at)

  
  
    """Unittest for testing to_dict method of the BaseModel class"""

    def test_to_dict_type(self):
        base_model = BaseModel()
        self.assertEqual(dict, type(base_model.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        base_model = BaseModel()
        self.assertIn("id", base_model.to_dict())
        self.assertIn("created_at", base_model.to_dict())
        self.assertIn("updated_at", base_model.to_dict())
        self.assertIn("__class__", base_model.to_dict())

    def test_to_dict_contains_added_attributes(self):
        base_model = BaseModel()
        base_model.name = "ALX"
        self.assertIn("name", base_model.to_dict())



if __name__ == 'main':
    unittest.main()
