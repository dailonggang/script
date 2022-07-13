from PIL import Image
import os.path
import glob


def convertpng(pngfile, outdir, width=200, height=200):
    img = Image.open(pngfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        path = os.path.join(outdir, os.path.basename(pngfile))
        print(path)
        new_img.save(os.path.join(outdir, os.path.basename(pngfile)))

    except Exception as e:
        print(e)


for pngfile in glob.glob("D:/Dailycode/images/train/*.png"):
    convertpng(pngfile, "D:/Dailycode/images/test/")