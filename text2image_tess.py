import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
import cv2
import matplotlib.pyplot as plt

def get_bounds(img):
    print('Getting bounds....')
    print("Type of img",type(img))
    image = cv2.imread(img, cv2.IMREAD_COLOR)
    # print("Type of image", type(image))
    text = pytesseract.image_to_string(image)
    return text

def get_boxes(img):
    print('Getting boxes....')
    img2 = cv2.imread(img, cv2.IMREAD_COLOR)
    print("Type of img", type(img2))
    data = pytesseract.image_to_data(img2, output_type=pytesseract.Output.DICT)
    n_boxes = len(data['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # cv2.imshow("image",img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return img2

#print(get_bounds(r"C:\Users\Shaily Desai\Downloads\temp_image3.jpeg"))
#print(get_boxes(r"C:\Users\Shaily Desai\Downloads\temp_image3.jpeg"))