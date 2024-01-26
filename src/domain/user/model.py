from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class User:
    id: str
    first_name: str
    last_name: str
    password: str


@dataclass
class UserRequestDTO(BaseModel):
    first_name: str
    last_name: str
    password: str


@dataclass
class UserResponseDTO(BaseModel):
    id: int
    first_name: str
    last_name: str
