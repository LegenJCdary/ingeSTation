# pylint: disable=duplicate-code

from ingestation_test.utils import generate_string


application = {
    "unrecognized_key": {
        "container": {
            "sata": {
                "device_path": "/dev/sda",
                "mount_path": "/mnt"
            }
        }
    },
    "mandatory_key": {
        "containers": {
            "sata": {
                "device_path": "/dev/sda"
            }
        }
    },
    "invalid_data_type": {
        "containers": {
            "sata": {
                "device_path": 1,
                "mount_path": "/mnt"
            }
        }
    },
    "too_long_value": {
        "containers": {
            "sata": {
                "device_path": generate_string(4097),
                "mount_path": "/mnt"
            }
        }
    }
}

project = {
    "unrecognized_key": {
        "permission": {
            "primary": {
                "uid": 0,
                "gid": 0,
                "mode": "0o0700"
            }
        }
    },
    "mandatory_key": {
        "destination": {
            "type": "nfs",
            "root_path": "/net/efs01",
            "endpoint": "ep01",
            "limits": {
                "warning": 1
            }
        }
    },
    "invalid_data_type": {
        "destination": {
            "type": "nfs",
            "root_path": "/net/efs01",
            "endpoint": "ep01",
            "limits": {
                "critical": "test",
                "warning": 0
            }
        }
    },
    "too_long_value": {
        "naming": {
            "log_file": generate_string(256),
            "codename": "test"
        }
    }
}

operator = {
    "unrecognized_key": {
        "workdir": "/users/my_logs/${date}.log",
        "name": {
            "log_file": "ingestion.log",
            "codename": "test"
        }
    },
    "mandatory_key": {
        "naming": {
            "log_file": "ingestion.log"}
    },
    "invalid_data_type": {
        "workdir": "/users/my_logs/${date}.log",
        "naming": {
            "log_file": "ingestion.log",
            "codename": 7
        }
    },
    "too_long_value": {
        "naming": {
            "log_file": "ingestion.log",
            "codename": generate_string(21)
        }
    }
}
