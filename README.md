`python3` `AMIL` `Django`
# ChatBot

AIML 1.0 in Chinese Dialog
AIML 中文对话Django接口 基于em-amil库

# 使用安装 
  1. 安装python3环境，及pip 包管理工具
  2. pip install -r requirements.txt
  3. python manager.py runserver localhost:8888
  4. 接口调用
# 接口说明
  - 接口地址  
  
        <ip>:<host>/chat/ask="xxx"&sessionid="xxx"   
  
  - 接口HTTP请求类型  
    
    `GET`
    
  - 接口参数
  
    参数|必选|类型|说明
    :----:|:---:|:---:|:---:
    ask  |ture    |string|对话内容
    sessionid|ture|string|用户对话ID
  
  - 演示图例 
  
    ![avatar](/images/postmancapture.png)