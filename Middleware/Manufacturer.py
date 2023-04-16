from dataclasses import dataclass
from Middleware.User import User


@dataclass
class Manufacturer(User):
    manufacturer_name: str
