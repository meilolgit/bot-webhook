import requests

WEBHOOK_URL = 'https://discord.com/api/webhooks/1289891223359983637/zopepLwFhY7Szw63iWQggRzdy4frH9tH6A0SIC9-jEDD5a1aLXXnmV_RCTQ0rLPJezDy'
IMAGE_URL = 'https://example.com/generated_image.jpg'  # 画像生成サービスのURL

def send_image():
    data = {
        'content': 'こちらが生成した画像です！',
        'embeds': [{
            'image': {
                'url': IMAGE_URL
            }
        }]
    }
    requests.post(WEBHOOK_URL, json=data)

send_image()
