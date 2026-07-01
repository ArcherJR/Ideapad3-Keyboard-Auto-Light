#!/usr/bin/env python3

# Using isw (https://github.com/YoyPa/isw)
# EC communication logic powered by isw (GPLv3)
#                   _                   _ _____  
#    /\            | |                 | |  __ \ 
#   /  \   _ __ ___| |__   ___ _ __    | | |__) |
#  / /\ \ | '__/ __| '_ \ / _ \ '__|   | |  _  / 
# / ____ \| | | (__| | | |  __/ | | |__| | | \ \ 
#/_/    \_\_|  \___|_| |_|\___|_|  \____/|_|  \_\
                                                

import subprocess
import time
from datetime import datetime

# Kullanıcıyı kısıtlamamak için durum kilitleri (Flag)
is_day_mode_set = False
is_night_mode_set = False

def send_notification(title, message):
    """Ubuntu masaüstüne şık bir sistem bildirimi gönderir."""
    try:
        # Bildirimin ekranda düzgün görünmesi için ikon ve süre parametreleri ekledik
        subprocess.run([
            "notify-send", 
            "-i", "input-keyboard", 
            title, 
            message
        ], check=True)
    except Exception:
        pass  # Arka planda hata oluşursa sistemi kilitleme, sessizce geç

# Kodun sürekli döngüde çalışmasını sağlar
while True:
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    
    # Mantık: 06:00 ile 17:30 arası GÜNDÜZ, geri kalan her an GECE
    is_day = (current_hour > 6 or (current_hour == 6 and current_minute >= 0)) and \
             (current_hour < 17 or (current_hour == 17 and current_minute < 30))
    
    # 1. SENARYO: Gündüz modu (06:00 - 17:30) -> Işıkları Kapat
    if is_day and not is_day_mode_set:
        try:
            subprocess.run(["sudo", "isw", "-s", "0x26", "1"], check=True)
            subprocess.run(["sudo", "isw", "-s", "0x8A", "210"], check=True)
            subprocess.run(["sudo", "isw", "-s", "0x8A", "214"], check=True)
            
            is_day_mode_set = True
            is_night_mode_set = False
            
            # Ekran bildirimi fırlatıyoruz
            send_notification("Klavye Otomasyonu", "Gündüz modu aktif: Klavye ışıkları kapatıldı.")
        except Exception:
            pass

    # 2. SENARYO: Gece modu (17:30 sonrası ve 06:00 öncesi) -> Işıkları Aç
    elif not is_day and not is_night_mode_set:
        try:
            subprocess.run(["sudo", "isw", "-s", "0x26", "3"], check=True)
            subprocess.run(["sudo", "isw", "-s", "0x8A", "215"], check=True)
            subprocess.run(["sudo", "isw", "-s", "0x8A", "211"], check=True)
            
            is_night_mode_set = True
            is_day_mode_set = False
            
            # Ekran bildirimi fırlatıyoruz
            send_notification("Klavye Otomasyonu", "Gece modu aktif: Klavye ışıkları açıldı.")
        except Exception:
            pass

    # İşlemciyi yormamak için 90 saniye uyu (varsayılan 30 performansı etkilemesin diye arttırıldı)
    time.sleep(90)
