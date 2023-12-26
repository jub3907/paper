from LDAscikit import LDAprocess
from LDAscikit import Utils

# use_f = 0
# # 0: 엘보우포인트 찾는거
# # 1: 토픽모델링
# df_matrix = Utils.ReadCSV(filename = "selected_keyword_1_1.csv", delimiter = ',')
# df_matrix = Utils.Edgelist2Matrix(df_matrix)

# if use_f == 1:
#     DocTopic, TopicWord = LDAprocess.LDAexecute(df_matrix, 15, 1, 25)
#     TopicInfo = LDAprocess.TopicInfo(TopicWord)

#     Utils.WriteCSV("DocTopic.csv", DocTopic)
#     Utils.WriteCSV("TopicWord.csv", TopicWord)
#     Utils.WriteCSV("TopicInfo.csv", TopicInfo)
# elif use_f == 0:
#     result = LDAprocess.TopicDecision(df_matrix, 1, 50, 1, 0)
#     # 토픽1~50, 3번째 숫자를 늘려야할듯
#     Utils.WriteCSV("TopicDecision.csv", result)
# elif use_f == 2:
#     Utils.WriteCSV(filename="DocTerm.csv", matrix=df_matrix, index=True)