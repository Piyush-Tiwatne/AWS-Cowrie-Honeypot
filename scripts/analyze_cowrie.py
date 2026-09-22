import json
from pathlib import Path
from collections import Counter

LOG_DIR = Path.home() / "cowrie/var/log/cowrie"

EXCLUDED_IPS = {
    "27.59.108.63",
    "106.192.127.200",
    "106.192.135.142"
}

logs = list(LOG_DIR.glob("cowrie.json*"))

connections = Counter()
usernames = Counter()
commands = Counter()
clients = Counter()
hassh = Counter()
dates = Counter()

total = 0
filtered = 0
login_success = 0
login_failed = 0
bad_json = 0

for log in logs:
    for line in log.open(errors="ignore"):
        try:
            data = json.loads(line)
        except:
            bad_json += 1
            continue

        event = data.get("eventid", "")
        ip = data.get("src_ip", "")

        if event == "cowrie.session.connect":
            total += 1

        if ip in EXCLUDED_IPS:
            continue

        if event == "cowrie.session.connect":
            filtered += 1
            connections[ip] += 1

            timestamp = data.get("timestamp", "")
            if timestamp:
                dates[timestamp[:10]] += 1

        elif event == "cowrie.login.success":
            login_success += 1
            usernames[data.get("username", "unknown")] += 1

        elif event == "cowrie.login.failed":
            login_failed += 1

        elif event == "cowrie.command.input":
            command = data.get("input", "").strip()
            if command:
                commands[command] += 1

        elif event == "cowrie.client.version":
            client = data.get("version", "unknown")
            clients[client] += 1

        if data.get("hassh"):
            hassh[data["hassh"]] += 1


report = []

report.append("=" * 60)
report.append("        COWRIE SSH HONEYPOT ANALYSIS REPORT")
report.append("=" * 60)

report.append("\n1. COLLECTION SUMMARY")
report.append("-" * 60)
report.append(f"Log files analyzed       : {len(logs)}")
report.append(f"Total connections        : {total}")
report.append(f"Connections after filter : {filtered}")
report.append(f"Unique source IPs        : {len(connections)}")
report.append(f"Successful login events  : {login_success}")
report.append(f"Failed login events      : {login_failed}")
report.append(f"Malformed JSON lines     : {bad_json}")

report.append("\n2. TOP SOURCE IPs")
report.append("-" * 60)
for ip, count in connections.most_common(10):
    report.append(f"{count:8}  {ip}")

report.append("\n3. TOP USERNAMES")
report.append("-" * 60)
for user, count in usernames.most_common(10):
    report.append(f"{count:8}  {user}")

report.append("\n4. TOP COMMANDS")
report.append("-" * 60)
for command, count in commands.most_common(10):
    report.append(f"{count:8}  {command}")

report.append("\n5. OBSERVED CLIENT STRINGS")
report.append("-" * 60)
for client, count in clients.most_common(10):
    report.append(f"{count:8}  {client}")

report.append("\n6. HASSH FINGERPRINTS")
report.append("-" * 60)
for fingerprint, count in hassh.most_common(10):
    report.append(f"{count:8}  {fingerprint}")

report.append("\n7. ACTIVITY BY DATE")
report.append("-" * 60)
for date in sorted(dates):
    report.append(f"{date}  {dates[date]}")

report.append("\n8. KEY OBSERVATIONS")
report.append("-" * 60)

if connections:
    ip, count = connections.most_common(1)[0]
    report.append(f"- Highest activity source generated {count} connections.")

if commands:
    command, count = commands.most_common(1)[0]
    report.append(f"- Most frequent command was '{command}' with {count} occurrences.")

if clients:
    client, count = clients.most_common(1)[0]
    report.append(f"- Most frequent client string was '{client}' with {count} observations.")

report.append("- Repeated command patterns indicate automated or scripted activity.")
report.append("- Successful logins represent authentication accepted by Cowrie, not EC2 compromise.")

output = "\n".join(report)

print(output)

Path.home().joinpath("cowrie/cowrie_analysis_report.txt").write_text(output)
print("\nReport saved to ~/cowrie/cowrie_analysis_report.txt")
