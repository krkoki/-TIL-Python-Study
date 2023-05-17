from chatbot.db.DatabaseConfig import *
from chatbot.db.Database import Database
from chatbot.Preprocess2 import Preprocess2

# 전처리 객체 생성
p = Preprocess2(word2index_dic='../data/chatbot_dict.bin',
                userdic='../data/user_dic.tsv')

# 질문/답변 학습 디비 연결 객체 생성
db = Database(host=DB_HOST, user=DB_USER,
              password=DB_PASSWORD, db_name=DB_NAME)
db.connect() # db 연결

# 원문
items = ["오전에 탕수육 10개 주문합니다",
         "안녕하세요",
         "반가워요",
         "오늘 예약할께요",
         "군만두 주문할게요"]

# 의도 파악
from chatbot.IntentModel import IntentModel
for query in items:
    intent = IntentModel(model_name='../model/intent_model.h5', proprocess=p)
    predict = intent.predict_class(query)
    intent_name = intent.labels[predict]

# 개체명 인식
from chatbot.NerModel import NerModel
ner = NerModel(model_name='../model/ner_model.h5', proprocess=p)
predicts = ner.predict(query)
ner_tags = ner.predict_tags(query)
print("질문 : ", query)
print("=" * 100)
print("의도 파악 : ", intent_name)
print("개체명 인식 : ", predicts)
print("답변 검색에 필요한 NER 태그 : ", ner_tags)
print("=" * 100)

# 답변 검색
from chatbot.FindAnswer import FindAnswer
try:
    f = FindAnswer(db)
    answer_text, answer_image = f.search(intent_name, ner_tags)
    answer = f.tag_to_word(predicts, answer_text)
except:
    answer = "죄송해요 무슨 말인지 모르겠어"
print("답변 : ", answer)
db.close() # db 연결 종료