# All fields are required!
# All dicts need to be dict type
# All path string should be limited to 4096 chars
template = {
    "containers": {
        "sata": {
            # str
            "device_path": None,
            # str
            "mount_path": None
        }
    },
    "destination": {
        # str
        "type": None,
        # str
        "root_path": None,
        # str
        "endpoint": None,
        "limits": {
            # int
            "critical": None,
            # int
            "warning": None
        }
    },
    "permissions": {
        "primary": {
            # int
            "uid": None,
            # int
            "gid": None,
            # str
            "mode": None
        },
    },
    "resources": {
        # int
        "thread_count": None
    },
    # str
    "workdir": None,
    "naming": {
        # str
        # len 255
        "log_file": None,
        # str
        # len 20
        "codename": None
    },
    # dict
    "notify": None,
    # list
    "exclude": None,
    # list
    "include": None
}
