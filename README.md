 # Ideapad3-Keyboard-Auto-Light
 ╔════════════════════════════════════════════════════════════════╗ 
 
 ║     I D E A P A D 3 - K E Y B O A R D - A U T O - L I G H T    ║ 

 ╚════════════════════════════════════════════════════════════════╝ 

by ArcherJR
<h1></h1>

Projenin Hikayesi / Project Overview

TR: IdeaPad 3 serisi laptoplarda varsayılan olarak herhangi bir otomatik klavye aydınlatma mekanizmasına sahip değildir. Bu eksikliği gidermek ve manuel müdahale ihtiyacını ortadan kaldırarak kullanıcı konforunu artırmak adına, doğrudan EC (Embedded Controller) seviyesinde çalışan tamamen otonom bir aydınlatma sistemi geliştirilmiştir.

EN: IdeaPad 3 series laptops do not feature a default automatic keyboard lighting temperature range. To eliminate the need for manual intervention and enhance user comfort, a fully autonomous lighting system operates directly at the EC (Embedded Controller) level.

<h1></h1>

İşletim Sistemi / Operating System: Ubuntu 24.04 (GNOME Desktop) önerilir / (Recommended).

Çekirdek Desteği / Kernel Support: ec_sys modülü yüklü olmalıdır / ec_sys module must be loaded.

Kütüphaneler / Libraries: python3, libnotify-bin (Desktop bildirimleri için / for desktop notifications).

EC Kontrol / EC Control: MSI cihazlar için geliştirilen isw aracı. EC adresi üzerinden veri yazma yeteneği sayesinde Ideapad serisine adapte edilmiştir. / isw utility, originally developed for MSI devices, adapted for Ideapad series via EC address write access.

Yetkilendirme / Authorization: sudo visudo üzerinden NOPASSWD parametresi ile isw komutuna şifresiz erişim yetkisi. / Passwordless access for isw command via NOPASSWD parameter in sudo visudo.

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
