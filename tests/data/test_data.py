validate_app = {
    "containers": {
        "sata": {
            "device_path": "/dev/sda",
            "mount_path": ""
        }
    },
    "syslog": False,
    "workdir": "/var/log/ingestation/${date}.log",
    "naming": {
        "log_file": "",
        "codename": ""
    },
    "notify": {
        "zh23": "zh23@ingestation.com"
    }
}

validate_proj = {
    "containers": {
        "sata": {
            "device_path": "/dev/sdb",
            "mount_path": "/mnt/proj"
        }
    },
    "destination": {
        "type": "nfs",
        "root_path": "/net/efs01",
        "endpoint": "",
        "limits": {
            "critical": 1,
            "warning": 5
        }
    },
    "source_options": {
        "skip": {
            "directories": [],
            "files": {
                "names": [],
                "extensions": []
            },
            "links": "",
            "empty": False
        }
    },
    "destination_options": {
        "preserve": True,
        "preserve_level": 3,
        "enforce_structure": {
            "file_pattern": "",
            "destination_pattern": ""
        }
    },
    "permissions": {
        "primary": {
            "uid": 0,
            "gid": 0,
            "mode": "0o700"
        },
        "acl": [
            {
                "uid": 1000,
                "gid": 1000,
                "access": "r",
                "default": False
            }
        ]
    },
    "resources": {
        "thread_count": 500
    },
    "syslog": True,
    "workdir": "/ingestation/logs/${date}.log",
    "naming": {
        "log_file": "",
        "codename": ""
    },
    "notify": {
        "I'm the best uploader": "uploader@ingestation.com"
    },
    "exclude_devices": [
        "DISKSN01"
    ],
    "include_devices": [
        "ExTERNAL_DISK00"
    ]
}

validate_op = {
    "destination_options": {
        "preserve": False,
        "preserve_level": 2,
        "enforce_structure": {
            "file_pattern": "f pattern",
            "destination_pattern": "dest pattern"
        }
    },
    "workdir": "/users/my_logs/${date}.log",
    "notify": {
        "HPC_upload": "upload_support@ingestation.com"
    },
    "exclude_devices": [
        "DISK_SN_XX"
    ],
    "include_devices": [
        "EXTERNAL_DISK01"
    ]
}

validate_op_error = {
    "destination_options": {
        "preserve": False,
        "preserve_level": "test_level",
        "enforce_structure": {
            "file_pattern": "f pattern",
            "destination_pattern": "dest pattern"
        }
    },
    "workdir": "/users/my_logs/${date}.log",
    "notify": {
        "HPC_upload": "upload_support@ingestation.com"
    },
    "exclude_devices": [
        "DISK_SN_XX"
    ],
    "include_devices": [
        "EXTERNAL_DISK01"
    ]
}

flatten_dict_simple = {"a": 1, "b": {"c": 2}}

flatten_dict_complex = {"a": 1, "b": {"c": 2}, "d": {"e": 3}, "f": {"g": 4}}
