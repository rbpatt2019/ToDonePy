import pytest
from pathlib import Path
from ToDonePy.notify import notify_send as notify_send
from tests.make_temp import make_file


def test_notify_send(
    summary: str = "Test",
    body: str = "Testing testing 1, 2, 3",
    urgency: str = "low",
    expire_time: int = 1000,
) -> None:
    """Test a basic notification with notify_send

    :summary: Title of notification
    :body: Body of notification
    :urgency: Urgency of notification. Must be in ['low', 'normal', 'critical']
    :expire_time: Time, in ms, to display notification

    :returns: None
    """
    assert notify_send(summary, body, urgency, expire_time)


def test_notify_send_invalid_urgency(
    summary: str = "Test",
    body: str = "Testing testing 1, 2, 3",
    urgency: str = "not in list",
    expire_time: int = 1000,
) -> None:
    """Test notify_send with an invalid parameter

    :summary: Title of notification
    :body: Body of notification
    :urgency: Urgency of notification. Must be in ['low', 'normal', 'critical']
    :expire_time: Time, in ms, to display notification

    :returns: None
    """
    with pytest.raises(IOError):
        notify_send(summary, body, urgency, expire_time)
