# pylint: disable=duplicate-code

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
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
            "required": [
                "log_file",
                "codename"
            ]
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
    "required": []
}
