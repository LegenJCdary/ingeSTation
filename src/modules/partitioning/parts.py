import os


class DataPartitioning:

    def __init__(self, logger, config, mount_list):
        self.logger = logger
        self.config = config
        self.mount_list = mount_list
        self.list_container_files()
        #self.calculate_box_size()
        self.repackage_to_boxes()

    def list_container_files(self):
        for k, v in self.mount_list.items():
            v["files"] = []
            for root, subs, files in os.walk(v["mount_path"]):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        v["files"].append((file_path, os.stat(file_path).st_size))
                    except Exception as exc:
                        raise exc

    """
    Things to consider:
    1. Filesystem type.
    2. Transfer protocol.
    3. Network card.
    4. Routing, vlan.
    5. (SATA) controller.
    6. Disk type (hw, fs).
    7. Disk count.
    8. File sizes.
    9. Input structure.
    10. Used tool (other than rsync?)
    """
    def calculate_box_size(self):
        pass

    def repackage_to_boxes(self):
        for k, v in self.mount_list:
            v["crates"] = []
            for file, _ in v["files"]:
                root, name = os.path.split(file)
                try:
                    v["crates"][root].append(name)
                except KeyError:
                    v["crates"][root] = []
