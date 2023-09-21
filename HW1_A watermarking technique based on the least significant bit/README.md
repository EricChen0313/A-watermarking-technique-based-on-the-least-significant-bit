# 撰寫浮水印之程式
* 於<影像處理與電腦視覺>課本章節 1.9作業 第4題(第七版課本p. 25)，"寫一程式程式以實作 1.6節 所提的植基於位元平面之浮水印"。
* 程式的輸入圖片有兩張，原圖及嵌入浮水印必須為兩張明顯不同的的 "同學自拍照" (都為灰階圖即可)，輸出圖片有兩張，
  * 對原圖分別把 8bit  去掉 least significant X bits(X為同學的學號最後一位數餘4加1)，並嵌入浮水印輸出，
  * 再從該圖還原出所嵌入的浮水印輸出。


## Table of Contents

- [Environment](#environment)
- [Installation](#installation)
- [Create React App](#create-react-app)
- [What's included](#whats-included)
- [Dependencies](#dependencies)
- [References](#references)

## Environment

Windows 10 64-bit, Visual Studio Code, Python @3.11.5, Anaconda3.

## Installation

1. Download [VSCode](https://code.visualstudio.com/Download).
2. After install completely, you can use the Extension in VSCode. Searching for the Python package to plug in.