#!/usr/bin/env python3

import sys
import requests
import json

# Synology will pass these as positional arguments
if len(sys.argv) < 4:
    print("badauth: Missing required parameters (username, password, hostname).")
    sys.exit(1)

ZONE_ID = sys.argv[1]    # $1 = username
API_TOKEN = sys.argv[2]  # $2 = password
RECORD_ID = sys.argv[3]  # $3 = hostname
IP = sys.argv[4] if len(sys.argv) > 4 else None  # $4 = ip (optional)

# Set default TTL and proxied status (modify as needed)
TTL = 1
PROXIED = True

def get_public_ip():
    """Retrieve the public IP address if $4 (IP) is not provided."""
    try:
        response = requests.get("http://ipinfo.io/ip")
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        print(f"badauth: Failed to get public IP - {e}")
        sys.exit(1)

def update_dns_record(zone_id, api_token, record_id, ip):
    """Update the DNS record on Cloudflare."""
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    data = {
        "type": "A",
        "content": ip,
        "ttl": TTL,
        "proxied": PROXIED,
    }
    try:
        response = requests.patch(url, headers=headers, data=json.dumps(data))
        response_data = response.json()
        if response_data.get("success"):
            print("good")
        else:
            print(f"badauth: {response_data}")
            sys.exit(1)
    except Exception as e:
        print(f"badauth: Failed to update DNS record - {e}")
        sys.exit(1)

if __name__ == "__main__":
    if not IP:
        IP = get_public_ip()

    update_dns_record(ZONE_ID, API_TOKEN, RECORD_ID, IP)


