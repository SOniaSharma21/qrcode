import pyqrcode
from pyqrcode import QRCode
s="www.gopythontutorials.wordpress.com"
url=pyqrcode.create(s)
url.svg("k.svg",scale=10)