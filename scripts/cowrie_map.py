import json
import time
import requests
import folium
from pathlib import Path
from collections import Counter


# Cowrie log directory
LOG_DIR = Path.home() / "cowrie" / "var" / "log" / "cowrie"


# Count connections from each source IP
source_ips = Counter()


# Read all Cowrie JSON logs
log_files = sorted(LOG_DIR.glob("cowrie.json*"))


for log_file in log_files:

    with log_file.open("r", errors="replace") as file:

        for line in file:

            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            # Only process connection events
            if event.get("eventid") != "cowrie.session.connect":
                continue

            ip = event.get("src_ip")

            if not ip:
                continue

            source_ips[ip] += 1


print(f"Found {len(source_ips)} unique source IPs.")


# Create world map
world_map = folium.Map(
    location=[20, 0],
    zoom_start=2,
    tiles="CartoDB positron"
)


# Perform GeoIP lookups
for ip, connections in source_ips.most_common():

    print(f"Looking up {ip}...")

    try:

        url = f"https://ip-api.com/json/{ip}"

        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code != 200:
            print(f"  HTTP error: {response.status_code}")
            continue

        data = response.json()

        if data.get("status") != "success":
            print(f"  Could not locate {ip}")
            continue

        latitude = data.get("lat")
        longitude = data.get("lon")
        country = data.get("country", "Unknown")
        city = data.get("city", "Unknown")
        isp = data.get("isp", "Unknown")

        # Marker information
        popup_text = f"""
        <b>Source IP:</b> {ip}<br>
        <b>Country:</b> {country}<br>
        <b>City:</b> {city}<br>
        <b>ISP:</b> {isp}<br>
        <b>Connections:</b> {connections}
        """

        # Add marker to map
        folium.Marker(
            location=[latitude, longitude],
            popup=popup_text,
            tooltip=f"{ip} - {connections} connections"
        ).add_to(world_map)

        print(
            f"  {country}, {city} - "
            f"{connections} connections"
        )

        # Delay between API requests
        time.sleep(1)

    except requests.RequestException as error:

        print(f"  Network error: {error}")

    except Exception as error:

        print(f"  Error processing {ip}: {error}")


# Save map
output_file = Path.home() / "cowrie_attack_map.html"

world_map.save(output_file)

print()
print("Map creation completed.")
print(f"Map saved to: {output_file}")