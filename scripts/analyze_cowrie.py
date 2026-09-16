import json
from pathlib import Path
from collections import Counter


# Cowrie log directory
LOG_DIR = Path.home() / "cowrie" / "var" / "log" / "cowrie"


# Counters
source_ips = Counter()
usernames = Counter()
commands = Counter()
client_versions = Counter()
hassh = Counter()
connections_by_date = Counter()

total_connections = 0
login_success = 0
login_failed = 0
malformed_lines = 0


# Find all Cowrie JSON log files
log_files = sorted(LOG_DIR.glob("cowrie.json*"))


for log_file in log_files:

    with log_file.open("r", errors="replace") as file:

        for line in file:

            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                malformed_lines += 1
                continue

            event_id = event.get("eventid", "")
            source_ip = event.get("src_ip")
            timestamp = event.get("timestamp", "")

            # --------------------------------
            # CONNECTIONS
            # --------------------------------
            if event_id == "cowrie.session.connect":

                total_connections += 1

                if source_ip:
                    source_ips[source_ip] += 1

                # Count connections by date
                if timestamp:
                    date = timestamp[:10]
                    connections_by_date[date] += 1

            # --------------------------------
            # LOGIN EVENTS
            # --------------------------------
            elif event_id == "cowrie.login.success":

                login_success += 1

                username = event.get("username")

                if username:
                    usernames[username] += 1

            elif event_id == "cowrie.login.failed":

                login_failed += 1

            # --------------------------------
            # COMMANDS
            # --------------------------------
            elif event_id == "cowrie.command.input":

                command = event.get("input")

                if command:
                    commands[command] += 1

            # --------------------------------
            # SSH CLIENT
            # --------------------------------
            elif event_id == "cowrie.client.version":

                client = event.get("version")

                if client:
                    client_versions[client] += 1

            # --------------------------------
            # HASSH
            # --------------------------------
            elif event_id == "cowrie.client.kex":

                fingerprint = event.get("hassh")

                if fingerprint:
                    hassh[fingerprint] += 1


# --------------------------------
# CREATE REPORT
# --------------------------------

report_file = Path("cowrie_analysis_report.txt")


with report_file.open("w") as report:

    report.write("=" * 60 + "\n")
    report.write("        COWRIE SSH HONEYPOT ANALYSIS REPORT\n")
    report.write("=" * 60 + "\n\n")

    # --------------------------------
    # SUMMARY
    # --------------------------------

    report.write("1. COLLECTION SUMMARY\n")
    report.write("-" * 60 + "\n")

    report.write(f"Log files analyzed      : {len(log_files)}\n")
    report.write(f"Total connections       : {total_connections}\n")
    report.write(f"Unique source IPs       : {len(source_ips)}\n")
    report.write(f"Successful login events : {login_success}\n")
    report.write(f"Failed login events     : {login_failed}\n")
    report.write(f"Malformed JSON lines    : {malformed_lines}\n\n")


    # --------------------------------
    # SOURCE IPS
    # --------------------------------

    report.write("2. TOP SOURCE IPs\n")
    report.write("-" * 60 + "\n")

    for ip, count in source_ips.most_common(10):

        report.write(
            f"{ip:<20} {count:>8} connections\n"
        )


    # --------------------------------
    # USERNAMES
    # --------------------------------

    report.write("\n3. TOP USERNAMES\n")
    report.write("-" * 60 + "\n")

    for username, count in usernames.most_common(10):

        report.write(
            f"{username:<20} {count:>8}\n"
        )


    # --------------------------------
    # COMMANDS
    # --------------------------------

    report.write("\n4. TOP COMMANDS\n")
    report.write("-" * 60 + "\n")

    for command, count in commands.most_common(10):

        report.write(
            f"{count:>8}  {command}\n"
        )


    # --------------------------------
    # SSH CLIENTS
    # --------------------------------

    report.write("\n5. SSH CLIENT VERSIONS\n")
    report.write("-" * 60 + "\n")

    for client, count in client_versions.most_common(10):

        report.write(
            f"{count:>8}  {client}\n"
        )


    # --------------------------------
    # HASSH
    # --------------------------------

    report.write("\n6. HASSH FINGERPRINTS\n")
    report.write("-" * 60 + "\n")

    for fingerprint, count in hassh.most_common(10):

        report.write(
            f"{count:>8}  {fingerprint}\n"
        )


    # --------------------------------
    # ACTIVITY BY DATE
    # --------------------------------

    report.write("\n7. CONNECTIONS BY DATE\n")
    report.write("-" * 60 + "\n")

    for date, count in sorted(connections_by_date.items()):

        report.write(
            f"{date:<15} {count:>8} connections\n"
        )


    # --------------------------------
    # KEY OBSERVATIONS
    # --------------------------------

    report.write("\n8. KEY OBSERVATIONS\n")
    report.write("-" * 60 + "\n")

    if source_ips:

        top_ip, top_ip_count = source_ips.most_common(1)[0]

        percentage = (
            top_ip_count / total_connections
        ) * 100

        report.write(
            f"- Dominant source IP: {top_ip} "
            f"({top_ip_count} connections, "
            f"approximately {percentage:.2f}% of all connections).\n"
        )


    if client_versions:

        top_client, top_client_count = client_versions.most_common(1)[0]

        report.write(
            f"- Dominant SSH client version: "
            f"{top_client} ({top_client_count} events).\n"
        )


    if usernames:

        top_username, top_username_count = usernames.most_common(1)[0]

        report.write(
            f"- Most frequently attempted username: "
            f"{top_username} ({top_username_count} successful-login events).\n"
        )


    if commands:

        top_command, top_command_count = commands.most_common(1)[0]

        report.write(
            f"- Most frequently observed command: "
            f"{top_command} ({top_command_count} occurrences).\n"
        )


    report.write(
        "- Repeated client, authentication and command patterns "
        "suggest automated or scripted SSH activity.\n"
    )

    report.write(
        "- Commands such as uname indicate system-information "
        "reconnaissance within the emulated environment.\n"
    )

    report.write(
        "- Cowrie login-success events represent authentication "
        "accepted by the honeypot and do not demonstrate compromise "
        "of the underlying EC2 host.\n"
    )


# --------------------------------
# TERMINAL SUMMARY
# --------------------------------

print("Analysis completed.")
print(f"Log files analyzed  : {len(log_files)}")
print(f"Total connections   : {total_connections}")
print(f"Unique source IPs   : {len(source_ips)}")
print(f"Successful logins   : {login_success}")
print(f"Failed logins       : {login_failed}")
print()
print(f"Report saved to: {report_file}")