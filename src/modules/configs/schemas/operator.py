operator = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
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
        "workdir": {
            "type": "string"
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
        "destination_options",
        "workdir",
        "notify",
        "exclude_devices",
        "include_devices"
    ]
}
