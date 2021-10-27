# Image Editor Project
* [Features](#features)
* [User Interface](#user-interface)
* [Examples](#examples)
* [Technology Stack](#technology-stack)
* [Run Application](#run-application)

## Features
| Feature | Description |
| :---: | :--- |
| Horizontal Flip | Flips the image across its central vertical line. |
| Vertical Flip | Flips the image across its central horizontal line. |
| Grayscale | Converts the image to grayscale. |
| Sepia | Sepia filter is applied to the image. |
| Binarization | Image pixels are set to either black or white depending on their original intensity. |
| Histogram Equalization | Histogram Equalization is applied to the image. |
| Invert Colors | The color of each pixel in the image is inverted. |
| Smoothness | Apply a blur to the image. |
| Sharpness| Sharpen the image. |
| Brightness | Change the brightness of the image. |
| Contrast | Change the contrast of the image. |
| Gamma Correction | Apply a gamma correction to the image. |
| Saturation | Change the saturation of the image. |
| Temperature | Change the temperature of the image. |
| Resize | Resize the image by some factor. Visible after download. |
| Color Pop | The color pop filter allows you isolate a chosen color in your image. Any pixel in the image that is not within a certain range of the chosen color is converted to grayscale. |
| Crop | Crop the image. |

## User Interface

### Upload
<img src="https://github.com/aaronmills0/image-editor/blob/main/readme_images/ui_uploadscreen.PNG" width="800">

### Canvas
<img src="https://github.com/aaronmills0/image-editor/blob/main/readme_images/ui_canvasscreen.PNG" width="800">

## Examples
| Original | Edited |
| :---: | :---: |
| <br><img src="https://github.com/aaronmills0/image-editor/blob/main/readme_images/francesco_ungaro.jpeg" width="500"><br>Photo by: Francesco Ungaro |  <img src="https://github.com/aaronmills0/image-editor/blob/main/readme_images/francesco_ungaro_edited.jpeg" width="500"><br> |
| <br><img src="https://github.com/aaronmills0/image-editor/blob/main/readme_images/catia_matos.jpeg" width="500"><br>Photo by: Catia Matos |  <img src="https://github.com/aaronmills0/image-editor/blob/main/readme_images/catia_matos_edited.jpeg" width="500"><br> |
| <br><img src="https://github.com/aaronmills0/image-editor/blob/main/readme_images/ricardo_esquivel.jpeg" width="500"><br>Photo by: Ricardo Esquivel |  <img src="https://github.com/aaronmills0/image-editor/blob/main/readme_images/ricardo_esquivel_edited.jpeg" width="500"><br> |

## Technology Stack
* Django
* OpenCV

## Run Application
python manage.py runserver
