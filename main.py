import glob
import PIL
import keras
from keras.preprocessing import image

#リサイズする画像サイズ
input_shape = (256, 256, 3)
#クラス数
num_classes = 2
#画像データ
x = []
#ラベル(1:正例, 0:負例)
y = []
#画像のファイル名
z = []

badPath='./Bad_Thumbnails'  #釣りサムネデータ
goodPath='./Good_Thumbnails' #通常のサムネデータ
image_list_positive = glob.glob(f'{badPath}/image_?.jpg')

for f in image_list_positive:
    x.append(image.img_to_array(image.load_img(f, target_size=input_shape[:2])))
    y.append(1)
    z.append(f)

image_list_negative = glob.glob(f'{goodPath}/image_?.jpg')

for f in image_list_negative:
    x.append(image.img_to_array(image.load_img(f, target_size=input_shape[:2])))
    y.append(0)
    z.append(f)
