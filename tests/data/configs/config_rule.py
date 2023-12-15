application = {
    "exclusive_over_defined": {
        "resources": {
            "thread_count": 1
        }
    },
    "exclusive_undefined": {
        "resources": {
            "thread_count": 0
        }
    },
    "exclusive_passed": {
        "containers": {
            "sata": {
                "device_path": "/dev/sda"}
        }
    },
    "inclusive_passed": {
        "notify": [
            "zh23@ingestation.com",
            "kuba@ingestation.com"
        ]
    },
    "priority_passed": {
        "workdir": "/var/log/ingestation"
    }
}

project = {
    "exclusive_over_defined": {
        "resources": {
            "thread_count": 2
        }
    },
    "exclusive_undefined": {
        "resources": {
        }
    },
    "inclusive_passed": {
        "notify": [
            "uploader@ingestation.com"
        ]
    },
    "priority_passed": {
        "workdir": "/var/log/ingestation2"
    }
}

operator = {
    "inclusive_passed": {
        "notify": [
            "upload_support@ingestation.com"
        ]
    },
    "priority_passed": {
        "workdir": "/users/my_logs/${date}.log"
    },
    "priority_none": {
        "destination_type": "nfs"
    }
}

result = {
    "exclusive_passed": "/dev/sda",
    "inclusive_passed": [
        'upload_support@ingestation.com',
        'uploader@ingestation.com',
        'zh23@ingestation.com',
        'kuba@ingestation.com'
    ],
    "priority_passed": "/users/my_logs/${date}.log"
}
