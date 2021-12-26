# Booking System(2021 TOC Final Project)
## Welcome to Booking System

## Usage
### * 初始的state為`user`  
以下是歡迎訊息，有rich menu點按可以開始進行互動。  

![](https://i.imgur.com/a0Bceli.jpg)  

### * 按下rich menu的「關於我們」trigger `menu`  
按下rich menu 的`關於我們`或輸入`@關於我們`可以查看Booking system的功能和詳細內容，上面的旋轉template也可以按按看進行其他互動。  

![](https://i.imgur.com/wGZRBua.jpg)

### * 按下rich menu的「使用說明」trigger `about`  
按下rich menu 的`使用說明`或輸入`@使用說明`可以查看Booking system 的旅館資訊，包括成功大學良好的口碑和引以為傲的企業最愛排名。  

![](https://i.imgur.com/1FXKUeR.jpg)

### * 按下rich menu的「位置資訊」trigger `info`  
按下rich menu 的`位置資訊`或輸入`@位置資訊`，Booking system會傳送給你國立成功大學的座標，點按開始進行導航。

![](https://i.imgur.com/rEawhvx.jpg)

### * 按下rich menu的「聯絡我們」trigger `comm`  
按下rich menu 的`聯絡我們`或輸入`@聯絡我們`，Booking system會傳送給你聯絡電話，點按即可進行通話。  

![](https://i.imgur.com/02nDRzo.jpg)

### * 此圖為點擊`撥打電話`後，進行撥打電話的畫面  
> 使用0123456789作為示範  

![](https://i.imgur.com/bAbNhcH.jpg)

### * 按下rich menu的「房間預約」trigger `room_booking`  
按下rich menu 的`房間預約`或輸入`@房間預約`，開始進行訂房流程，  
訂房流程依序需trigger：`name`,`data`,`day`,`breakfast`四個states，分別需要你輸入「姓名」、「日期」、「天數」、「早餐種類」，  來完成訂房，如果中途或完成訂房後後悔想取消預約，點按rich menu 的`取消訂房`，或輸入`@取消訂房`即可清空訂房資料，後面會進行示範。

![](https://i.imgur.com/DnxUnED.jpg)

(訂房成功會呈現你輸入過的訂房資訊)
### * 輸入`查詢訂房`trigger `search`
查詢你的訂房紀錄。
### * 按下rich menu的「取消訂房」trigger `cancel`
取消你的訂房紀錄，取消後想再查詢訂房紀錄會呈現查無訂房資料的相關訊息。

![](https://i.imgur.com/YTj7IPG.jpg)

### * 輸入`查看功能`trigger`lobby`
輸入查看功能後可以點選`show fsm`和`查詢訂房`，來進行互動。
1. show fsm: chat bot傳此次project的fsm picture。
2. 查詢訂房:查詢你的訂房紀錄。


![](https://i.imgur.com/cnWDBii.jpg)

### * 輸入`意見回饋 「主旨」 「內容」`trigger `request`
依照格式輸入`意見回饋` `主旨` `內容`即可將你的寶貴意見寄信給開發人員。（我本人@@）

![](https://i.imgur.com/beYkI9q.jpg)

### * 此圖為我收到的信件
![](https://i.imgur.com/PkZ7m1G.jpg)


## Finite State Machine
![fsm](https://i.imgur.com/csunAds.png)

[![Maintainability](https://api.codeclimate.com/v1/badges/dc7fa47fcd809b99d087/maintainability)](https://codeclimate.com/github/NCKU-CCS/TOC-Project-2020/maintainability)

[![Known Vulnerabilities](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020/badge.svg)](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020)


Template Code for TOC Project 2020

A Line bot based on a finite state machine

More details in the [Slides](https://hackmd.io/@TTW/ToC-2019-Project#) and [FAQ](https://hackmd.io/s/B1Xw7E8kN)

## Setup

### Prerequisite
* Python 3.6
* Pipenv
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install pipenv

pipenv --three

pipenv install

pipenv shell
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)
	* [Note: macOS Install error](https://github.com/pygraphviz/pygraphviz/issues/100)


#### Secret Data
You should generate a `.env` file to set Environment Variables refer to our `.env.sample`.
`LINE_CHANNEL_SECRET` and `LINE_CHANNEL_ACCESS_TOKEN` **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

#### a. Ngrok installation
* [ macOS, Windows, Linux](https://ngrok.com/download)

or you can use Homebrew (MAC)
```sh
brew cask install ngrok
```

**`ngrok` would be used in the following instruction**

```sh
ngrok http 8000
```

After that, `ngrok` would generate a https URL.

#### Run the sever

```sh
python3 app.py
```

#### b. Servo

Or You can use [servo](http://serveo.net/) to expose local servers to the internet.




## Deploy
Setting to deploy webhooks on Heroku.

### Heroku CLI installation

* [macOS, Windows](https://devcenter.heroku.com/articles/heroku-cli)

or you can use Homebrew (MAC)
```sh
brew tap heroku/brew && brew install heroku
```

or you can use Snap (Ubuntu 16+)
```sh
sudo snap install --classic heroku
```

### Connect to Heroku

1. Register Heroku: https://signup.heroku.com

2. Create Heroku project from website

3. CLI Login

	`heroku login`

### Upload project to Heroku

1. Add local project to Heroku project

	heroku git:remote -a {HEROKU_APP_NAME}

2. Upload project

	```
	git add .
	git commit -m "Add code"
	git push -f heroku master
	```

3. Set Environment - Line Messaging API Secret Keys

	```
	heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
	heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
	```

4. Your Project is now running on Heroku!

	url: `{HEROKU_APP_NAME}.herokuapp.com/callback`

	debug command: `heroku logs --tail --app {HEROKU_APP_NAME}`

5. If fail with `pygraphviz` install errors

	run commands below can solve the problems
	```
	heroku buildpacks:set heroku/python
	heroku buildpacks:add --index 1 heroku-community/apt
	```

	refference: https://hackmd.io/@ccw/B1Xw7E8kN?type=view#Q2-如何在-Heroku-使用-pygraphviz

## Reference
[Pipenv](https://medium.com/@chihsuan/pipenv-更簡單-更快速的-python-套件管理工具-135a47e504f4) ❤️ [@chihsuan](https://github.com/chihsuan)

[TOC-Project-2019](https://github.com/winonecheng/TOC-Project-2019) ❤️ [@winonecheng](https://github.com/winonecheng)

Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)

[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
(https://github.com/chihsuan)

[TOC-Project-2019](https://github.com/winonecheng/TOC-Project-2019) ❤️ [@winonecheng](https://github.com/winonecheng)

Flask Architecture ❤️ [@Sirius207](https://github.com/Sirius207)

[Line line-bot-sdk-python](https://github.com/line/line-bot-sdk-python/tree/master/examples/flask-echo)
