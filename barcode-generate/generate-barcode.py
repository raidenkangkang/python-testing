from pystrich.ean13 import EAN13Encoder
encoder = EAN13Encoder("111111111111")
encoder.save("barcode01.png")