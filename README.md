# android-to-pc-bluetooth-communication
***Öncelikle kodlar windows içindir.***
___

***Gereklilikler***

Pyserial kütüphanesini bilgisayarınıza kurmalısınız. ```pip install pyserial``` 

Hazırlamış olduğum bluetooth verisi gönderip alabilen PcKontrolWin.apk apksını android cihazınıza kurmalısınız.
___

***Kodun çalıştırılması***

Öncelikle bilgisayarla telefonu bluetooth üzerinden eşleştiriyoruz.

Sonra serial_port.py ismindeki python kodunu komut isteminden yada herhangi bir derleyiciden çalıştırıyoruz. Ardından uygulama üzerinden bağlantı seçinize tıklıyoruz burada daha önceden eşleştirilen cihazlar mac adresleriyle beraber çıkacaklar pc'mizin bulunduğu bluetooth bağlantımızı seçiyoruz.

![image](https://user-images.githubusercontent.com/99413396/167316293-375a7ba6-f235-4028-8de6-34c4a506c11b.png)
![image](https://user-images.githubusercontent.com/99413396/167316359-3df6c470-2b74-45eb-86a1-c80e3af9b966.png)
Bunları yaptıktan sonra bağlantı başarılı... yazısı çıkmalıdır. Ardından istediğiniz komutu gönderebilirsiniz fakat benim bilgisayarımda kodlar bir harfi eksik gidiyor. Mesela scriptoff kelimesini gönderiyorum [b'criptoff'] şeklinde gidiyor kodda düzenleme yaparken buna dikkat ederseniz işiniz kolaylaşacaktır.

***Önemli nokta bağlantı seçmeden önce python dosyasını çalıştırmalısınız!!! Yoksa hata verecektir.***

bu haliyle kod düzgün çalışacaktır ama bu python kodunu exe gibi çalıştırmak isterseniz pyinstaller yükleyerek yapabilirsiniz 
```
pip install pyinstaller
python -m PyInstaller <dosyanızın konumu>
```

örnek: 
```
python -m PyInstaller .\Desktop\serial_port.py
```

pyinstaller sizin yerinize python kodunu windows uygulamasına dönüştürecektir kodu yazdıktan sonra oluşan dist klasörünün içinde uygulamayı bulabilirsiniz
