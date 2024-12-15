# Synology NAS DDNS with Cloudflare

This Python script integrates with Synology DSM to dynamically update DNS records on Cloudflare. It works with Synology's DDNS system by accepting parameters directly from DSM's DDNS configuration.

## Features

- Supports Cloudflare API for DNS updates.
- Compatible with Synology DSM's DDNS feature.
- Automatically fetches public IP if not provided.
- Tested and verified on **DSM 7.2.2**.

## Installation

1. **SSH into Synology NAS**:
   - Open a terminal on your computer and connect to your Synology NAS via SSH:
   - Make the script executable:
     ```bash
     ssh admin@<NAS_IP>
     ```

1. **Copy the Script to Synology NAS**:
   - Download the Script:
     ```bash
     wget https://raw.githubusercontent.com/syanyong/synology-nas-ddns-cloudflare/refs/heads/main/cloudflare_ddns.py .
     ```
   - Copy:
     ```bash
     cp cloudflare_ddns.py /usr/syno/bin/ddns
     ```
   - Make the script executable:
     ```bash
     sudo chmod +x /usr/syno/bin/ddns/cloudflare_ddns.py
     ```

2. **Update Synology Configuration**:
   - Edit `/etc.defaults/ddns_provider.conf`:
     ```ini
     [Cloudflare]
         modulepath=/usr/syno/bin/ddns/cloudflare_ddns.py
         queryurl=https://api.cloudflare.com
     ```


3. **Add DDNS in DSM (UI)**:
   - Go to **Control Panel > External Access > DDNS**.
   - Add a new entry:
     - **Service Provider**: `Cloudflare`
     - **Hostname**: `<RECORD_ID>` (DNS record ID)
     - **Username**: `<ZONE_ID>` (Cloudflare Zone ID)
     - **Password**: `<API_TOKEN>` (Cloudflare API Token)

## Compatibility

- Tested and verified on:
  - Synology **DSM 7.2.2**
  - Cloudflare API v4
- Expected to work on all DSM 7.x versions.


## Usage

1. **Parameters Passed by Synology**:
   - `$1`: `ZONE_ID` (username in DSM configuration)
   - `$2`: `API_TOKEN` (password in DSM configuration)
   - `$3`: `RECORD_ID` (hostname in DSM configuration)
   - `$4`: `IP` (optional, automatically detected if not provided)

2. **Manual Execution**:
   You can test the script manually:
   ```bash
   /usr/syno/bin/ddns/cloudflare_ddns.py <ZONE_ID> <API_TOKEN> <RECORD_ID> <IP>
   ```

## Author
This project was created and maintained by Sarucha Yanyong.
GitHub: @syanyong


   
