import pyqrcode
from pyqrcode import QRCode
s=input("enter a link")
url=pyqrcode.create(s)
url.svg("k.svg",scale=10)