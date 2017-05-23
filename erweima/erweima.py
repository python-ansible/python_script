import qrcode

url = 'https://github.com/python-ansible'
img = qrcode.make(url)

with open('1.png', 'wb') as f:
    img.save(f)
