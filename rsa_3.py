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
key=RSA.importKey(open('public.pem').read())
cipher=PKCS1_v1_5.new(key)
ciphertext=cipher.encrypt(open('Sing.mp3','rb').read())
with open('encrypted.mp3','wb') as f:
    f.write(ciphertext)


#with open('encrypted.mp3','wb') as f:
#    f.write(rsa.publickey().encrypt(open('Sing.mp3','rb').read(),random_func)[0])

#秘密鍵による復号
with open('encrypted.mp3','rb') as f:
    with open('decryted.mp3','wb') as fz:
        fz.write(RSA.importKey(private_pem,'hogehoge').decrypt(f.read()))



