# pylint: disable=duplicate-code

schema = {
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
                            "type": "string",
                            "maxLength": 4096,
                            "minLength": 4,
                            "pattern": "^/\\w+"
                        },
                        "mount_path": {
                            "type": "string",
                            "maxLength": 4096,
                            "minLength": 1
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
            "required": ["sata"]
        },
        "destination": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "maxLength": 4096,
                    "minLength": 2
                },
                "root_path": {
                    "type": "string",
                    "maxLength": 4096
                },
                "endpoint": {
                    "type": "string",
                    "maxLength": 4096
                },
                "limits": {
                    "type": "object",
                    "properties": {
                        "critical": {
                            "type": "integer",
                            "minimum": 1
                        },
                        "warning": {
                            "type": "integer",
                            "minimum": 1
                        }
                    },
                    "additionalProperties": False,
                    "required": ["critical"]
                }
            },
            "additionalProperties": False,
            "required": [
                "type",
                "root_path",
                "endpoint",
                "limits"
            ]
        },
        "permissions": {
            "type": "object",
            "properties": {
                "primary": {
                    "type": "object",
                    "properties": {
                        "uid": {
                            "type": "integer"
                        },
                        "gid": {
                            "type": "integer"
                        },
                        "mode": {
                            "type": "string",
                            "pattern": "^0o[0-7]{4}$"
                        }
                    },
                    "additionalProperties": False,
                    "required": ["mode"]
                }
            },
            "additionalProperties": False,
            "required": ["primary"]
        },
        "resources": {
            "type": "object",
            "properties": {
                "thread_count": {
                    "type": "integer"
                }
            },
            "additionalProperties": False,
            "required": ["thread_count"]
        },
        "workdir": {
            "type": "string",
            "maxLength": 4096
        },
        "naming": {
            "type": "object",
            "properties": {
                "log_file": {
                    "type": "string",
                    "maxLength": 255
                },
                "codename": {
                    "type": "string",
                    "maxLength": 20,
                    "minLength": 3
                }
            },
            "additionalProperties": False,
            "required": []
        },
        "notify": {
            "type": "array",
            "items": {
                "type": "string",
                "maxLength": 4096,
                "minLength": 11
            }
        },
        "exclude": {
            "type": "array",
            "items": {
                "type": "string",
                "maxLength": 4096,
                "minLength": 6
            }
        },
        "include": {
            "type": "array",
            "items": {
                "type": "string",
                "maxLength": 4096,
                "minLength": 6
            }
        }
    },
    "additionalProperties": False,
    "required": ["containers"]
}
