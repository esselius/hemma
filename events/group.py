from typing import Literal, Optional
from .common import Base, MyBase


class GroupState(MyBase):
    all_on: bool
    any_on: bool


class GroupChanged(Base):
    r: Literal["groups"]
    e: Literal["changed"]
    name: Optional[str] = None
    state: Optional[GroupState] = None
