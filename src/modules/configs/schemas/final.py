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
                            "minLength": 4,
                            "maxLength": 4096,
                            "pattern": "^/\\w+"
                        },
                        "mount_path": {
                            "type": "string",
                            "minLength": 2,
                            "maxLength": 4096,
                            "pattern": "^/\\w+"
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
                "endpoint": {
                    "type": "string",
                    "minLength": 1,
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
                },
                "root_path": {
                    "type": "string",
                    "minLength": 2,
                    "maxLength": 4096
                },
                "type": {
                    "type": "string",
                    "minLength": 2,
                    "maxLength": 4096
                }
            },
            "additionalProperties": False,
            "required": [
                "endpoint",
                "limits",
                "root_path",
                "type"
            ]
        },
        "exclude": {
            "type": "array",
            "items": {
                "type": "string",
                "minLength": 6,
                "maxLength": 4096
            }
        },
        "include": {
            "type": "array",
            "items": {
                "type": "string",
                "minLength": 6,
                "maxLength": 4096
            }
        },
        "naming": {
            "type": "object",
            "properties": {
                "codename": {
                    "type": "string",
                    "minLength": 5,
                    "maxLength": 20
                },
                "log_file": {
                    "type": "string",
                    "minLength": 5,
                    "maxLength": 255
                }
            },
            "additionalProperties": False,
            "required": [
                "codename",
                "log_file"
            ]
        },
        "notify": {
            "type": "array",
            "items": {
                "type": "string",
                "minLength": 11,
                "maxLength": 4096
            }
        },
        "permissions": {
            "type": "object",
            "properties": {
                "primary": {
                    "type": "object",
                    "properties": {
                        "gid": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 4096
                        },
                        "mode": {
                            "type": "string",
                            "pattern": "^0o[0-7]{4}$"
                        },
                        "uid": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 4096
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
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 500
                }
            },
            "additionalProperties": False,
            "required": ["thread_count"]
        },
        "workdir": {
            "type": "string",
            "minLength": 2,
            "maxLength": 4096
        }
    },
    "additionalProperties": False,
    "required": [
        "containers",
        "destination",
        "exclude",
        "include",
        "naming",
        "notify",
        "permissions",
        "resources",
        "workdir",
    ]
}
