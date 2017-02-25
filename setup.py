#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@author: ‘wang_pc‘
@site: 
@software: PyCharm
@file: setup.py
@time: 2017/2/10 16:18
'''
from setuptools import setup

setup(
    name='qrcode_terminal',
    version='0.6',
    license='MIT',
    author_email='840652591@qq.com',
    url='https://github.com/alishtory/qrcode_terminal',
    description='Python QRCode Terminal',
    platforms=['any'],
    py_modules= ['qrcode_terminal'],
    packages= ['qrcode_terminal'],
    entry_points={
        'console_scripts': [
            'qrcode-terminal-py= qrcode_terminal.qrcode_terminal:draw_cmd',
        ],
    },
    install_requires=['Pillow', 'qrcode'],
    include_package_data=True,
)
