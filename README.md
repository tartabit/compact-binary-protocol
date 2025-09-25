# compact-binary-protocol

A small, self-contained Python library that defines the compact binary protocol used by Tartabit client components.

Features:
- Encoding helpers (VarString, etc.)
- Data model classes for typed data items (DataLocation, DataMulti, DataKv, ...)
- Packet classes for telemetry, configuration (server→device), and update requests/status
- Decoding helpers for responses and header parsing

All multi-byte values are encoded using big-endian format.

## Install (pypi)

To install the package from PyPI, run:

```bash
pip install compact-binary-protocol
```

## Install (local)
This repository is part of a monorepo. To use the library from adjacent components, import it directly via the package name `compact_binary_protocol` (no installation step needed if package path is in PYTHONPATH). For packaging, add a minimal pyproject or install in editable mode:

```
pip install -e ./compact-binary-protocol
```

## Quick start
```python
from compact_binary_protocol import (
    DataMulti, TelemetryPacket,
)

imei = "358419511056392"
item = DataMulti(
    battery=95,
    rssi=30,
    first_timestamp=1724900000,
    interval=60,
    records=[{"temperature": 21.5, "humidity": 40.0}]
)
tele = TelemetryPacket(imei, 1724900000, 1, 'T', item)
packet_bytes = tele.to_bytes()
print(packet_bytes.hex())
```

## API Overview
- encode_var_string(str) -> bytes
- PacketDecoder.parse_response_data(str)
- PacketDecoder.decode_packet_header(hex_str) -> (version, command, transaction_id, remainder_bytes)
- DataReader for reading from bytes
- DataLocation (gnss/cell)
- DataBasic, DataMulti, DataNull, DataSteps, DataVersions, DataNetworkInfo, DataCustomerId, DataKv
- Packets: Packet (base), TelemetryPacket, ConfigPacket (server→device body decoder), UpdateRequestPacket, UpdateStatusPacket

## Building
To build the package, run the following command:
```bash
pip install build twine
python -m venv .venv
. venv/bin/activate
python -m build
twine upload dist/*
```

## License
Copyright 2024-2025 Tartabit, LLC.
