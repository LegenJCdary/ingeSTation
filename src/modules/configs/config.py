from templates import final, examples

from src.modules.global_vars import CONFIG_RULES


class MergedConf:
    def __init__(self):
        # self.pre_final = self.create_final_conf()
        # self.final = self.validate_conf(self.pre_final)

        self.merged_conf = {
            "cli": self.merge_conf(examples.cli),
            "application": self.merge_conf(examples.application),
            "project": self.merge_conf(examples.project),
            "operator": self.merge_conf(examples.operator)
        }

    # def create_final_conf(self):
    #     final_conf = {}
    #
    #     for k, v in final.config.items():
    #         for x, y in v.items():
    #             # Repeat until lowest level
    #             merged_key = f"{parent_key}{sep}{key}" if parent_key else key
    #             rule = CONFIG_RULES.get(merged_key)
    #             if rule:
    #                 mode = rule.get("mode")
    #                 if mode:
    #                     order = rule.get(mode)
    #                     if order:
    #                         final_value = self.get_final_value(merged_key, mode, order)
    #                         final[k][x] = final_value
    #                     else:
    #                         raise Exception("Order is undefined. Rule mode order needs to be defined for rule mode.")
    #                 else:
    #                     raise Exception("Mode is undefined")
    #             else:
    #                 raise Exception(f"No rules defined for conf key {merged_key}, update CONFIG_RULES.")
    #
    #     return final_conf
    #
    # def get_final_value(merged_key, mode, order):
    #     value = self.apply_config_rule(merged_key, mode, order)
    #     if value is None:
    #         return DEFAULT_VALUES.get(merged_key)
    #
    #     return value
    #
    # def apply_config_rule(merged_key, mode, order):
    #     value = None
    #     if mode == "exclusive":
    #         value = self.apply_exclusive_rule()
    #     elif mode == "inclusive":
    #         value = self.apply_inclusive_rule()
    #     elif mode == "priority":
    #         value = self.apply_priority_rule()
    #     else:
    #         raise Exception("Unexpected mode found, review CONFIG_RULES")
    #
    #     return value
    #
    # def apply_priority_rule(self, order):
    #     """
    #     Cascade/iterate conf by conf using defined order
    #     If undefined at the end, return None
    #     """
    #     order =
    #     for conf in order:

    def merge_conf(self, dct):
        merged_conf = {}
        for key, value in dct.items():
            if isinstance(value, dict):
                nested = self.merge_conf(value)
                for nested_key, nested_value in nested.items():
                    merged_conf[f"{key}_{nested_key}"] = nested_value
            else:
                merged_conf[key] = value
        return merged_conf

    def apply_exclusive_rule(self, merged_key):
        """
        1. Check if value is defined in both -> raise Exc
        2. Return value if defined in any
        3. If undefined -> raise Exc
        """
        order = CONFIG_RULES.get(merged_key)["exclusive"]

        value1 = self.merged_conf[order[0]].get(merged_key)
        value2 = self.merged_conf[order[1]].get(merged_key)

        if value1 and value2:
            raise Exception(f"{merged_key} is both defined in application and project configs.")
        if not value1 and not value2:
            raise Exception(f"{merged_key} is not defined in either config file.")
        if value1:
            return value1
        if value2:
            return value2

    def apply_inclusive_rule(self, merged_key):
        """Just merge all of them (remove duplicates)"""
        order = CONFIG_RULES.get(merged_key)["inclusive"]
        merged_value = []
        for conf in order:
            value = self.merged_conf[conf].get(merged_key)
            if value:
                merged_value.extend(value)

        return merged_value


if __name__ == '__main__':
    mc = MergedConf()
    print(mc.merged_conf["application"])
    print(mc.merged_conf["project"])

    print(mc.apply_exclusive_rule('containers_sata_device_path'))
    print(mc.apply_inclusive_rule('exclude_devices'))
