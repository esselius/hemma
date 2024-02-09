from . import Event
from .group import *


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
