def parse_windows_logs(file):
    events = []

    with open(file, "r") as f:
        for line in f:
            event_id, user, ip, time = line.strip().split(",")

            events.append({
                "event_id": event_id,
                "user": user,
                "ip": ip,
                "time": time
            })

    return events
