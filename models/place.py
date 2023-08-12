#!/usr/bin/python3

"""Place Module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class that inherits from BaseModel
    class.

    Attributes
    ----------

    city_id : str 
        This refers to the City.id
    user_id: str
        This refers to the User.id
    name: str
        This refers to the name of the place
    description: str
        This refers to the description of the
        place.
    number_rooms: int
        This refers to the number of rooms the
        place has. 
    number_bathrooms: int
        This refers to the number of bathrooms
        the place has.
    max_guest: int
        This refers to the number of max limit
        of guests allowed at the place.
    price_by_night: int
        This refers to the price per night of
        the place. 
    latitude: float
        This refers to the distance of the place
        measured (north or south) from the equator.
    longitude: float
        This refers to the distance of the place
        measured (east or west) from the Greenwich
        meridian.
    amenity_ids: list of str
        This refers to the list of Amenity.id

    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
