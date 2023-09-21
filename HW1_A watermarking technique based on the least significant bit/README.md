# 撰寫浮水印之程式
* 於<影像處理與電腦視覺>課本章節 1.9作業 第4題(第七版課本p. 25)，"寫一程式程式以實作 1.6節 所提的植基於位元平面之浮水印"。
* 程式的輸入圖片有兩張，原圖及嵌入浮水印必須為兩張明顯不同的的 "同學自拍照" (都為灰階圖即可)，輸出圖片有兩張，
  * 對原圖分別把 8bit  去掉 least significant X bits(X為同學的學號最後一位數餘4加1)，並嵌入浮水印輸出，
  * 再從該圖還原出所嵌入的浮水印輸出。


## Table of Contents

- [Environment](#environment)
- [Installation](#installation)
- [Give it a try with yourself](#give-it-a-try-with-yourself)
- [What's included](#whats-included)
- [Dependencies](#dependencies)
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
```
