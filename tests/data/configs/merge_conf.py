# pylint: disable=duplicate-code

dct1 = {
    "a": 1,
    "b": {
        "c": 2
    }
}

expect1 = {"a": 1, "b_c": 2}

dct2 = {
    "a": 1,
    "b": {
        "c": 2
    },
    "d": [3, 4]
}

expect2 = {"a": 1, "b_c": 2, "d": [3, 4]}

dct3 = {
    "containers": {
        "sata": {
            "device_path": "/dev/sda",
            "mount_path": "/mnt"
        }
    },
    "resources": {
        "thread_count": 1
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

expect3 = {
    "containers_sata_device_path": "/dev/sda",
    "containers_sata_mount_path": "/mnt",
    "resources_thread_count": 1,
    "workdir": "/var/log/ingestation",
    "naming_log_file": "{date}.log",
    "naming_codename": "CODE",
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
