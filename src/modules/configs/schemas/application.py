application = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "containers": {
            "type": "object",
            "properties": {
                "sata": {
                    "type": "object",
                    "properties": {
                        "device_path": {
                            "type": "string"
                        },
                        "mount_path": {
                            "type": "string"
                        }
                    },
                    "additionalProperties": False,
                    "required": [
                        "device_path",
                        "mount_path"
                    ]
                }
            },
            "additionalProperties": False,
            "required": [
                "sata"
            ]
        },
        "syslog": {
            "type": "boolean"
        },
        "workdir": {
            "type": "string"
        },
        "naming": {
            "type": "object",
            "properties": {
                "log_file": {
                    "type": "string"
                },
                "codename": {
                    "type": "string"
                }
            },
            "additionalProperties": False,
            "required": [
                "log_file",
                "codename"
            ]
        },
        "notify": {
            "type": "object",
            "additionalProperties": True
        }
    },
    "additionalProperties": False,
    "required": [
        "containers",
        "syslog",
        "workdir",
        "naming",
        "notify"
    ]
}
