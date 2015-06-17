参考情報
======

**CO2センサ K30 I2Cプログラム計測**

K-30 10,000ppm CO2 Sensor
http://www.co2meter.com/products/k-30-co2-sensor-module

メーカPDF資料
http://co2meters.com/Documentation/AppNotes/AN142-RaspberryPi-K_series.pdf

$ mkdir notsmb
$ cd notsmb
$ wget http://www.byvac.com/downloads/sws/notsmb_1_3.zip
$ unzip notsmb_1_3.zip
$ sudo python setup.py install

**温湿度センサHDC1000 I2C プログラム計測**

秋月電子 HDC100使用 温湿度センサーモジュール
http://akizukidenshi.com/catalog/g/gM-08775/

RaspberryPi + wiringPi-Python + HDC1000 で温湿度を取る（femmnomenaさん）
http://d.hatena.ne.jp/femm/20150426/1430033839

$ sudo apt-get install python-pip
$ sudo pip install wiringpi2

**OLED ディスプレイ 128×64 表示プログラム**

GROVE - I2C OLEDディスプレイ128×64
https://www.switch-science.com/catalog/829/

Seeed-Studio/Grove-RaspberryPi
https://github.com/Seeed-Studio/Grove-RaspberryPi/tree/master/Grove%20-%20OLED%20Display%20128x64

$ git clone https://github.com/Seeed-Studio/Grove-RaspberryPi
$ cd “Grove-RaspberryPi\Grove - OLED Display 128x64”

**照度センサ TSL2561 I2C プログラム計測**

GROVE - I2C デジタル光センサ
https://www.switch-science.com/catalog/1174/

m_shige1979のささやかな抵抗と欲望の日々（id:m_shige1979さん ）
http://m-shige1979.hatenablog.com/entry/2014/06/17/211645

seanbechhofer/raspberrypi
https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code/tree/master/Adafruit_I2C
https://github.com/seanbechhofer/raspberrypi/blob/master/python/TSL2561.py
$ git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code
$ git clone https://github.com/seanbechhofer/raspberrypi
