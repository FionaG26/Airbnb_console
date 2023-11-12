#!/usr/bin/python3
"""
Module for BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for all models in the AirBnB clone project.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        """
        result = dict(self.__dict__)
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public instance with the current datetime.
        """
        self.updated_at = datetime.now()
