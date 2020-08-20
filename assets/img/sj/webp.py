
# encoding=utf-8

#  -s 最小要压缩图片大小 （kb)
#  -i 要压缩的图片文件夹目录
#  -q 压缩图片质量  默认80

import os
import sys
import getopt
from PIL import Image

input_file = "" 
outputPath = input_file

def handle_sys_arguments():
    opts, args = getopt.getopt(sys.argv[1:], "i:")
    global output_file
    global input_file

    for op, value in opts:
        print("op:" + op + "__" + value)
        if op == "-i":
            input_file = value

def path_file(path):
    for i in os.listdir(path):
        print(i)
        new_path = os.path.join(path, i)
        if os.path.isfile(new_path):
            transform(new_path)
        else:
            path_file(new_path)

def transform(f):
    split_name = os.path.splitext(f)
    filePath = f

    print(split_name[0])

    if split_name[1] == ".jpg" or split_name[1] == ".png":
        im = Image.open(filePath)
        im.save(split_name[0] + ".webp")
		
def check_args():
    if input_file.strip() == "":
        print("请输入要转换的文件夹路径")
        exit()
		
if __name__ == '__main__':
    handle_sys_arguments()
    check_args()
    path_file(input_file)