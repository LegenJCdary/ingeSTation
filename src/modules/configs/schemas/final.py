schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "containers_sata_device_path": {
            "type": "string",
            "maxLength": 4096
        },
        "containers_sata_mount_path": {
            "type": "string",
            "maxLength": 4096
        },
        "destination_type": {
            "type": "string",
            "maxLength": 4096
        },
        "destination_root_path": {
            "type": "string",
            "maxLength": 4096
        },
        "destination_endpoint": {
            "type": "string",
            "maxLength": 4096
        },
        "destination_limits_critical": {
            "type": "integer"
        },
        "destination_limits_warning": {
            "type": "integer"
        },
        "permissions_primary_uid": {
            "type": "integer"
        },
        "permissions_primary_gid": {
            "type": "integer"
        },
        "permissions_primary_mode": {
            "type": "string",
            "maxLength": 4096
        },
        "resources_thread_count": {
            "type": "integer"
        },
        "workdir": {
            "type": "string",
            "maxLength": 4096
        },
        "naming_log_file": {
            "type": "string",
            "maxLength": 255
        },
        "naming_codename": {
            "type": "string",
            "maxLength": 20
        },
        "notify": {
            "type": "array",
            "items": {
                "type": "string",
                "maxLength": 4096
            }
        },
        "exclude": {
            "type": "array",
            "items": {
                "type": "string",
                "maxLength": 4096
            }
        },
        "include": {
            "type": "array",
            "items": {
                "type": "string",
                "maxLength": 4096
            }
        }
    },
    "additionalProperties": False,
    "required": [
        "containers_sata_device_path",
        "containers_sata_mount_path",
        "destination_type",
        "destination_root_path",
        "destination_endpoint",
        "destination_limits_critical",
        "destination_limits_warning",
        "permissions_primary_uid",
        "permissions_primary_gid",
        "permissions_primary_mode",
        "resources_thread_count",
        "workdir",
        "naming_log_file",
        "naming_codename",
        "notify",
        "exclude",
        "include"
    ]
}
