# ingeSTation
Python application designed for data ingest(at)ion and controlling operations on ingest stations.
ST stands for Speedy Transfer or Super Turbo.

# Use case
Standard approach to data ingest using this application would be:
- Admin scope:
    1. Prepare and configure ingest stations with Linux OS.
    2. Ensure target filesystem is connected to stations.
    3. Install required software: (cryptestup), Python, rsync.
    4. Configure permissions (or sudo access) for ingest operators.
    5. Create and secure config files required by ingeSTation.
- Operator scope:
    1. Create Python venv and install ingeSTation with pip.
    2. Create operator config file required by ingeSTation.
    3. Connect external drives to station.
    4. Activate venv and run ingestation binary.
