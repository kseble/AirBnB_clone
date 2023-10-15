#!/usr/bin/python3
"""Defines the class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ represent Review.
        
        Attributes:
            place_id (str): The place id
            user_id (str): The User id
            text (str): the text of the review
        """

        place_id = ""
        user_id = ""
        text = ""
