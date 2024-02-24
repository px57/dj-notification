
from kernel.interfaces.stack import RulesStack
from kernel.message.centralize import MESSAGE_SWITCHER

NOTIFICATION_RULESTACK = RulesStack()
MESSAGE_SWITCHER.load_stack(NOTIFICATION_RULESTACK)