
from gpm.interfaces.stack import RulesStack
from gpm.message.centralize import MESSAGE_SWITCHER

NOTIFICATION_RULESTACK = RulesStack()
MESSAGE_SWITCHER.load_stack(NOTIFICATION_RULESTACK)