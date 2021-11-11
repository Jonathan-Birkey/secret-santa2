from click.testing import CliRunner
import unittest
from secretsanta import secretsanta


class MyTestCase(unittest.TestCase):
    def test_something(self):
        runner = CliRunner()
        result = runner.invoke(secretsanta)
        self.assertTrue(result.exit_code == 0)
        print(result.output)
        self.assertTrue(result.output == "Hello")


if __name__ == '__main__':
    unittest.main()
