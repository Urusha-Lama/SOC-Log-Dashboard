def parse_firewall_logs(file):
    events = []

    with open(file, "r") as f:
        for line in f:
            parts = line.strip().split(",")

            if len(parts) != 3:
                continue

            action, ip, port = parts

            events.append({
                "action": action,
                "ip": ip,
                "port": port
            })

    return events
