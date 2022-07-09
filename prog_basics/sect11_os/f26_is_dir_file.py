# 파일인지 디렉터리인지 확인하기(os.pathisfile, os.pathisdir)
import os
from os.path import exists, isdir, isfile

# files = os.listdir('..')
files = os.listdir()
# print('files :', files)

for file in files:
    if isdir(file):
        print('<DIR> %s' %file)

for file in files:
    if isfile(file):
        print('FILE : %s' %file)