import requests
import time
from pypresence import Presence
from pypresence.types import ActivityType
import xml.etree.ElementTree as ET

# --- КОНФИГУРАЦИЯ ---
CLIENT_ID = "не чото не хочу" # Ваш ID из .env
VLC_PASSWORD = "не чото не хочу"             # Пароль, который вы ввели в VLC
# ---------------------

RPC = Presence(CLIENT_ID)
RPC.connect()

def get_vlc_data():
    try:
        url = "http://localhost:8080/requests/status.xml"
        r = requests.get(url, auth=('', VLC_PASSWORD), timeout=1)
        root = ET.fromstring(r.text)
        
        # Парсим метаданные
        title = root.find(".//info[@name='title']").text or "Unknown Track"
        artist = root.find(".//info[@name='artist']").text or "Unknown Artist"
        state = root.find("state").text  # playing, paused, stopped
        current_time = int(root.find("time").text)
        total_time = int(root.find("length").text)
        
        return {"title": title, "artist": artist, "state": state, "cur": current_time, "total": total_time}
    except:
        return None

print("[INFO] Мост запущен. Слушаю VLC...")

while True:
    data = get_vlc_data()
    
    if data and data['state'] == 'playing':
        # Вычисляем время для прогресс-бара
        start_ts = time.time() - data['cur']
        end_ts = start_ts + data['total']
        
        RPC.update(
            activity_type=ActivityType.LISTENING,
            details=data['title'],
            state=f"от {data['artist']}",
            start=int(start_ts),
            end=int(end_ts),
            large_image="vlc", # Загрузите лого в Discord Developer Portal
            small_image="play"
        )
    else:
        RPC.clear()
        
    time.sleep(5) # Проверка каждые 5 секунд
