project = {
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
        "destination": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string"
                },
                "root_path": {
                    "type": "string"
                },
                "endpoint": {
                    "type": "string"
                },
                "limits": {
                    "type": "object",
                    "properties": {
                        "critical": {
                            "type": "integer"
                        },
                        "warning": {
                            "type": "integer"
                        }
                    },
                    "additionalProperties": False,
                    "required": [
                        "critical",
                        "warning"
                    ]
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
        "source_options": {
            "type": "object",
            "properties": {
                "skip": {
                    "type": "object",
                    "properties": {
                        "directories": {
                            "type": "array"
                        },
                        "files": {
                            "type": "object",
                            "properties": {
                                "names": {
                                    "type": "array"
                                },
                                "extensions": {
                                    "type": "array"
                                }
                            },
                            "additionalProperties": False,
                            "required": [
                                "names",
                                "extensions"
                            ]
                        },
                        "links": {
                            "type": "string"
                        },
                        "empty": {
                            "type": "boolean"
                        }
                    },
                    "additionalProperties": False,
                    "required": [
                        "directories",
                        "files",
                        "links",
                        "empty"
                    ]
                }
            },
            "additionalProperties": False,
            "required": [
                "skip"
            ]
        },
        "destination_options": {
            "type": "object",
            "properties": {
                "preserve": {
                    "type": "boolean"
                },
                "preserve_level": {
                    "type": "integer"
                },
                "enforce_structure": {
                    "type": "object",
                    "properties": {
                        "file_pattern": {
                            "type": "string"
                        },
                        "destination_pattern": {
                            "type": "string"
                        }
                    },
                    "additionalProperties": False,
                    "required": [
                        "file_pattern",
                        "destination_pattern"
                    ]
                }
            },
            "additionalProperties": False,
            "required": [
                "preserve",
                "preserve_level",
                "enforce_structure"
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
                            "type": "string"
                        }
                    },
                    "additionalProperties": False,
                    "required": [
                        "uid",
                        "gid",
                        "mode"
                    ]
                },
                "acl": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "uid": {
                                "type": "integer"
                            },
                            "gid": {
                                "type": "integer"
                            },
                            "access": {
                                "type": "string"
                            },
                            "default": {
                                "type": "boolean"
                            }
                        },
                        "additionalProperties": False,
                        "required": [
                            "uid",
                            "gid",
                            "access",
                            "default"
                        ]
                    }
                }
            },
            "additionalProperties": False,
            "required": [
                "primary",
                "acl"
            ]
        },
        "resources": {
            "type": "object",
            "properties": {
                "thread_count": {
                    "type": "integer"
                }
            },
            "additionalProperties": False,
            "required": [
                "thread_count"
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
        },
        "exclude_devices": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "include_devices": {
            "type": "array"
        }
    },
    "additionalProperties": False,
    "required": [
        "containers",
        "destination",
        "source_options",
        "destination_options",
        "permissions",
        "resources",
        "syslog",
        "workdir",
        "naming",
        "notify",
        "exclude_devices",
        "include_devices"
    ]
}
