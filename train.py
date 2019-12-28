# train.py
# function: initial train of chatterbot
# author: jack-lio
# github: https://github.com/Jack-Lio
# date: 2019.12.27

from chatbot import myChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
# 设置训练器
trainer = ChatterBotCorpusTrainer(myChatBot)
# 使用现有的中文语料库训练它，具备初始的问答能力
#trainer.train("chatterbot.corpus.chinese")  # 中文语料库
# 使用自定义的的中文语料库训练它
trainer.train("./corpus/")  # 中文语料库
