# Bilibili Card

一个简陋的 Bilibili 统计卡片，基于`Python`开发，生成卡片为`.svg`格式   
并不是很好用🙃

## 功能

输入B站UID可以自动获取头像、性别、生日、粉丝数、关注数、签名等信息，并按照预设的模板生成一张`.svg`格式的卡片，下面有演示

## 使用方法

下载本项目代码，运行`build_card.py`，输入B站UID即可  
生成的卡片位于`cards/`文件夹下，`UID.svg`文件  
`template/`中提供了一种**过于简陋**的模板样式🙃

## 贡献 

#### 提供一些更好看的模板

模板应为`.svg`格式，在`template/`文件夹中可以找到例子，不妨顺便提交一个演示文件

#### 改进代码

由于我并不会`JS`，对于`.svg`等格式也是刚学的，你大可提交 PR 改进代码

#### 你想做的任何事

。。。

## 可改进之处&Bugs

- 头像改为base64格式
- 搞一个可以更新的网站
- 卡片背景
- 卡片加点别的信息
- 。。。

## 演示

![card](https://raw.githubusercontent.com/dogefy/bilibili-card/main/demo/672342685.svg)  
如你所见，上面这个例子在仓库的demo文件夹中，并不具备自动更新的功能 :(

## 协议
[MIT License](https://github.com/dogefy/bilibili-card/blob/main/LICENSE)