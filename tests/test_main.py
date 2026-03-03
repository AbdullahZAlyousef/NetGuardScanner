import unittest
from src.service_mapper import ServiceMapper
from src.report_generator import ReportGenerator
from src.main import is_valid_ip
import os
import json


class TestNetGuardScanner(unittest.TestCase):

    def test_valid_ip(self):
        """Test valid IP address"""
        self.assertTrue(is_valid_ip("127.0.0.1"))

    def test_invalid_ip(self):
        """Test invalid IP address"""
        self.assertFalse(is_valid_ip("abc"))

    def test_service_risk_mapping(self):
        """Test known service risk mapping"""
        mapper = ServiceMapper()
        result = mapper.evaluate_service("microsoft-ds")
        self.assertEqual(result["risk"], "High")

    def test_json_report_creation(self):
        """Test JSON file creation"""
        reporter = ReportGenerator(output_directory="output/sample_output")
        sample_data = {"127.0.0.1": []}
        reporter.save_to_json(sample_data, filename="test_output.json")

        self.assertTrue(os.path.exists("output/sample_output/test_output.json"))

        # Cleanup test file
        os.remove("output/sample_output/test_output.json")


if __name__ == "__main__":
    unittest.main()