application = {}
project = {}

operator = {
    "properties": {
        "exclude": {
            "$ref": "./objects"
        },
        "include": {
            "type": "array",
            "minItems": 0,
            "uniqueItems": True,
            "items": {
                "oneOf": [
                    {
                        "type": "integer",
                        "minimum": 3
                    },
                    {
                        "type": "string",
                        "minLength": 3
                    }
                ]
            }
        },
        "notify": {
            "type": "object",
            "minProperties": 1,
            "patternProperties": {
                "^[A-Za-z_]*$": {
                    "type": "string",
                    "minLength": 13
                }
            }
        },
        "workdir": {
            "type": "string",
            "minLength": 3
        }
    },
    "required": [],
    "not": {
        "anyOf": [
            {"required": ["destination"]},
            {"required": ["destination_options"]},
            {"required": ["source"]},
            {"required": ["source_options"]},
            {"required": ["permissions"]},
            {"required": ["resources"]},
            {"required": ["syslog"]},
            {"required": ["database"]},
            {"required": ["naming"]},
        ]
    }
}
