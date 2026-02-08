# MAS-004_VJ3350-Ultimate-Bridge

Basis-Client und Daemon fuer Videojet 3350 ueber Ultimate-Protokoll.

## Protokoll
- UTF-8 Text
- Delimiter `;`
- Ende `CRLF`
- Antwort startet mit `ACK` (0x06) oder `NAK` (0x15)

## Service-Dateien
- `systemd/mas004-vj3350-ultimate-bridge.service`
- `scripts/install.sh`
- `scripts/run.sh`
- `scripts/default_config.json`

## Installation auf Raspi
```bash
cd /opt/MAS-004_VJ3350-Ultimate-Bridge
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
chmod +x scripts/*.sh
./scripts/install.sh
```

## Config
`/etc/mas004_vj3350_ultimate_bridge/config.json`

- `enabled`: Service aktiv/inaktiv
- `simulation`: wenn `true`, keine Live-Verbindung
- `host`, `port`: Laser Endpoint
- `probe_command`: Default `GetVersion`
- `timeout_s`, `poll_interval_s`
