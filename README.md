# audioRecord
- 仿微信的语音段传输v1.0
- 使用 webRTC(获取和录制音频)和 webSocket（发送音频流）

# ToDo
- 用vue-pwa框架搭建项目
- 集成vux UI框架

# 启动
- pip install tornado
- python server.py
- 启动nginx或caddy服务器
- 一个浏览器打开index.html
- 另一个浏览器打开index.html
- 开始录音，停止自动发送

# 通过docker compose 直接运行
  docker-compose up -d

# 效果图
![](1.png)
