# coding=utf-8
import sys
import os
# sys.path.insert(0, "../")
import time
import aiml
import random
kernel = aiml.Kernel()
dialog = ['为什么我付出那么多却没有回报?', '我一直把他当成是我最好的朋友,但是遇到困难他居然帮别人也不帮助我!', '我很委屈', '我感觉很累', '我想我大概是看错了人', '我在想是不是我情商太低了', '是不是我太容易相信别人了?', '好的', '是的',
          '好吧', '是的', '好的', '我想不到', '嗯好的', '感觉会的', '我会有这样的新想法...', '好多了', '我愿意', '有的', '没有', '会的', '我是一个很容易激动的人', '会的',
          '是的', '原来是这样啊', '继续', '那我们如何让庄稼长得更好呢', '天生的', '记忆力很好', '很强的执行力,敏捷的反应能力,幽默感']

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
# kernel.learn("AIMLSet/cn-startup.xml")
# k.learn("ChatBot/cn-test.aiml")
# k.learn("cn-startup.xml")
# kernel.respond('LOAD CN TEST')
# kernel.respond('LOAD TEST')

# k.learn("psy-dialog.aiml")
# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(learnFiles="AIMLSet/cn-startup.xml", commands="LOAD CN TEST")
    # kernel.saveBrain("bot_brain.brn")
if __name__ == '__main__':
    print("@@TEST START...@@")
    time.sleep(1)
    for msg in dialog:
        print("Human: ", end='')
        for item in msg:
            # time.sleep(0.1)
            print(item, end='')
        print(' ')
        res = kernel.respond(msg).replace(' ', '')
        print('BOT: ', end='')
        for item in res:
            # time.sleep(0.1)
            print(item, end='')
        # time.sleep(1)
        print(' ')
    while True:
        message = input("Enter your message to the bot: ")
        if message == "quit":
            exit()
        elif message == "save":
            kernel.saveBrain("bot_brain.brn")
        else:
            bot_response = kernel.respond(message)
            print(bot_response.replace(' ', ''))

# Do something with bot_response
