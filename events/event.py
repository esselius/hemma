from typing import Union
from pydantic import TypeAdapter

from .light import LightAdded, LightChanged
from .sensor import SensorChanged
from .group import GroupChanged


Event = TypeAdapter(
    Union[
        SensorChanged,
        LightChanged,
        LightAdded,
        GroupChanged,
    ]
)
