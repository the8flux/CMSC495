from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    user_logon: str
    description: str
