# chatbot.py
# function: init the setting of chatbot
# author: jack-lio
# github: https://github.com/Jack-Lio
# date: 2019.12.27

from chatterbot import ChatBot,comparisons,response_selection,languages,filters
# 初始化聊天机器人设置
myChatBot = ChatBot(
    "ChatterJack",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            # 'default_response': '我没明白你的意思诶，不过我会继续学习的！',
            'maximum_similarity_threshold': 0.90
        }
    ],
    statement_comparison_function=comparisons.levenshtein_distance,
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
    ],
    filters=[filters.get_recent_repeated_responses],            # 去除最近重复的回应，避免机器人重复说一样的话
    response_selection_method = response_selection.get_first_response,
    input_adapter='chatterbot.input.VariableInputTypeAdapter',
    output_adapter='chatterbot.output.OutputAdapter',
)

