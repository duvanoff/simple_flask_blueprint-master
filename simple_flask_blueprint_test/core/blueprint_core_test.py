import unittest
from simple_flask_blueprint.core.blueprint_core import say_hallo


class SimpleFlaskBlueprintTest(unittest.TestCase):

    def test_say_hallo(self):
        self.assertEquals(say_hallo('Kalimaha'), 'Hallo Kalimaha!')
        self.assertEquals(say_hallo(), 'Hallo!')
