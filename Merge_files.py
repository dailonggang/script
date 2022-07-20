import os

# 原文件夹
ori_file = "C:/Users/dlg/Desktop/nnn/train"
# 目标合并文件夹
tar_file = "C:/Users/dlg/Desktop/train"
# 得到文件夹下的所有文件名称
files = os.listdir(ori_file)

index = 0
while index < 1:  # 1为原文件夹下文件数量
    ori_txt = os.path.join(ori_file, files[index])
    tar_txt = os.path.join(tar_file, files[index])
    f = open(ori_txt, 'r').read()  # 将打开的文件内容保存到变量f
    log = open(tar_txt, 'a+')  # 以追加模式打开文件
    log.write(f)                     # 写入文件
    print('已经合并：' + files[index])
    index += 1
