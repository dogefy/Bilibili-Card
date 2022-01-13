# Bilibili Card

[简体中文](https://github.com/dogefy/bilibili-card/blob/main/README.md) / [English](https://github.com/dogefy/bilibili-card/blob/main/README_en.md)  

A simple status card for Bilibili, develped by `Python`, in `.svg` format.  
not good as the expectation 🙃

## Feature

Get `face photo, gender, birthday, followers, followings, sign` **automatically** through Bilibili UID.  
Then get a card in `.svg` format according to the template in `template/`.  
A simple demo can be found below.  

## Usage

Download code, run `build_card.py` , and input the Bilibili UID.  
The card is in `cards/`, named as `UID.svg`.  
A simple template is in `template/`.🙃


## Contribution 

#### Provide more templates

Template should be in `.svg` format, examples can be found in `template/`, a demo is also needed.

#### Improve & Fix

Some code is stupid and inefficient, you can help to improve！ 

#### Others

You can fork and commit PRs freely.

## Future features & Bugs

- a web server to get card and update automatically
- more backgrounds
- more imformation
- . . .

## Demo

![card](https://raw.githubusercontent.com/dogefy/bilibili-card/main/demo/672342685.svg)

As you see, this demo is in `demo/`, so it cannot be updated automatically.  :(

## License

[MIT License](https://github.com/dogefy/bilibili-card/blob/main/LICENSE)