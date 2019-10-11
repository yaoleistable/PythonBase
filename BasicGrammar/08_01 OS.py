import os

# list =['source activate learn','conda list']
libs = {'django', 'pandas', 'pypdf2'}
try:
    for lib in libs:
        os.system('pip install' + lib)
    print('安装成功')
except:
    print('安装失败')
