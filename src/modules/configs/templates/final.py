<<<<<<< HEAD
config = {
    "containers": {
        "sata": {
            "device_path": None,
=======
# All fields are required!
# All dicts need to be dict type
# All path string should be limited to 4096 chars
config = {
    "containers": {
        "sata": {
            # str
            "device_path": None,
            # str
>>>>>>> 277e9fa9b72346b65566d29496a9d68678db06a8
            "mount_path": None
        }
    },
    "destination": {
<<<<<<< HEAD
        "root_path": None,
        "endpoint": None,
        "limits": {
            "critical": None,
=======
        # str
        "root_path": None,
        # str
        "endpoint": None,
        "limits": {
            # int
            "critical": None,
            # int
>>>>>>> 277e9fa9b72346b65566d29496a9d68678db06a8
            "warning": None
        }
    },
    "permissions": {
        "primary": {
<<<<<<< HEAD
            "uid": None,
            "gid": None,
=======
            # int
            "uid": None,
            # int
            "gid": None,
            # str
>>>>>>> 277e9fa9b72346b65566d29496a9d68678db06a8
            "mode": None
        },
    },
    "resources": {
<<<<<<< HEAD
        "thread_count": None
    },
    "workdir": None,
    "naming": {
        "log_file": None,
        "codename": None
    },
    "notify": None,
    "exclude": None,
=======
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
>>>>>>> 277e9fa9b72346b65566d29496a9d68678db06a8
    "include": None
}
