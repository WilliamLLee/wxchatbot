# retrain.py
# function: retrain the chatterbot after initial train
# author: jack-lio
# github: https://github.com/Jack-Lio
# date: 2019.12.27

from chatbot import myChatBot
from chatterbot.trainers import ListTrainer
from data import get_text
#设置训练器，采用句子序列的方式训练
trainer = ListTrainer(myChatBot)

trainer.train([
    "你好",
    "你好，我是你的专属机器人Jack！",
    "你会做什么？",
    "上知天文，下知地理，无所不知无所不晓！",
    "这么厉害啊！那你知道南开大学吗？",
    "当然知道，南开大学是主人读的大学啊，我最了解她了！",
    "南开大学",
    "南开大学是一所著名的双一流大学",
    "南开大学是周恩来的母校",
    "谁是最帅的人？",
    "当然是我的主人您啊！",
    "谁最帅？",
    "当然是李伟啊！我的主人天下第一帅！",
])

trainer.train(get_text())