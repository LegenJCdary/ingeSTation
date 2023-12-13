# pylint: disable=duplicate-code

application = {
    "non_mandatory_key": {
        "containers": {
            "sata": {
                "device_path": "/dev/sda",
                "mount_path": "/mnt"
            }
        },
        "exclude": [
            "EX_DISK_APP"
        ]
    },
    "validation_passed": {
        "containers": {
            "sata": {
                "device_path": "/dev/sda",
                "mount_path": "/mnt"
            }
        },
        "workdir": "/var/log/ingestation",
        "naming": {
            "log_file": "{date}.log",
            "codename": "CODE"
        },
        "notify": [
            "zh23@ingestation.com",
            "kuba@ingestation.com"
        ],
        "exclude": [
            "EX_DISK_APP"
        ],
        "include": [
            "IN_DISK_APP01", "IN_DISK_APP02"
        ]
    }
}

project = {
    "non_mandatory_key": {
        "destination": {
            "type": "nfs",
            "root_path": "/net/efs01",
            "endpoint": "ep01",
            "limits": {
                "critical": 1,
                "warning": 1
            }
        }
    },
    "validation_passed": {
        "destination": {
            "type": "nfs",
            "root_path": "/net/efs01",
            "endpoint": "ep01",
            "limits": {
                "critical": 1,
                "warning": 1
            }
        },
        "permissions": {
            "primary": {
                "uid": 0,
                "gid": 0,
                "mode": "0o0700"
            }
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
        "exclude": [
            "DISKSN03"
        ],
        "include": []
    }
}

operator = {
    "non_mandatory_key": {
        "workdir": "/users/my_logs/${date}.log",
        "naming": {
            "log_file": "ingestion.log",
            "codename": "test"
        }
    },
    "validation_passed": {
        "workdir": "/users/my_logs/${date}.log",
        "naming": {
            "log_file": "ingestion.log",
            "codename": "test"
        },
        "notify": [
            "upload_support@ingestation.com"
        ],
        "exclude": [
            "DISKSN04"
        ],
        "include": ["IN_OP_DISK"]
    }
}
