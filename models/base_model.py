#!/usr/bin/python3
"""Define a class BaseModel."""

from datetime import datetime
import uuid
import models

class BaseModel:
    """Represent a BaseModel."""

    def __init__(self, *args, **kwargs):
        """Initialize a Base_Model instance.
        Args:
            self (BaseModel): current instance
            args (any): not used here
            kwargs (dict) : dictionnary of key/value pairs attributes
        """    
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs):
            date_format = "%Y-%m-%dT%H:%M:%S.%f" 
            for key,value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
                    
        else:
            models.storage.new(self)

    def __str__(self):
        """Define the print() representation of a BasModel"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update the public instance attribute update_at with the current date"""
        self.updated_at = datetime.today()
        models.storage.save()
        models.storage.reload()


    def to_dict(self):
        """Return a dictionnary that contain all key/values of __dict__ of the instance with a added key __class__ """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return (new_dict)
