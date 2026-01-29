from collections import defaultdict

def detect_windows(events):
    alerts = []
    attempts = defaultdict(set)
    count = defaultdict(int)

    for e in events:
        if e["event_id"] == "4625":
            count[e["ip"]] += 1
            attempts[e["ip"]].add(e["user"])

        # Success after failures = HIGH CONFIDENCE
        if e["event_id"] == "4624" and count[e["ip"]] >= 5:
            alerts.append(
                f"Credential stuffing suspected from {e['ip']} "
                f"({count[e['ip']]} failures, success login)"
            )

    # Multiple users attacked
    for ip, users in attempts.items():
        if len(users) >= 3:
            alerts.append(
                f"Brute-force suspected from {ip} "
                f"against multiple users: {list(users)}"
            )

    return alerts


def detect_firewall(events):
    alerts = []

    for e in events:
        if e["action"] == "BLOCK" and e["port"] in ["22", "3389"]:
            alerts.append(
                f"Firewall blocked attack from {e['ip']} on port {e['port']}"
            )

    return alerts
