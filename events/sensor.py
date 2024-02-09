from datetime import datetime
from typing import Any, List, Literal, Optional, Union

from .common import Base, MyBase, HeartbeatAttr


class ButtonState(MyBase):
    buttonevent: int
    lastupdated: datetime


class SensorButtonConfig(MyBase):
    clickmode: str
    devicemode: str
    on: bool
    reachable: bool


class SensorBatteryConfig(MyBase):
    alert: Optional[str] = None
    battery: int
    on: bool
    reachable: bool
    offset: Optional[int] = None


class TempSensorState(MyBase):
    temperature: int
    lastupdated: datetime


class HumiditySensorState(MyBase):
    humidity: int
    lastupdated: datetime


class DaylightSensorState(MyBase):
    dark: bool
    daylight: bool
    status: int
    sunrise: datetime
    sunset: datetime
    lastupdated: datetime


class SensorChanged(Base):
    r: Literal["sensors"]
    e: Literal["changed"]
    uniqueid: str
    state: Optional[
        Union[
            ButtonState,
            TempSensorState,
            HumiditySensorState,
            DaylightSensorState,
        ]
    ] = None
    attr: Optional[HeartbeatAttr] = None
    config: Optional[Union[SensorBatteryConfig, SensorButtonConfig]] = None
