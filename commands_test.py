import unittest
import commands as cmd
class TestCommands(unittest.TestCase):
    
    def test_get_stats(self):
        self.assertNotEqual(cmd.get_stats(), None)

if __name__ == '__main__':
    unittest.main(exit=False)