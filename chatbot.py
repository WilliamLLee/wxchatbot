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
            'default_response': '我没明白你的意思诶，不过你可以问我南开教师有关的问题，我对计算机学院的老师很熟悉哦！我还会说笑话唱歌呢！',
            'maximum_similarity_threshold': 0.90
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Jack,在吗？',
            'output_text': '我一直都在你的心里^_^',
        }
    ],
    statement_comparison_function=comparisons.levenshtein_distance,
    # statement_comparison_function=comparisons.SynsetDistance,
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
    ],
    filters=[filters.get_recent_repeated_responses],            # 去除最近重复的回应，避免机器人重复说一样的话
    response_selection_method = response_selection.get_first_response,
    # input_adapter='chatterbot.input.VariableInputTypeAdapter',
    # output_adapter='chatterbot.output.OutputAdapter',
    read_only=True,    # 避免在学习每一次对话输入
)

