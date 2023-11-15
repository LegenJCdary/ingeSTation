APPLICATION_DIR = "/etc/ingestation"

CONFIG_RULES = {
    "containers_sata_device_path": {
        "mode": "exclusive",
        "exclusive": ("application", "project")
    },
    "containers_sata_mount_path": {
        "mode": "exclusive",
        "exclusive": ("application", "project")
    },
    "destination_type": {
        "mode": "priority",
        "priority": ("project", "application")
    },
    "destination_root_path": {
        "mode": "priority",
        "priority": ("project", "application")
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
    "exclude_devices": {
        "mode": "inclusive",
        "inclusive": ("cli", "operator", "project", "application")
        "default": []
    },
    "include_devices": {
        "mode": "inclusive",
        "inclusive": ("cli", "operator", "project", "application")
        "default": []
    }
    "naming_codename": {
        "mode": "priority",
        "priority": ("project", "application")
    },
    "naming_log_file": {
        "mode": "priority",
        "priority": ("operator", "project", "application")
    },
    "notify": {
        "mode": "inclusive",
        "inclusive": ("operator", "project", "application")
        "default": {}
    },
    "permissions_primary_uid": {
        "mode": "priority",
        "priority": ("project", "application")
        "default": False
    },
    "permissions_primary_gid": {
        "mode": "priority",
        "priority": ("project", "application")
        "default": False
    },
    "permissions_primary_mode": {
        "mode": "priority",
        "priority": ("project", "application")
        "default": ""
    },
    "resources_thread_count": {
        "mode": "exclusive",
        "exclusive": ("application", "project")
    },
    "workdir": {
        "mode": "priority",
        "priority": ("operator", "project", "application")
    }
}
