# coding=utf-8
import sys
# sys.path.insert(0, "../")

import aiml

k = aiml.Kernel()

# Use the 'learn' method to load the contents
# of an AIML file into the Kernel.
k.learn("AIMLSet/cn-startup.xml")
# k.learn("ChatBot/cn-test.aiml")
# k.learn("cn-startup.xml")
k.respond('LOAD TEST')
# k.learn("psy-dialog.aiml")
# Use the 'respond' method to compute the response
# to a user's input string.  respond() returns
# the interpreter's response, which in this case
# we ignore.
# while True:
#     print k.respond(raw_input("> ")).replace(' ', '')
