from click.testing import CliRunner
import unittest
from secretsanta import secretsanta


class MyTestCase(unittest.TestCase):
    def test_secretsanta(self):
        runner = CliRunner()
        result = runner.invoke(secretsanta)
        self.assertTrue(result.exit_code == 0)


if __name__ == '__main__':
    unittest.main()
