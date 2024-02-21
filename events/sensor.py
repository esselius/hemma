from datetime import datetime
from typing import Any, List, Literal, Optional, Union

from .common import Base, MyBase, HeartbeatAttr


class ButtonState(MyBase):
    buttonevent: Optional[int]
    lastupdated: Union[datetime, Literal["none"]]
    eventduration: Optional[int] = None


class SensorButtonConfig(MyBase):
    clickmode: str
    devicemode: str
    on: bool
    reachable: bool


class SensorBatteryConfig(MyBase):
    alert: Optional[str] = None
    battery: Optional[int]
    on: bool
    reachable: Optional[bool]
    offset: Optional[int] = None
    group: Optional[int] = None
    enrolled: Optional[int] = None
    pending: Optional[List] = None


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


class PowerSensorState(MyBase):
    current: int
    lastupdated: datetime
    power: int
    voltage: int


class PowerSensorConsumptionState(MyBase):
    consumption: int
    lastupdated: datetime


class DoorSensorState(MyBase):
    lastupdated: Union[datetime, Literal["none"]]
    lowbattery: bool
    open: bool
    tampered: bool


class VirtualSensorState(MyBase):
    lastupdated: Union[datetime, Literal["none"]]
    status: Optional[int] = None
    presence: Optional[bool] = None


class SensorAddDump(MyBase):
    id: int
    config: SensorBatteryConfig
    etag: str
    lastannounced: Optional[datetime]
    lastseen: datetime
    manufacturername: str
    mode: Optional[int] = None
    modelid: str
    name: str
    productname: Optional[str] = None
    state: Union[ButtonState, DoorSensorState]
    type: str
    uniqueid: Optional[str] = None
    ep: Optional[int] = None


class SensorBase(Base):
    r: Literal["sensors"]
    uniqueid: str


class SensorChanged(SensorBase):
    e: Literal["changed"]
    uniqueid: str
    state: Optional[
        Union[
            ButtonState,
            TempSensorState,
            HumiditySensorState,
            DaylightSensorState,
            PowerSensorState,
            PowerSensorConsumptionState,
            DoorSensorState,
            VirtualSensorState,
        ]
    ] = None
    attr: Optional[HeartbeatAttr] = None
    config: Optional[Union[SensorBatteryConfig, SensorButtonConfig]] = None


class SensorAdded(SensorBase):
    e: Literal["added"]
    uniqueid: str
    sensor: SensorAddDump
