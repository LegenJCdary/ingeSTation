# pylint: disable=duplicate-code

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
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
        "workdir": {
            "type": "string",
            "maxLength": 4096,
            "minLength": 2
        }
    },
    "additionalProperties": False,
    "required": []
}
