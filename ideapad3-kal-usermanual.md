 ╔════════════════════════════════════════════════════════════════╗
 ║    I D E A P A D 3 - K E Y B O A R D - A U T O - L I G H T     ║
 ╚════════════════════════════════════════════════════════════════╝
                        --by ArcherJR--

1. Projenin Kısaca Hikayesi
IdeaPad 3 serisi donanımlar varsayılan olarak herhangi bir otomatik klavye aydınlatma mekanizmasına sahip değildir. Bu eksikliği gidermek ve manuel müdahale ihtiyacını ortadan kaldırarak kullanıcı konforunu artırmak adına, doğrudan EC (Embedded Controller) seviyesinde çalışan tamamen otonom bir aydınlatma sistemi geliştirilmiştir.

Autonomous keyboard backlight controller for Lenovo IdeaPad 3 on Linux. Engineered for EC-level hardware interaction via isw.

2. System Requirements
İşletim Sistemi: Ubuntu 24.04 (GNOME Desktop).(önerilen)
Çekirdek Desteği: ec_sys modülü write_support=1 parametresi ile yüklü olmalıdır.
Kütüphaneler: python3, libnotify-bin (Desktop bildirimleri için).
EC Kontrol: MSI cihazlar için geliştirilen ancak EC adresi üzerinden veri yazma yeteneği sayesinde Ideapad serisine adapte edilen isw aracı.
Yetkilendirme: sudo visudo üzerinden NOPASSWD parametresi ile isw komutuna şifresiz erişim yetkisi.

3. Architectural Scheme
Sistem kendi içerisinde sürekli çalışan bir döngüye sahiptir.
Döngü: Python servisi sistem saatini okur.
Mantık: Belirlenen eşik saatlerine göre isw aracını tetikler.
Geri Bildirim: İşlem başarıyla sonuçlandığında notify-send ile masaüstü bildirimi tetiklenir.

4. Install Guide
git clone https://github.com/ArcherJR/Ideapad3-Keyboard-Auto-Light.git
cd Ideapad3-Keyboard-Auto-Light
sudo cp isw /usr/local/bin/
test for isw:
cd
isw
if you see isw help panel you do this bro congragulations

sudo nano /etc/modprobe.d/ec_sys.conf
add parameters in .conf file :
options ec_sys write_support=1
ctrl + o    enter       ctrl + x 
echo "ec_sys" | sudo tee -a /etc/modules


Yetkilendirme: sudo visudo kullanarak isw aracına NOPASSWD yetkisi tanımlayın.
sudo visudo
add this in visudo:
ALL ALL=(ALL) NOPASSWD: /usr/local/bin/isw
ctrl + o    enter       ctrl + x 

Servis: keyboardAutoLightForIdeapad3.py dosyasını /home/$USER/ dizinine yerleştirin.
sudo mv keyboardAutoLightForIdeapad3.py ~

Autostart: .desktop dosyasını ~/.config/autostart/ dizinine taşıyın ve chmod +x keyboard-light.desktop komutu ile yetkilendirin.
sudo mv keyboard-light.desktop ~/.config/autostart/
chmod +x keyboard-light.desktop

Çalıştırma: Masaüstü oturumu başladığında servis otomatik olarak arka planda çalışmaya başlar.

Credits: This project utilizes isw by YoyPa for EC (Embedded Controller) communication. The isw utility is licensed under GPLv3. https://github.com/YoyPa/isw