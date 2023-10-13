#!/usr/bin/python3
"""Defines the class User"""
from models.base_moddel import BaseModel


class User(BaseModel):
    """Represent a User

    Attributes:
        email (str): user's email
        password (str): user's password
        first_name (str): user's first name
        last_name (str): user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
