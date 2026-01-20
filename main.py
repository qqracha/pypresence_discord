from pypresence import Presence
from pypresence.types import ActivityType # Добавлен импорт типов
import time
import config

if not config.CLIENT_ID:
    raise ValueError("CLIENT_ID not found in .env!")

RPC = Presence(config.CLIENT_ID)
RPC.connect()

def update_status():
    start_time = time.time()
    end_time = start_time + config.TRACK_DURATION
    
    RPC.update(
        activity_type=ActivityType.LISTENING, # Исправлено: activity_type вместо type
        details=config.TRACK_NAME,
        state=config.ALBUM_NAME,
        large_image=config.IMAGE_URL,
        large_text=config.ALBUM_NAME,
        start=int(start_time),
        end=int(end_time),
        buttons=[{"label": "Открыть в Spotify", "url": config.SPOTIFY_URL}]
    )

print("[INFO] Статус запущен. Теперь вы 'слушаете' OST Schedule I.")
update_status()

while True:
    time.sleep(15) # Обновление каждые 15 сек для поддержания соединения
    # Если песня закончилась, перезапускаем таймер
    if time.time() > (time.time() + config.TRACK_DURATION):
        update_status()
