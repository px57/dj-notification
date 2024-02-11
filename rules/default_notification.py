

from django.utils import timezone
import os
from notification.rules.stack import NOTIFICATION_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager
import PIL

class DefaultRuleClass(InterfaceManager):
    """
        @description: The default rule class. 
    """
    pass

NOTIFICATION_RULESTACK.set_rule(DefaultRuleClass())