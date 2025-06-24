#Side project
import sys
import requests
from bs4 import BeautifulSoup
import whisper
!{sys.executable} -m pip install beautifulsoup4 requests
model = whisper.load_model("base")
result = model.transcribe(r"C:\Users\sarve\Downloads\Shape of You.mp3")
lyrics = result["text"]
print("Transcribed Lyrics:", lyrics)
def search_google_for_song(lyrics):
    query = f"{lyrics.strip()} song"
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error during requests to Google: {e}")
        return ""
html = search_google_for_song(lyrics)
soup = BeautifulSoup(html, "html.parser")
result_block = soup.find_all('div', class_='BNeawe iBp4i AP7Wnd')

if result_block:
    for result in result_block:
        print(result.get_text())
else:
    print("Song not found.")
