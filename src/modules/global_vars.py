APPLICATION_DIR = "/etc/ingestation"

CONFIG_RULES = {
    "exclude_flatten": [
        "notify",
        "exclude_devices",
        "include_devices",
    ],

    "merge_to_dict": [
        "notify",
    ],

    "merge_to_list": [
        "exclude_devices",
        "include_devices",
    ]
}

MANDATORY_KEYS = [
    "containers_sata_device_path",
    "destination_root_path",
]

PRECEDENCE_RULES= {
    "app_proj_op": [
        "containers_sata_device_path",
        "containers_sata_mount_path",
    ],
    "app_op_proj": ["syslog"],
    "proj_app_op": [
        "permissions_primary_uid",
        "permissions_primary_gid",
        "permissions_primary_mode",
        "permissions_acl_0_uid",
        "permissions_acl_0_gid",
        "permissions_acl_0_access",
        "permissions_acl_0_default"
    ],
    "proj_op_app": [
        "destination_type",
        "destination_root_path",
        "destination_endpoint",
        "destination_limits_critical",
        "destination_limits_warning",
        "destination_options_preserve",
        "destination_options_preserve_level",
        "destination_options_enforce_structure_file_pattern",
        "destination_options_enforce_structure_destination_pattern",
    ],
    "op_app_proj": ["workdir", "naming_log_file", "naming_codename"],
    "op_proj_app": [
        "source_options_skip_links",
        "source_options_skip_empty",
        "resources_thread_count",
    ]
}
