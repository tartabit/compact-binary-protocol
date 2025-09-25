# compact-binary-protocol

A small, self-contained Python library that defines the compact binary protocol used by Tartabit client components.

Features:
- Encoding helpers
- Data model classes for location and sensor data
- Packet classes for telemetry, configuration, power on, update requests/status
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
    SensorDataMulti, TelemetryPacket,
)

imei = "358419511056392"
sensor = SensorDataMulti(
    battery=95,
    rssi=30,
    first_timestamp=1724900000,
    interval=60,
    records=[{"temperature": 21.5, "humidity": 40.0}]
)
tele = TelemetryPacket(imei=imei, timestamp=1724900000, transaction_id=1, sensor_data=sensor, event=0)
packet_bytes = tele.to_bytes()
print(packet_bytes.hex())
```

## API Overview
- encoding.encode_var_string(str) -> bytes
- decoder.PacketDecoder.parse_response_data(str)
- decoder.PacketDecoder.decode_packet_header(hex_str)
- decoder.DataReader for reading from bytes
- data.LocationData (gnss/cell)
- data.SensorData*, data.SensorDataMulti, data.SensorDataNull, data.SensorDataSteps, data.SensorDataVersions, data.SensorDataNetworkInfo
- packets.Packet base + TelemetryPacket, ConfigPacket, UpdateRequestPacket, UpdateStatusPacket

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
