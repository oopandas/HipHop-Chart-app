from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
import requests

class ChartViewTests(TestCase):
    @patch("chart.views.requests.get") # requests.getをモック
    def test_fallback_to_mock_data_on_api_failure(self, mock_get):
        #API呼び出しが失敗したことにする
        mock_get.side_effect = requests.RequestException("API down")

        # /chart/ にアクセス
        response = self.client.get(reverse("chart:chart_list"))
        # self.assertEqual(response.status_code, 200)
        print("response.context:", response.content) # デバック
        print(response.content.decode())             # デバック
        # モックデータが表示されているかを確認
        self.assertContains(response, "Mock Song 1")
        self.assertContains(response, "Mock Artist A")

    @patch("chart.views.requests.get") # requests.getをモック
    def test_normal_api_response(self, mock_get):
        #APIが正常に返る場合
        mock_get.return_value.json.return_value = {
            "tracks": {
                "track": [
                    {"name": "Real Song 1", "artist": {"name": "Real Artist 1"}},
                    {"name": "Real Song 2", "artist": {"name": "Real Artist 2"}},
                ]
            }
        }
        response = self.client.get(reverse("chart:chart_list"))
        self.assertContains(response, "Real Song 1")
        self.assertContains(response, "Real Artist 1")

    @patch("chart.views.requests.get") # requests.getをモック
    def test_empty_chart(self, mock_get):
        #空データの場合
        mock_get.return_value.json.return_value = {
            "tracks": {"track": []}
        }
        response = self.client.get(reverse("chart:chart_list"))
        self.assertContains(response, "チャートデータを取得できませんでした。")


