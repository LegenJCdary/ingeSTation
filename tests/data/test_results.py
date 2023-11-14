parse_app = {
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

parse_proj = {
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

parse_op = {
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

flatten_simple_dict_result = {"a": 1, "b_c": 2}

flatten_complex_dict_result = {"a": 1, "b#c": 2, "d": {"e": 3}, "f#g": 4}

final_conf = {
    'containers_sata_device_path': '/dev/sda',
    'containers_sata_mount_path': '',
    'syslog': False,
    'workdir': '/users/my_logs/${date}.log',
    'naming_log_file': '',
    'naming_codename': '',
    'notify': {
        'zh23': 'zh23@ingestation.com',
        "I'm the best uploader": 'uploader@ingestation.com',
        'HPC_upload': 'upload_support@ingestation.com'
    },
    'destination_type': 'nfs',
    'destination_root_path': '/net/efs01',
    'destination_endpoint': '',
    'destination_limits_critical': 1,
    'destination_limits_warning': 5,
    'source_options_skip_links': '',
    'source_options_skip_empty': False,
    'destination_options_preserve': True,
    'destination_options_preserve_level': 3,
    'destination_options_enforce_structure_file_pattern': '',
    'destination_options_enforce_structure_destination_pattern': '',
    'permissions_primary_uid': 0,
    'permissions_primary_gid': 0,
    'permissions_primary_mode': '0o700',
    'permissions_acl_0_uid': 1000,
    'permissions_acl_0_gid': 1000,
    'permissions_acl_0_access': 'r',
    'permissions_acl_0_default': False,
    'resources_thread_count': 500,
    'exclude_devices': [
        'DISKSN01', 'DISK_SN_XX'
    ],
    'include_devices': [
        'ExTERNAL_DISK00',
        'EXTERNAL_DISK01'
    ]
}
