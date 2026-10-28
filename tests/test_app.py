
import unittest
from app import get_pipeline_status


class TestPipelineStatus(unittest.TestCase):

    def test_success(self):
        self.assertEqual(
            get_pipeline_status(True), "SUCCESS"
        )

    def test_failure(self):
        self.assertEqual(
            get_pipeline_status(False), "FAILURE"
        )


if __name__ == "__main__":
    unittest.main()
