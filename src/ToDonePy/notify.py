import subprocess


def notify_send(summary: str, body: str, urgency: str, expire_time: int) -> bool:
    """Send a notification using notify-send

    :summary: Title of notification
    :body: Body of notification
    :urgency: Urgency of notification. Must be in ['low', 'normal', 'critical']
    :expire_time: Time, in ms, to display notification

    :returns: True, if successful
    """
    ns = subprocess.Popen(
        ["notify-send", summary, body, "-u", urgency, "-t", str(expire_time)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    result, err = ns.communicate()
    if ns.returncode != 0:
        raise IOError(err)
    else:
        return True
