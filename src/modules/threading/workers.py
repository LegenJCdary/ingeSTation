import concurrent.futures

from ..uploading.chunks import Crate
from ..uploading.upload import Upload
from ..checks.healthchecks import HealthCheck


class Workers:

    def __init__(self):
        pass

    def run_overseer(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            self.run_fs_healthcheck()
            self.run_container_healthcheck()
            for crate in self.crates:
                self.start_working(crate)
        pass

    def run_fs_healthcheck(self):
        HealthCheck.check_fs()
        pass

    def run_container_healthcheck(self):
        HealthCheck.check_device()
        pass

    def start_working(self):
        Crate.create_crate()
        self.run_upload()
        pass

    def run_upload(self):
        Upload.tool_selection()
        pass
