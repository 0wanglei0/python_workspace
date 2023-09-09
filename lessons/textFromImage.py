# 导入依赖库
from PIL import Image
import pytesseract

# # 读取图片
# img = cv2.imread('chinese.jpg')
#
#
# # 配置pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# # 识别图片中的文字
# text = pytesseract.image_to_string(img, lang='chi_sim')
#
# # 输出识别结果
# print(text)


def read_image(name):
    print(pytesseract.image_to_string(Image.open(name), lang='chi_sim'))
def main():
    read_image('1657158527412.jpg')