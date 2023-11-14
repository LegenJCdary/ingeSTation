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
        "kuba": "kua@ingestation.com"
    },
    "exclude": [],
    "include": []
}

merged = {
    'containers_sata_device_path': '',
    'containers_sata_mount_path': '',
    'syslog': False,
    'workdir': '',
    'naming_log_file': '',
    'naming_codename': '',
    'notify': {
        'zh23': 'zh23@ingestation.com',
        'kuba': 'kuba@ingestation.com',
        "I'm the best uploader": 'uploader@ingestation.com',
        'HPC_upload': 'upload_support@ingestation.com'
    },
    'destination_type': '',
    'destination_root_path': '',
    'destination_endpoint': '',
    'destination_limits_critical': 0,
    'destination_limits_warning': 0,
    'source_options_skip_links': '',
    'source_options_skip_empty': False,
    'destination_options_preserve': True,
    'destination_options_preserve_level': 1,
    'destination_options_enforce_structure_file_pattern': '',
    'destination_options_enforce_structure_destination_pattern': '',
    'permissions_primary_uid': 0,
    'permissions_primary_gid': 0,
    'permissions_primary_mode': '0o700',
    'permissions_acl_0_uid': 1000,
    'permissions_acl_0_gid': 1000,
    'permissions_acl_0_access': 'r',
    'permissions_acl_0_default': False,
    'resources_thread_count': 0,
    'exclude_devices': [
        'DISKSN01',
        'DISKSN02'
    ],
    'include_devices': None
}

application = {
    'containers': {
        'sata': {
            'device_path': '',
            'mount_path': ''
        }
    },
    'syslog': False,
    'workdir': '',
    'naming': {
        'log_file': '',
        'codename': ''
    },
    'notify': {
        'zh23': 'zh23@ingestation.com',
        'kuba': 'kuba@ingestation.com',
    }
}

project = {
    'containers': {
        'sata': {
            'device_path': '',
            'mount_path': ''
        }
    },
    'destination': {
        'type': '',
        'root_path': '',
        'endpoint': '',
        'limits': {
            'critical': 0,
            'warning': 0
        }
    },
    'source_options': {
        'skip': {
            'directories': [],
            'files': {
                'names': [],
                'extensions': []
            },
            'links': '',
            'empty': False
        }
    },
    'destination_options': {
        'preserve': True,
        'preserve_level': 1,
        'enforce_structure': {
            'file_pattern': '',
            'destination_pattern': ''
        }
    },
    'permissions': {
        'primary': {
            'uid': 0,
            'gid': 0,
            'mode': '0o700'
        },
        'acl': [
            {
                'uid': 1000,
                'gid': 1000,
                'access': 'r',
                'default': False
            }
        ]
    },
    'resources': {
        'thread_count': 0
    },
    'syslog': False,
    'workdir': '',
    'naming': {
        'log_file': '',
        'codename': ''
    },
    'notify': {
        "I'm the best uploader": 'uploader@ingestation.com',
    },
    'exclude_devices': [
        'DISKSN01'
    ],
    'include_devices': []
}

operator = {
    'destination_options': {
        'preserve': True,
        'preserve_level': 1,
        'enforce_structure': {
            'file_pattern': '',
            'destination_pattern': ''
        }
    },
    'workdir': '',
    'notify': {
        'HPC_upload': 'upload_support@ingestation.com'
    },
    'exclude_devices': [
        'DISKSN02'
    ],
    'include_devices': []
}
