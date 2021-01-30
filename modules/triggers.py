class BaseTrigger(object):
    __trigger_name__ = "Base trigger class"
    __trigger_number__ = 0
    __takes_input__ = True
    __input_name__ = None

    def get_trigger(self, payload, triggering_entity):
        return None


class ExecuteOnKeyPress(BaseTrigger):

    __trigger_name__ = "Execute logic bomb on key press"
    __trigger_number__ = 1
    __takes_input__ = True
    __input_name__ = "key name"

    def get_trigger(self, payload, triggering_entity):
        logic = f"{triggering_entity}"
        return logic


class ExecuteOnCertainTime(BaseTrigger):

    __trigger_name__ = "Execute logic bomb on certain time"
    __trigger_number__ = 2
    __takes_input__ = True
    __input_name__ = "time"

    def get_trigger(self, payload, triggering_entity):
        logic = f"{triggering_entity}"
        return logic


class ExecuteOnCertainDate(BaseTrigger):

    __trigger_name__ = "Execute logic bomb on certain Date"
    __trigger_number__ = 3
    __takes_input__ = True
    __input_name__ = "date"

    def get_trigger(self, payload, triggering_entity):
        logic = f"{triggering_entity}"
        return logic
