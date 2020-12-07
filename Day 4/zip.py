from pathlib import Path
from zipfile import ZipFile
#rglob is recursive, glob only specified directory


zipper = ZipFile('D:\\Python\\dat 2 assign','w')
path = Path()
for p in path.rglob("*.py"):
    zipper.write(p)
zipper.close()

with ZipFile('D:\\Python\\dat 2 assign') as zp:
    print(zp.namelist())
    info = zp.getinfo('pyramid.py')
    print(f'{info.file_size}-->{info.compress_size}')
    zp.extractall('test/')