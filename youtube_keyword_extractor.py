import requests
from bs4 import BeautifulSoup

def get_video_keywords(video_id):
    url = f"https://www.youtube.com/watch?v={video_id}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    keywords = [meta["content"] for meta in soup.find_all("meta") if meta.has_attr("name") and meta.get("name") == "keywords"]
    return keywords[0].split(", ")

video_id = "_lRvVmYps8g"
keywords = get_video_keywords(video_id)
print(keywords)
