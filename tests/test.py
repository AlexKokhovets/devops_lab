from unittest import TestCase
from handlers import pulls


class MyTestCase(TestCase):
    def setUp(self):
        """Init"""

    def test_pull_requests_by_state(self):
        """Test for is pulls requesting by state"""
        self.assertEqual(pulls.get_pulls_by_state('all').status_code, 200)
        self.assertEqual(pulls.get_pulls_by_state('open').status_code, 200)
        self.assertEqual(pulls.get_pulls_by_state('closed').status_code, 200)

    def test_pull_requests_by_label(self):
        """Test for is pulls requesting by state"""
        self.assertEqual(pulls.get_pulls_by_label('needs work').status_code, 200)
        self.assertEqual(pulls.get_pulls_by_label('accepted').status_code, 200)

    def test_json_parsing(self):
        self.assertEqual(pulls.parse_pulls_from_json([{"title": 1, "number": 2, "html_url": 3}]),
                         [{"title": 1, "num": 2, "link": 3}])

    def test_filtering(self):
        self.assertNotEqual(len(pulls.get_pulls('all')), 0)
        self.assertNotEqual(len(pulls.get_pulls('closed')), 0)
        self.assertNotEqual(len(pulls.get_pulls('open')), 0)
        self.assertNotEqual(len(pulls.get_pulls('accepted')), 0)
        self.assertNotEqual(len(pulls.get_pulls('needs work')), 0)

    def tearDown(self):
        """Finish"""
