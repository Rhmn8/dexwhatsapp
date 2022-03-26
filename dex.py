from pyaxmlparser import APK
import sys
import base64
import zipfile
import hashlib

if len(sys.argv) < 2:
    print("How to use: python dexmd5.py <whatsapp.apk>")
    exit()
else:
    apkFile = sys.argv[1]
    apk = APK(apkFile)
try:
    zipFile = zipfile.ZipFile(apkFile,'r')
    classesDexFile = zipFile.read('classes.dex')
    hash = hashlib.md5()
    hash.update(classesDexFile)

    print("Version: " + apk.version_name)
    print("ClassesDex: " + base64.b64encode(hash.digest()).decode("utf-8"));
except Exception as e:
    print(sys.argv[1] + " Not found.")