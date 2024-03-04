APPLICATION_DIR = "/etc/ingestation"
APPLICATION_CONF = "/etc/ingestation/ingestation.json"

CONFIG_RULES = {
    "containers_sata_device_path": {
        "mode": "exclusive",
        "exclusive": ("application",)
    },
    "containers_sata_mount_path": {
        "mode": "exclusive",
        "exclusive": ("application",)
    },
    "destination_endpoint": {
        "mode": "priority",
        "priority": ("project", "application")
    },
    "destination_limits_critical": {
        "mode": "priority",
        "priority": ("project", "application")
    },
    "destination_limits_warning": {
        "mode": "priority",
        "priority": ("project", "application")
    },
    "destination_root_path": {
        "mode": "priority",
        "priority": ("project", "application")
    },
    "destination_type": {
        "mode": "priority",
        "priority": ("project", "application")
    },
    "exclude": {
        "mode": "inclusive",
        "inclusive": ("cli", "operator", "project", "application"),
        "default": []
    },
    "include": {
        "mode": "inclusive",
        "inclusive": ("cli", "operator", "project", "application"),
        "default": []
    },
    "naming_codename": {
        "mode": "priority",
        "priority": ("operator", "project", "application")
    },
    "naming_log_file": {
        "mode": "priority",
        "priority": ("operator", "project", "application")
    },
    "notify": {
        "mode": "inclusive",
        "inclusive": ("operator", "project", "application"),
        "default": {}
    },
    "permissions_primary_gid": {
        "mode": "priority",
        "priority": ("project", "application"),
        "default": False
    },
    "permissions_primary_mode": {
        "mode": "priority",
        "priority": ("project", "application"),
        "default": ""
    },
    "permissions_primary_uid": {
        "mode": "priority",
        "priority": ("project", "application"),
        "default": False
    },
    "resources_thread_count": {
        "mode": "exclusive",
        "exclusive": ("application", "project")
    },
    "smtp_password": {
        "mode": "exclusive",
        "exclusive": ("application", "project")
    },
    "smtp_server": {
        "mode": "exclusive",
        "exclusive": ("application", "project")
    },
    "smtp_user": {
        "mode": "exclusive",
        "exclusive": ("application", "project")
    },
    "workdir": {
        "mode": "priority",
        "priority": ("operator", "project", "application")
    }
}
