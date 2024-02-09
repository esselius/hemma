from pydantic_core import TzInfo

from . import Event
from .light import *

light_added = {
    "e": "added",
    "t": "event",
    "r": "lights",
}

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
        **light_added,
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


def test_light_added_extender():
    assert LightAdded(
        **light_added,
        id=4,
        uniqueid="bc:33:ac:ff:fe:12:58:3a-01",
        light=LightAddDump(
            capabilities=LightCapabilities(alerts=["none", "select", "lselect"]),
            etag="ccf6ed6fc470e4c1fd46b9646cc54b5e",
            hascolor=False,
            lastannounced=None,
            lastseen="2024-02-09T11:30Z",
            manufacturername="IKEA of Sweden",
            modelid="TRADFRI Signal Repeater",
            name="Range extender 4",
            productid=None,
            state=LightState(alert="none", reachable=False),
            swversion=None,
            type="Range extender",
            uniqueid="bc:33:ac:ff:fe:12:58:3a-01",
        )
    ) == Event.validate_json(open("events/fixtures/light_added_extender.json").read())

def test_light_announcement_extender():
    assert LightChanged(
        **light_changed,
        id=5,
        uniqueid="bc:33:ac:ff:fe:12:58:3a-01",
        attr=HeartbeatAttr(
            id="5",
            lastannounced=None,
            lastseen=datetime(2024, 2, 9, 11, 35, tzinfo=TzInfo(0)),
            manufacturername="IKEA of Sweden",
            modelid="TRADFRI Signal Repeater",
            name="Range extender 5",
            productid=None,
            swversion=None,
            type="Range extender",
            uniqueid="bc:33:ac:ff:fe:12:58:3a-01"
        )
    ) == Event.validate_json(open("events/fixtures/light_announcement_extender.json").read())