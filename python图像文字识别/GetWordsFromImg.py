# -*- coding :utf-8 -*-
#Author :刘悦
#前提是安装识别引擎tesseract-ocr，是一个软件
#和pytesseract，pip install pytesseract，可以命令安装
from PIL import Image
import pytesseract
#上面都是导包，只需要下面这一行就能实现图片文字识别
text=pytesseract.image_to_string(Image.open(r'456.png'),lang='chi_sim')
print(text)

