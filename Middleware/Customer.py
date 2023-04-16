from dataclasses import dataclass
from Middleware.User import User


@dataclass
class Customer(User):
    customer_name: str
