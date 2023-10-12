# Writing a watermarking program 撰寫浮水印之程式
## English version
* In <Image Processing and Computer Vision> textbook Chapter 1.9 Assignment Question 4 (7th edition textbook p. 25), 'Write a program to implement the bit-plane-based watermarking described in Section 1.6.

* The program takes two input images, the original image and the watermark image, which should be two clearly distinct 'classmate selfies' (both in grayscale). The program produces two output images.
  * For the original image, remove the least significant X bits (where X is the remainder when the last digit of the classmate's student ID is divided by 4 plus 1), and then embed the watermark before outputting it.
  * Then, extract the embedded watermark from that image and produce the output.
## Traditional Chinese version
* 於<影像處理與電腦視覺>課本章節 1.9作業 第4題(第七版課本p. 25)，"寫一程式程式以實作 1.6節 所提的植基於位元平面之浮水印"。

* 程式的輸入圖片有兩張，原圖及嵌入浮水印必須為兩張明顯不同的的 "同學自拍照" (都為灰階圖即可)，輸出圖片有兩張，
  * 對原圖分別把 8bit  去掉 least significant X bits(X為同學的學號最後一位數餘4加1)，並嵌入浮水印輸出，
  * 再從該圖還原出所嵌入的浮水印輸出。


## Table of Contents

- [Environment](#environment)
- [Installation](#installation)
- [Give it a try with yourself](#give-it-a-try-with-yourself)
- [Result](#result)
- [What's included](#whats-included)
- [References](#references)

## Environment

Windows 10 64-bit, Visual Studio Code, Python @3.11.5, Anaconda3.

## Installation

1. Download [VSCode](https://code.visualstudio.com/Download), [Anaconda](https://www.anaconda.com/download).
2. After VScode install completely, you can use the Extension in VSCode. Searching for the Python package to plug in. 
![python extension](https://github.com/EricChen0313/A-watermarking-technique-based-on-the-least-significant-bit/blob/main/HW1_A%20watermarking%20technique%20based%20on%20the%20least%20significant%20bit/ImageExampleFolder/python%20extension%20in%20VSCode.jpg)
3. Open Anaconda prompt, and enter the command 'pip install opencv-python', then you can use opencv in VSCode.

## Give it a try with yourself

```bash
# clone the repo
$ git clone https://github.com/EricChen0313/A-watermarking-technique-based-on-the-least-significant-bit.git

# open the folder in Visual Studio Code

# push the 'Terminal' button above
$ python hw_code.py

# then it will give out 4 pictures like below
```

## Result
![Result Image](https://github.com/EricChen0313/A-watermarking-technique-based-on-the-least-significant-bit/blob/main/HW1_A%20watermarking%20technique%20based%20on%20the%20least%20significant%20bit/Images/RESULT_IMAGE.jpg)

<table>
    <tr> 
        <td>position</td>
        <td>explanation</td>
    </tr>
    <tr> 
        <td>Left top corner</td>
        <td>Main picture.</td>
    </tr>
    <tr> 
        <td>Right top corner</td>
        <td>The watermarking effect image you want to mix in the main picture.</td>
    </tr>
     <tr> 
        <td>Left bottom corner</td>
        <td>Result picture. (main pic + watermarking effect)</td>
    </tr>
    <tr> 
        <td>Right bottom corner</td>
        <td>Retrieve the embedded watermark image from the result image.</td>
    </tr>
</table>

## What's included
```
HW1_A watermarking technique based on the least significant bit
├── ImageExampleFolder/              
│   └── python extension in VSCode.jpg   #Indicative sample image
|
├── Images/              
│   └── RESULT_IMAGE.jpg          #The whole result picture print in a single window
│   └── effect.jpg                #Original effect image with RGB channels
│   └── main.jpg                  #Original main image with RGB channels
│   └── new_main.jpg              #Main image after embedding the effect one 
│   └── resized_effect.jpg        #Effect image after resizing
│   └── resized_gray_effect.jpg   #Effect image after resizing and grayscaling
│   └── resized_gray_main.jpg     #Main image after resizing and grayscaling
│   └── resize_main.jpg           #Main image after resizing
│   └── result of effect.jpg      #The embedded watermark image retrieved from the result one
│   └── result.jpg                #Also main image after embedding the effect one  
│   └── result_effect.jpg         #Effect image we want to embedd into the main one 
│   └── result_main.jpg           #Also main image after embedding the effect one  
|
├── code/              
│   └── gray_img_code.py          #Turning the RGB image to gray one  
│   └── hw_code.py                #The code using a watermarking technique based on the least significant bit 
│   └── resize_code.py            #Resizing the image to the desired viewing size
│
└── README.md
```

## References
- [opencv 隱藏浮水印](https://benjaminnl.pixnet.net/blog/post/59461240-opencv-%E9%9A%B1%E8%97%8F%E6%B5%AE%E6%B0%B4%E5%8D%B0)
- [影像的旋轉、翻轉和改變尺寸](https://steam.oxxostudio.tw/category/python/ai/opencv-resize.html)
- [影像的色彩轉換](https://steam.oxxostudio.tw/category/python/ai/opencv-cvtcolor.html)
