import requests
import os
from datetime import datetime

NOTION_TOKEN = os.getenv('NOTION_TOKEN') 
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def log_to_notion(author, description, zip_name):
    data = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {
            "작성자": {"title": [{"text": {"content": author}}]},
            "설명": {"rich_text": [{"text": {"content": description}}]},
            "zip 이름": {"rich_text": [{"text": {"content": zip_name}}]},
            "날짜": {"date": {"start": datetime.now().isoformat()}}
        }
    }

    response = requests.post(
        "https://api.notion.com/v1/pages",
        headers=headers,
        json=data
    )

    if response.status_code == 200 or response.status_code == 201:
        print("✅ Notion 기록 성공")
    else:
        print("❌ Notion 기록 실패:", response.text)
