from pydantic_core import TzInfo

from . import Event
from .sensor import *

sensor_changed = {
    "e": "changed",
    "t": "event",
    "r": "sensors",
}


def test_sensor_battery():
    assert SensorChanged(
        **sensor_changed,
        id=7,
        uniqueid="cc:86:ec:ff:fe:9f:de:4a-01-1000",
        config=SensorBatteryConfig(
            alert="none",
            battery=87,
            on=True,
            reachable=True,
        )
    ) == Event.validate_json(open("events/fixtures/sensor_battery.json").read())


def test_sensor_button():
    assert SensorChanged(
        **sensor_changed,
        id=7,
        uniqueid="cc:86:ec:ff:fe:9f:de:4a-01-1000",
        state=ButtonState(
            buttonevent=2003, lastupdated=datetime(2024, 2, 6, 20, 43, 35, 495000)
        )
    ) == Event.validate_json(open("events/fixtures/sensor_button.json").read())


def test_sensor_config():
    assert SensorChanged(
        **sensor_changed,
        id=3,
        uniqueid="54:ef:44:10:00:71:43:55-29-0012",
        config=SensorButtonConfig(
            clickmode="rocker", devicemode="compatibility", on=True, reachable=True
        )
    ) == Event.validate_json(open("events/fixtures/sensor_config.json").read())


def test_sensor_config_changed():
    assert SensorChanged(
        **sensor_changed,
        id=9,
        uniqueid="14:2d:41:ff:fe:2f:3c:4d-01-0405",
        config=SensorBatteryConfig(
            battery=100,
            offset=0,
            on=True,
            reachable=True
        )
    ) == Event.validate_json(open("events/fixtures/sensor_config_changed.json").read())


def test_sensor_daylight():
    assert SensorChanged(
        **sensor_changed,
        id=1,
        uniqueid="00:21:2e:ff:ff:0c:a0:94-01",
        state=DaylightSensorState(
            dark=True,
            daylight=False,
            lastupdated=datetime(2024, 2, 4, 15, 56, 28, 54000),
            status=200,
            sunrise=datetime(2024, 2, 4, 7, 11, 9),
            sunset=datetime(2024, 2, 4, 15, 43, 23),
        )
    ) == Event.validate_json(open("events/fixtures/sensor_daylight.json").read())


def test_sensor_heartbeat():
    assert SensorChanged(
        **sensor_changed,
        id=3,
        uniqueid="54:ef:44:10:00:71:43:55-29-0012",
        attr=HeartbeatAttr(
            id=3,
            lastannounced=datetime(2024, 1, 8, 17, 28, 42, tzinfo=TzInfo(0)),
            lastseen=datetime(2024, 2, 6, 20, 46, tzinfo=TzInfo(0)),
            manufacturername="LUMI",
            modelid="lumi.switch.l0agl1",
            name="Bibliotek switch",
            swversion="0.0.0_0024",
            type="ZHASwitch",
            uniqueid="54:ef:44:10:00:71:43:55-29-0012",
        )
    ) == Event.validate_json(open("events/fixtures/sensor_heartbeat.json").read())


def test_sensor_humidity():
    assert SensorChanged(
        **sensor_changed,
        id=9,
        uniqueid="14:2d:41:ff:fe:2f:3c:4d-01-0405",
        state=HumiditySensorState(
            humidity=4180, lastupdated=datetime(2024, 2, 6, 21, 20, 37, 137000)
        )
    ) == Event.validate_json(open("events/fixtures/sensor_humidity.json").read())


def test_sensor_temp():
    assert SensorChanged(
        **sensor_changed,
        id=8,
        uniqueid="14:2d:41:ff:fe:2f:3c:4d-01-0402",
        state=TempSensorState(
            lastupdated=datetime(2024, 2, 6, 20, 46, 54, 35000),
            temperature=2060,
        )
    ) == Event.validate_json(open("events/fixtures/sensor_temp.json").read())


def test_sensor_accouncement():
    assert SensorChanged(
        **sensor_changed,
        id=7,
        uniqueid="cc:86:ec:ff:fe:9f:de:4a-01-1000",
        attr=HeartbeatAttr(
            id="7",
            lastannounced=datetime(2024, 2, 9, 6, 24, 11, tzinfo=TzInfo(0)),
            lastseen=datetime(2024, 2, 9, 10, 37, tzinfo=TzInfo(0)),
            manufacturername="IKEA of Sweden",
            modelid="TRADFRI open/close remote",
            name="Sovrum rullgardinsknapp",
            productid="E1766",
            swversion="2.3.079",
            type="ZHASwitch",
            uniqueid="cc:86:ec:ff:fe:9f:de:4a-01-1000",
        )
    ) == Event.validate_json(open("events/fixtures/sensor_announcement.json").read())
