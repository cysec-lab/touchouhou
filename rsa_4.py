#coding=utf-8
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random

random_func = Random.new().read
rsa = RSA.generate(2048,random_func)

#秘密鍵作成
private_pem = rsa.exportKey(format='PEM',passphrase='hogehoge')
with open('private.pem','wb') as f:
    f.write(private_pem)

#公開鍵作成
public_pem = rsa.publickey().exportKey()
with open('public.pem','wb') as f:
    f.write(public_pem)


#公開鍵による暗号化
key1=RSA.importKey(open('public.pem').read())
cipher1=PKCS1_v1_5.new(key1)

fin1=open('sample.jpg','rb')
bdata1 = fin1.read()
size1 = len(bdata1)
offset = 0
chunk = 245
ciphertext = open('encrypted.jpg','ab')
while True:
    if offset > size1:
        break
    ciphertext.write(cipher1.encrypt(bdata1[offset:offset+chunk]))
    offset += chunk



#ciphertext=cipher.encrypt(open('Sing.mp3','rb').read())
#with open('encrypted.mp3','wb') as f:
#   f.write(ciphertext)


#with open('encrypted.mp3','wb') as f:
#    f.write(rsa.publickey().encrypt(open('Sing.mp3','rb').read(),random_func)[0])

#秘密鍵による復号
key2=RSA.importKey(open('private.pem').read(),'hogehoge')
cipher2=PKCS1_v1_5.new(key2)

fin2=open('encrypted.jpg','rb')
bdata2 = fin2.read()
size2 = len(bdata2)


sentinel1=Random.new().read(245)
sentinel2=Random.new().read(size1%245)


offset = 0
chunk = 256
plaintext = open('decrypted.jpg','ab')
while True:
    if offset > size2-512:
        break
    plaintext.write(cipher2.decrypt(bdata2[offset:offset+chunk],sentinel1))
    offset += chunk

plaintext.write(cipher2.decrypt(bdata2[-256:],sentinel2))

fin1.close()
ciphertext.close()

fin2.close()
plaintext.close()


#with open('encrypted.mp3','rb') as f:
#    with open('decryted.mp3','wb') as fz:
#        fz.write(RSA.importKey(private_pem,'hogehoge').decrypt(f.read()))



