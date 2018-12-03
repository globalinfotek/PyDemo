from unittest import TestCase
from unittest.mock import patch

from source.update_service import UpdateService


class TestUpdateService(TestCase):

    def setUp(self):
        self.unit_under_test = UpdateService()

    @patch('source.update_service.requests.post')
    def test_post_update(self, mock_post):
        mock_post.return_value = 'OK'
        result = self.unit_under_test.post_update()
        result.cancel()
        assert mock_post.called
