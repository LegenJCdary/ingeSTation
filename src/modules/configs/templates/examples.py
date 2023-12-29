cli = {
    "workdir": "/users/my_logs/${date}.log",
    "exclude_devices": [
        "DISKSN01"
    ],
    "include_devices": []
}

application = {
    "containers": {
        "sata": {
            "device_path": "/dev/sda",
            "mount_path": ""
        }
    },
    "resources": {
        "thread_count": 0
    },
    "workdir": "/var/log/ingestation/${date}.log",
    "naming": {
        "log_file": "",
        "codename": ""
    },
    "notify": [
        "zh23@ingestation.com",
        "kuba@ingestation.com"
    ],
    "exclude_devices": [
        "DISKSN02"
    ],
    "include_devices": []
}

project = {
    "destination": {
        "type": "nfs",
        "root_path": "/net/efs01",
        "endpoint": "",
        "limits": {
            "critical": 0,
            "warning": 0
        }
    },
    "permissions": {
        "primary": {
            "uid": 0,
            "gid": 0,
            "mode": "0o700"
        },
    },
    "resources": {
        "thread_count": 0
    },
    "workdir": "/var/log/ingestation/",
    "naming": {
        "log_file": "ingestion.log",
        "codename": "test"
    },
    "notify": [
        "uploader@ingestation.com"
    ],
    "exclude_devices": [
        "DISKSN03"
    ],
    "include_devices": []
}

operator = {
    "workdir": "/users/my_logs/${date}.log",
    "naming": {
        "log_file": "ingestion.log",
        "codename": "test"
    },
    "notify": [
        "upload_support@ingestation.com"
    ],
    "exclude_devices": [
        "DISKSN04"
    ],
    "include_devices": []
}
