final = {
    "containers": {
        "sata": {
            "device_path": "",
            "mount_path": ""
        }
    },
    "destination": {
        "type": "",
        "root_path": "",
        "endpoint": "",
        "limits": {
            "critical": 0,
            "warning": 0
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
        "preserve_level": 1,
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
        "thread_count": 0
    },
    "syslog": False,
    "workdir": "",
    "database": {
        "path": "",
        "table_name": ""
    },
    "naming": {
        "log_file": "",
        "codename": ""
    },
    "notify": {
        "sadmin": "jakub.wierzbowski@aptiv.com"
    },
    "exclude": [],
    "include": []
}