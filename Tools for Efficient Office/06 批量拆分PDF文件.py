# -*- coding: UTF-8 -*-
"""
@author: YaoLei
@file: 05 批量提取PDF文件封面.py
@time: 2019/10/15 8:53 下午
"""
import os

from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter


def split_pdf(infile):
    """
    :param infile: 待拆分的PDF文件
    :return: 无
    """
    path = os.getcwd()
    file_name = os.path.splitext(infile)[0]
    file_ext = os.path.splitext(infile)[1]
    # print('文件名、扩展名', file_name, file_ext)
    out_path = os.path.join(path, 'PDF拆页')
    # print(out_path)
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    with open(infile, 'rb') as infile:
        reader = PdfFileReader(infile)
        number_of_pages = reader.getNumPages()  # 计算此PDF文件中的页数
        for i in range(number_of_pages):
            writer = PdfFileWriter()
            writer.addPage(reader.getPage(i))
            out_file_name = out_path + '/' + file_name + '_' + str(i + 1) + '.pdf'
            with open(out_file_name, 'wb') as outfile:
                writer.write(outfile)
    print('PDF拆分完成！')


def batch_split_file():
    """
    批量拆分当前文件夹内PDF文件
    :return:
    """
    try:
        for root, dirs, files in os.walk(os.getcwd()):
            # print('root', root)
            # print('dirs', dirs)
            # print('files', files)
            for file in files:
                if os.path.splitext(file)[1] == '.pdf':
                    split_pdf(file)
                    print(file + ' 拆分完成')
    except Exception as e:
        print('错误', e)


if __name__ == '__main__':
    in_file = r'example.pdf'
    out_path = './PDF拆页/'
    # split_pdf(in_file)
    batch_split_file()
