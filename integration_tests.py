import unittest
from agn_module import AGNModule

class TestAGNModule(unittest.TestCase):
    def test_model_forward(self):
        model = AGNModule()
        x = torch.randn(1, 3, 224, 224)
        output = model(x)
        self.assertIsNotNone(output)

if __name__ == "__main__":
    unittest.main()