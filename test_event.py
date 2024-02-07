from event import Event


def test_event_parsing():
    with open("events.jsonl") as events:
        for event in events.readlines():
            print(event)
            e = Event.validate_json(event)
