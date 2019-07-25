# coding=utf-8
import sys
# sys.path.insert(0, "../")

import aiml
# AIML 文件加载
k = aiml.Kernel()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
k.learn("AIMLSet/cn-startup.xml")
# k.learn("ChatBot/cn-test.aiml")
# k.learn("cn-startup.xml")
# 话题导入
k.respond('LOAD TOPIC')
