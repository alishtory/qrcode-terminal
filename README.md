# Python QRCode Terminal
You can draw QR codes in your terminal by Python:
![Py QrCode][cmdqrcode-example-img]

## Install Dependencies
You need install these:
```shell    
    yum install -y python-devel zlib-devel libjpeg-turbo-devel
    pip install pillow qrcode
```

## Install
Can be installed with pip:
``` shell
    pip install qrcode_terminal
```

## Useage

### As Library
```python
    import qrcode_terminal
    qrcode_terminal.draw('http://www.baidu.com')
```
![Py QrCode][pyqrcode-example-img]

### In Terminal
``` shell
    qrcode-terminal-py -d http://www.baidu.com
```
![Py QrCode][cmdqrcode-example-img]

[pyqrcode-example-img]:https://raw.githubusercontent.com/alishtory/qrcode-terminal/master/example/pyqrcode.jpg
[cmdqrcode-example-img]:https://raw.githubusercontent.com/alishtory/qrcode-terminal/master/example/cmdqrcode.jpg


