from typing import Union
from pydantic import TypeAdapter

from .light import LightAdded, LightChanged
from .sensor import SensorAdded, SensorChanged
from .group import GroupChanged


Event = TypeAdapter(
    Union[
        SensorAdded,
        SensorChanged,
        LightChanged,
        LightAdded,
        GroupChanged,
    ]
)
