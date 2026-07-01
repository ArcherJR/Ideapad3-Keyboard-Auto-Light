# Ideapad3-Keyboard-Auto-Light
╔════════════════════════════════════════════════════════════════╗ 
║     I D E A P A D 3 - K E Y B O A R D - A U T O - L I G H T    ║ 
╚════════════════════════════════════════════════════════════════╝ 
                      --by ArcherJR--
<h1></h1>
Projenin Kısaca Hikayesi:

IdeaPad 3 serisi donanımlar varsayılan olarak herhangi bir otomatik klavye aydınlatma mekanizmasına sahip değildir. Bu eksikliği gidermek ve manuel müdahale ihtiyacını ortadan kaldırarak kullanıcı konforunu artırmak adına, doğrudan EC (Embedded Controller) seviyesinde çalışan tamamen otonom bir aydınlatma sistemi geliştirilmiştir.
Autonomous keyboard backlight controller for Lenovo IdeaPad 3 on Linux. Engineered for EC-level hardware interaction via isw.
<h1></h1>
System Requirements İşletim Sistemi:

Ubuntu 24.04 (GNOME Desktop).(önerilen) Çekirdek Desteği: ec_sys modülü write_support=1 parametresi ile yüklü olmalıdır. Kütüphaneler: python3, libnotify-bin (Desktop bildirimleri için). EC Kontrol: MSI cihazlar için geliştirilen ancak EC adresi üzerinden veri yazma yeteneği sayesinde Ideapad serisine adapte edilen isw aracı. Yetkilendirme: sudo visudo üzerinden NOPASSWD parametresi ile isw komutuna şifresiz erişim yetkisi.
<h1></h1>
Architectural Scheme: 

Sistem kendi içerisinde sürekli çalışan bir döngüye sahiptir. Döngü: Python servisi sistem saatini okur. Mantık: Belirlenen eşik saatlerine göre isw aracını tetikler. Geri Bildirim: İşlem başarıyla sonuçlandığında notify-send ile masaüstü bildirimi tetiklenir.
<h1></h1>
Install Guide:

```bash
git clone https://github.com/ArcherJR/Ideapad3-Keyboard-Auto-Light.git
```

```bash
cd Ideapad3-Keyboard-Auto-Light
```

```bash
sudo cp isw /usr/local/bin/
```

```bash
sudo chmod +x /usr/local/bin/isw
```

```bash
sudo cp isw.conf /etc/
```

test: isw -h

```bash
sudo nano /etc/modules
```

<h1></h1>

add to the bottom of the file
```bash
ec_sys 
```

```bash
sudo visudo
```
<h1></h1>
add to the bottom of the file:

```bash
ALL ALL=(ALL) NOPASSWD: /usr/local/bin/isw
```

```bash
cp keyboardAutoLightForIdeapad3.py ~
```

```bash
cp keyboard-light.desktop ~/.config/autostart/
```

```bash
chmod +x ~/.config/autostart/keyboard-light.desktop
```

```bash
sudo nano /etc/modprobe.d/isw-ec_sys.conf
```

```bash
options ec_sys write_support=1
```

```bash
sudo reboot
```

test: cat /sys/module/ec_sys/parameters/write_support

if you see Y you do this

you can delete Ideapad3-Keyboard-Auto-Light folder
<h1></h1>
Credits: This project utilizes isw by YoyPa for EC (Embedded Controller) communication. The isw utility is licensed under GPLv3. https://github.com/YoyPa/isw
