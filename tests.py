from django.test import TestCase

from notification.rules.default_notification import DefaultRuleClass
from notification.rules.stack import NOTIFICATION_RULESTACK

class WelcomeNotification(DefaultRuleClass):
    """
        @description: This class is the avatar file rule
    """
    """
    The label of the rule.
    """
    label = 'WELCOME'

    """
    Whether the rule is allowed.
    """
    allow = True

    def __init__(self):
        super(WelcomeNotification, self).__init__()
    
    def check(self, *args, **kwargs):
        return True
    
    def run(self, *args, **kwargs):
        return True

    def error(self, *args, **kwargs):
        return True
    
    def response(self, *args, **kwargs):
        return True
    
    def click(self, *args, **kwargs):
        return True

    def open(self, *args, **kwargs):
        return True

NOTIFICATION_RULESTACK.set_rule(WelcomeNotification())


class NotificationTestCase(TestCase):
    """
    This class represents the notification test case.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        pass

    def test_notification(self):
        """
        Test the notification.
        """
        pass