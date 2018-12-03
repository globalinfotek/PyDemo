from unittest import TestCase

from source.application_details import ApplicationDetails


class TestApplicationDetails(TestCase):
    def setUp(self):
        self.details = ApplicationDetails()

    def test_name(self):
        original_name = self.details.name
        self.assertIsNotNone(original_name)

        expected_name = 'other'
        self.details.name = expected_name
        self.assertEqual(expected_name, self.details.name)

    def test_host_name(self):
        original_host = self.details.host_name
        self.assertIsNotNone(original_host)

        expected_host = 'abc-host'
        self.details.host_name = expected_host
        self.assertEqual(expected_host, self.details.host_name)

    def test_version(self):
        original_version = self.details.version
        self.assertIsNotNone(original_version)

        expected_version = '5.0.1'
        self.details.version = expected_version
        self.assertEqual(expected_version, self.details.version)
