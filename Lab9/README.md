# Importy
```python
import imutils
import cv2
import argparse
import numpy as np
```
# Wczytanie oraz wyświetlenie obrazu
```python
image = cv2.imread("harold_picture.jpg")
(h, w, d ) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
```
# Zapisywanie obrazu
```python
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("images/image1.jpg",image)
```
![Image](images/image1.jpg)

# Dostęp do poszczególnych pikseli
```python
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))
```
# Przycinanie zdjęcia
```python
roi = image[100:250, 300:460]
cv2.imwrite("images/image2.jpg",roi)
```
![Image](images/image2.jpg)

# Zmiana wielkości zdjęcia
```python
resized = cv2.resize(image, (90, 60))
cv2.imwrite("images/image3.jpg",resized)
```
![Image](images/image3.jpg)


# Zmiana wielkości zdjęcia na podstawie proporcji
```python
r = 400.0 / w
dim = (400, int(h * r))
aspect_resized = cv2.resize(image, dim)
cv2.imwrite("images/image4.jpg",aspect_resized)
```
![Image](images/image4.jpg)

# Zmiana wielkości zdjęcia poprzez imutils
```python
im_resize = imutils.resize(image, width=400)
cv2.imwrite("images/image5.jpg",im_resize)
```
![Image](images/image5.jpg)

# Rotacja obrazu
```python
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imwrite("images/image6.jpg",rotated)
```
![Image](images/image6.jpg)

# Rotacja obrazu poprzez imutils
```python
im_rotate = imutils.rotate(image, -45)
cv2.imwrite("images/image7.jpg",im_rotate)
```
![Image](images/image7.jpg)

# Rotacja obrazu poprzez imutils_bound
```python
im_rotate_bound = imutils.rotate_bound(image, 45)
cv2.imwrite("images/image8.jpg",im_rotate_bound)
```
[Image](images/image8.jpg)

# Nałożenie blura na obraz 
```python
blurred = cv2.GaussianBlur(image, (99, 99), 0)
cv2.imwrite("images/image9.jpg",blurred)
```
[Image](images/image9.jpg)

# Narysowanie prostokąta na obrazek
```python
output = image.copy()
cv2.rectangle(output, (290, 60), (460, 250), (0, 0, 0), 5)
cv2.imwrite("images/image10.jpg",output)
```
[Image](images/image10.jpg)

# Narysowanie kółka na obrazie
```python
output = image.copy()
cv2.circle(output, (400, 160), 100, (255, 255, 255), 5)
cv2.imwrite("images/image11.jpg",output)
```
[Image](images/image11.jpg)

# Narysowanie linii na obrazie 
```python
output = image.copy()
cv2.line(output, (215, 88), (626, 72), (0, 0, 200), 3)
cv2.imwrite("images/image12.jpg",output)
```
[Image](images/image12.jpg)

# Wrzucenie tekstu na obraz
```python
output = image.copy()
cv2.putText(output, "I don't know what i'm signing", (270, 60),
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imwrite("images/image13.jpg",output)
```
[Image](images/image13.jpg)

# Pobieranie nowego obrazu do dalszej pracy
```python
logos=cv2.imread("logo_picture.jpg")
cv2.imwrite("images/image14.jpg",logos)
```
[Image](images/image14.jpg)

# Liczenie obiektów na obrazie
```python
logos = argparse.ArgumentParser()
args = vars(logos.parse_args())
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())
```

# Tworzenie czarno-białego obrazu
```python
gray = cv2.cvtColor(logos, cv2.COLOR_BGR2GRAY)
cv2.imwrite("images/image15.jpg",gray)
```
[Image](images/image15.jpg)

# Wykrywanie krawędzi na obrazie
```python
edged = cv2.Canny(gray, 30, 150)
cv2.imwrite("images/image16.jpg",edged)
```
[Image](images/image16.jpg)

# Threshold obrazu
```python
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imwrite("images/image17.jpg",thresh)
```
[Image](images/image17.jpg)

# Zaznaczanie kontur obiektów na obrazie
```python
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = logos.copy()
for c in cnts:
	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
	cv2.imwrite("images/image18.jpg", output)
```
[Image](images/image18.jpg)

# Erozje i dylatacje na obrazie
## Erozja
```python
mask = thresh.copy()
mask = cv2.erode(mask, None, iterations=2)
cv2.imwrite("images/image19.jpg",mask)
```
[Image](images/image19.jpg)

## Dylatacja
```python
mask = thresh.copy()
mask = cv2.dilate(mask, None, iterations=10)
cv2.imwrite("images/image20.jpg",mask)
```
[Image](images/image20.jpg)

# Operacje maskujące i bitowe na obrazie
```python
mask = thresh.copy()
output = cv2.bitwise_and(logos, logos, mask=mask)
cv2.imwrite("images/image21.jpg",output)
```
[Image](images/image21.jpg)
