from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch

class ChartViewTests(TestCase):

    @patch("chart.views.requests.get") # requests.getをモック
    def test_fallback_to_mock_data_on_api_failure(self, mock_get):
        #API呼び出しが失敗したことにする
        mock_get.side_offect = Exception("API down")

        # /chart/ にアクセス
        response = self.client.get(reverse("chart:chart_list"))
        self.assertEqual(response.status_code, 200)

        # モックデータが表示されているかを確認
        self.assertContains(response, "Mock Song 1")
        self.assertContains(response, "Mock Artist A")

