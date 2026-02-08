from __future__ import annotations

from typing import Iterable

ULT_ACK = 0x06
ULT_NAK = 0x15


def build_command(command: str, args: Iterable[str] | None = None) -> bytes:
    parts = [(command or "").strip()]
    for arg in args or ():
        parts.append(str(arg))
    line = ";".join(parts) + ";\r\n"
    return line.encode("utf-8")


def parse_result(raw: bytes) -> tuple[bool, str, list[str]]:
    if not raw:
        raise ValueError("Ultimate response empty")

    state = raw[0]
    if state not in (ULT_ACK, ULT_NAK):
        raise ValueError("Ultimate response missing ACK/NAK prefix")

    text = raw[1:].decode("utf-8", errors="replace").strip()
    text = text.replace("\r", "").replace("\n", "")
    fields = [f for f in text.split(";") if f != ""]
    result_code = fields[0] if fields else ""
    args = fields[1:] if len(fields) > 1 else []
    return state == ULT_ACK, result_code, args
