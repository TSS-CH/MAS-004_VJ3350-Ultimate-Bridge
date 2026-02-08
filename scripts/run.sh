#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CONFIG_PATH="${1:-/etc/mas004_vj3350_ultimate_bridge/config.json}"

exec "$ROOT_DIR/.venv/bin/python" -m mas004_vj3350_ultimate_bridge --config "$CONFIG_PATH"
