import os

APPLICATION_DIR = "/etc/ingestation"

options = {
    "project_conf": os.path.join(APPLICATION_DIR, "project.json"),
    "application_conf": os.path.join(APPLICATION_DIR, "application.json")
}
