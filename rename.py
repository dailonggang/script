import os


class BatchRename():
    '''
    批量重命名文件夹中的文件
    '''

    def __init__(self):
        self.path = 'D:/Dailycode/images/train/'  # 表示需要命名处理的文件夹
        self.save_path = 'D:/Dailycode/images/test/'  # 保存重命名后的图片地址

    def rename(self):
        filelist = os.listdir(self.path)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（个数）
        i = 1  # 表示文件的命名是从1开始的
        for item in filelist:
            # endswith()判断是否以指定后缀结尾,初始的图片的格式为jpg格式的
            if item.endswith('.txt'):
                # 当前文件中图片的地址
                src = os.path.join(os.path.abspath(self.path), item)
                # 处理后文件的地址和名称,可以自己按照自己的要求改进
                dst = os.path.join(os.path.abspath(self.save_path), '' + str(i) + '.txt')
                # 异常处理,如果try正常运行，跳过except
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print('total %d to rename & converted %d jpgs' % (total_num, i))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
