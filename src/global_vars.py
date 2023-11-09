import os

APPLICATION_DIR = "/etc/ingestation"

options = {
    "operator_conf": os.path.join(APPLICATION_DIR, "operator.json"),
    "project_conf": os.path.join(APPLICATION_DIR, "project.json"),
    "application_conf": os.path.join(APPLICATION_DIR, "application.json")
}
