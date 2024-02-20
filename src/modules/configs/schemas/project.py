# pylint: disable=duplicate-code

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "destination": {
            "type": "object",
            "properties": {
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
                },
                "root_path": {
                    "type": "string",
                    "maxLength": 4096
                },
                "type": {
                    "type": "string",
                    "maxLength": 4096,
                    "minLength": 2
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
        },
        "naming": {
            "type": "object",
            "properties": {
                "codename": {
                    "type": "string",
                    "maxLength": 20,
                    "minLength": 3
                },
                "log_file": {
                    "type": "string",
                    "maxLength": 255
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
        "permissions": {
            "type": "object",
            "properties": {
                "primary": {
                    "type": "object",
                    "properties": {
                        "gid": {
                            "type": "integer"
                        },
                        "mode": {
                            "type": "string",
                            "pattern": "^0o[0-7]{4}$"
                        },
                        "uid": {
                            "type": "integer"
                        }
                    },
                    "additionalProperties": False,
                    "required": [
                        "uid",
                        "gid",
                        "mode"
                    ]
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
        "smtp": {
            "type": "object",
            "properties": {
                "password": {
                    "type": "string",
                    "maxLength": 255,
                    "minLength": 15
                },
                "server": {
                    "type": "string",
                    "maxLength": 255,
                    "minLength": 11
                },
                "user": {
                    "type": "string",
                    "maxLength": 255,
                    "minLength": 3
                }
            },
            "additionalProperties": False,
            "required": ["server"]
        },
        "workdir": {
            "type": "string",
            "maxLength": 4096,
            "minLength": 2
        }
    },
    "additionalProperties": False,
    "required": []
}
