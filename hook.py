import requests
import random

WEBHOOK_URL = 'https://discord.com/api/webhooks/1289891223359983637/zopepLwFhY7Szw63iWQggRzdy4frH9tH6A0SIC9-jEDD5a1aLXXnmV_RCTQ0rLPJezDy'

def send_image():
    # ここで画像を生成するロジックを追加
    IMAGE_URL = 'https://app-content.cyberlink.com/content/AppCMS/2024/05/10/AppCMS/Uploader/13c80fb5-9aa2-444d-9d52-776cecc8cf9f.jpg?product=MyEdit&version=All&versiontype=All&platform=Web&type=TTI_Styles&ext=/13c80fb5-9aa2-444d-9d52-776cecc8cf9f.jpg'  # 生成した画像のURL

    data = {
        'content': 'こちらが生成した画像です！',
        'embeds': [{
            'image': {
                'url': IMAGE_URL
            }
        }]
    }
    requests.post(WEBHOOK_URL, json=data)

# コマンドをチェックする関数を実装することも可能
def check_command(command):
    if command == '!画像生成':
        send_image()

# 例: コマンドを受け取ったと仮定して実行
check_command('!画像生成')
