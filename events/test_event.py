from pydantic_core import TzInfo

from .event import *
from .group import *
from .sensor import *
from .light import *


def test_group():
    assert GroupChanged(
        e="changed",
        r="groups",
        t="event",
        id=3,
        state=GroupState(
            all_on=False,
            any_on=False,
        ),
    ) == Event.validate_json(open("events/fixtures/group.json").read())


def test_group_rename():
    assert GroupChanged(
        e="changed", r="groups", t="event", id=3, name="Bibliotek"
    ) == Event.validate_json(open("events/fixtures/group_rename.json").read())


light_changed = {
    "e": "changed",
    "t": "event",
    "r": "lights",
}


def test_light_announcement():
    assert LightChanged(
        **light_changed,
        id=2,
        uniqueid="00:17:88:01:03:7e:3d:7e-0b",
        attr=LightAnnouncementAttr(
            colorcapabilities=31,
            ctmax=500,
            ctmin=153,
            id="2",
            lastannounced=None,
            lastseen=datetime(2024, 2, 8, 11, 51, tzinfo=TzInfo(0)),
            manufacturername="Signify Netherlands B.V.",
            modelid="LCT012",
            name="Undre lampa",
            productid="Philips-LCT012-1-E14ECLv1",
            swconfigid="78566063",
            swversion="1.108.7",
            type="Extended color light",
            uniqueid="00:17:88:01:03:7e:3d:7e-0b",
        )
    ) == Event.validate_json(open("events/fixtures/light_announcement.json").read())


def test_light_color_added():
    assert LightAdded(
        e="added",
        t="event",
        r="lights",
        id=2,
        uniqueid="00:17:88:01:03:7e:3d:7e-0b",
        light=LightAddDump(
            capabilities=LightCapabilities(
                alerts=[
                    "none",
                    "select",
                    "lselect",
                    "blink",
                    "breathe",
                    "okay",
                    "channelchange",
                    "finish",
                    "stop",
                ],
                bri={"min_dim_level": 0},
                color={
                    "ct": {"computes_xy": True, "max": 65279, "min": 0},
                    "gamut_type": None,
                    "modes": [],
                    "xy": {"blue": [0, 0], "green": [0, 0], "red": [0, 0]},
                },
            ),
            colorcapabilities=0,
            config={
                "bri": {"startup": "previous"},
                "color": {"ct": {"startup": 336}, "xy": {"startup": [0, 0]}},
                "groups": [],
                "on": {"startup": "previous"},
            },
            ctmax=65279,
            ctmin=0,
            etag="b3f7e5259da6b2a7ed5027981bdf0bbc",
            hascolor=True,
            lastannounced=None,
            lastseen="2024-02-08T11:49Z",
            manufacturername="Signify Netherlands B.V.",
            modelid="LCT012",
            name="Extended color light 2",
            productid=None,
            state={
                "alert": "none",
                "bri": 0,
                "colormode": "hs",
                "ct": 0,
                "effect": "none",
                "hue": 0,
                "on": False,
                "reachable": False,
                "sat": 0,
                "xy": [0, 0],
            },
            swconfigid=None,
            swversion=None,
            type="Extended color light",
            uniqueid="00:17:88:01:03:7e:3d:7e-0b",
        ),
    ) == Event.validate_json(open("events/fixtures/light_color_added.json").read())


def test_light_config_previous():
    assert LightChanged(
        **light_changed,
        id=2,
        uniqueid="00:17:88:01:03:7e:3d:7e-0b",
        config=LightStartupConfig(
            bri={"startup": 254},
            color={"ct": {"startup": 366}, "xy": {"startup": "previous"}},
            on={"startup": True},
        )
    ) == Event.validate_json(open("events/fixtures/light_config_previous.json").read())


def test_light_config():
    assert LightChanged(
        **light_changed,
        id=2,
        uniqueid="00:17:88:01:03:7e:3d:7e-0b",
        config=LightStartupConfig(
            bri={"startup": 254},
            color={"ct": {"startup": 366}, "xy": {"startup": [0, 0.9961]}},
            on={"startup": True},
        )
    ) == Event.validate_json(open("events/fixtures/light_config.json").read())


def test_light_heartbeat():
    assert LightChanged(
        **light_changed,
        id=3,
        uniqueid="54:ef:44:10:00:71:43:55-01",
        attr=HeartbeatAttr(
            id="3",
            lastannounced=datetime(2024, 1, 8, 17, 28, 42, tzinfo=TzInfo(0)),
            lastseen=datetime(2024, 2, 6, 20, 46, tzinfo=TzInfo(0)),
            manufacturername="LUMI",
            modelid="lumi.switch.l0agl1",
            name="Bibliotek Taklampa",
            swversion="0.0.0_0024",
            type="On/Off light",
            uniqueid="54:ef:44:10:00:71:43:55-01",
        )
    ) == Event.validate_json(open("events/fixtures/light_heartbeat.json").read())


def test_light_off_dimmable():
    assert LightChanged(
        **light_changed,
        id=1,
        uniqueid="b4:e3:f9:ff:fe:de:09:0d-01",
        state=LightState(
            alert="none",
            bri=254,
            on=False,
            reachable=True,
        )
    ) == Event.validate_json(open("events/fixtures/light_off_dimmable.json").read())


def test_light_off():
    assert LightChanged(
        **light_changed,
        id=3,
        uniqueid="54:ef:44:10:00:71:43:55-01",
        state=LightState(
            alert="none",
            on=False,
            reachable=True,
        )
    ) == Event.validate_json(open("events/fixtures/light_off.json").read())


def test_light_color():
    assert LightChanged(
        **light_changed,
        id=2,
        uniqueid="00:17:88:01:03:7e:3d:7e-0b",
        state=LightState(
            alert="none",
            bri=31,
            colormode="xy",
            ct=0,
            effect="none",
            hue=8417,
            on=True,
            reachable=True,
            sat=140,
            xy=[0.4082, 0.4289],
        )
    ) == Event.validate_json(open("events/fixtures/light_color.json").read())


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
            lastannounced=datetime(2024,2,9,6,24,11, tzinfo=TzInfo(0)),
            lastseen=datetime(2024,2,9,10,37,tzinfo=TzInfo(0)),
            manufacturername="IKEA of Sweden",
            modelid="TRADFRI open/close remote",
            name="Sovrum rullgardinsknapp",
            productid="E1766",
            swversion="2.3.079",
            type="ZHASwitch",
            uniqueid="cc:86:ec:ff:fe:9f:de:4a-01-1000",
        )
    ) == Event.validate_json(open("events/fixtures/sensor_announcement.json").read())
