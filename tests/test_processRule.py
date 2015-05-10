from unittest import TestCase
from rule_worker_app import process_rule


class TestProcessRule(TestCase):
    def setUp(self):
        self.auth_token = ""

    def test_process_rule(self):
        worker = process_rule.ProcessRule()
        auth_token = ""

        worker.process_rule()


    def test_move_to_trash(self):
        from_address = "cow@chick.com"
        age = 7
        worker = process_rule.ProcessRule.move_to_trash(self.auth_token, from_address, age)