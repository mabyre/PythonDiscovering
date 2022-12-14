#
# PEP-655 - Python 3.11
#

import typing as tp
from typing import TypedDict


class Movie(TypedDict):
    title: str
    year: tp.NotRequired[int]


m1: Movie = {"title": "Black Panther", "year": 2018}  # OK
m2: Movie = {"title": "Star Wars"}  # OK (year is not required)
m3: Movie = {"year": 2022}  # ERROR (missing required field title)
