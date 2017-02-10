# Python QRCode Terminal
You can draw QR codes in your terminal by Python:

## Install Dependencies
You need install these:
    yum install -y python-devel zlib-devel libjpeg-turbo-devel
    pip install pillow qrcode

## Install
Can be installed with pip:
    pip install qrcode_terminal

## Useage

### As Library
    import qrcode_terminal
    qrcode_terminal.draw('http://www.baidu.com')
![Py QrCode][pyqrcode-example-img]

### In Terminal
    qrcode-terminal-py -d http://www.baidu.com
![Py QrCode][cmdqrcode-example-img]



