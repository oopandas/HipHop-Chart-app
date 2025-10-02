from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
import requests

class ChartViewTests(TestCase):
    @patch("chart.views.requests.get") # requests.getをモック
    # test_fallback_to_mock_data_on_api_failure
    def test_whether_mock_data_is_displayed_when_the_api_fails(self, mock_get):
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
    
    def test_to_see_if_data_bs_dark_theme_is_included_in_html(self):
        # ページを取得
        response = self.client.get(reverse("chart:chart_list"))
        # htmlを文字列化
        html = response.content.decode()
        # 指定の文字列が含まれているか確認
        self.assertIn('data-bs-theme="dark"', html)

    def test_whether_the_link_tag_contains_the_Bootstrap_CDN(self):
        # ページ取得
        response = self.client.get(reverse("chart:chart_list"))
        # htmlを文字列化
        html = response.content.decode()
        # linkタグにCDNが読み込まれているか
        self.assertIn(
            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css",
            html
        )

    def test_whether_the_script_tag_contains_the_Bootstrap_CDN(self):
        # ページ取得
        response = self.client.get(reverse("chart:chart_list"))
        # htmlを文字列化
        html = response.content.decode()
        # スクリプトタグにCDNが読み込まれているか
        self.assertIn(
            "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js",
            html
        )



