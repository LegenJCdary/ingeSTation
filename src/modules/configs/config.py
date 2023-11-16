from .templates import final
from modules.global_vars import CONFIG_RULES


class MergedConf:
    def __init__():
        self.pre_final = self.create_final_conf()
        self.final = self.validate_conf(self.pre_final)

    def create_final_conf():
        final = {}

        for k, v in final.config.items():
            for x, y in v.items():
                # Repeat until lowest level
                merged_key = f"{parent_key}{sep}{key}" if parent_key else key
                rule = CONFIG_RULES.get(merged_key)
                if rule:
                    mode = rule.get("mode")
                    if mode:
                        order = rule.get(mode)
                        if order:
                            final_value = self.get_final_value(merged_key, mode, order)
                            final[k][x] = final_value
                        else:
                            raise Exception("Order is undefined. Rule mode order needs to be defined for rule mode.")
                    else:
                        raise Exception("Mode is undefined")
                else:
                    raise Exception(f"No rules defined for conf key {merged_key}, update CONFIG_RULES.")

        return final

    def get_final_value(merged_key, mode, order):
        value = self.apply_config_rule(merged_key, mode, order)
        if value is None:
            return DEFAULT_VALUES.get(merged_key)

        return value

    def apply_config_rule(merged_key, mode, order):
        value = None
        if mode == "exclusive":
            value = self.apply_exclusive_rule()
        elif mode == "inclusive":
            value = self.apply_inclusive_rule()
        elif mode == "priority":
            value = self.apply_priority_rule()
        else:
            raise Exception("Unexpected mode found, review CONFIG_RULES")

        return value

    def apply_exclusive_rule():
        """
        1. Check if value is defined in both -> raise Exc
        2. Return value if defined in any
        3. If undefined -> raise Exc
        """
        for conf in order:
            config = getattr(self, conf)
            (...)

    def apply_inclusive_rule():
        """Just merge all of them (remove duplicates)"""

    def apply_priority_rule():
        """
        Cascade/iterate conf by conf using defined order
        If undefined at the end, return None
        """
