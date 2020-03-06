import jieba
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from tensorflow.keras.backend import expand_dims
import sys
model = load_model('cnn_model.h5')
def predict(text):
    cw = list(jieba.cut(text))
    word_id = []
    for word in cw:
        try:
            temp = dict_text[word]
            word_id.append(temp)
        except:
            word_id.append(0)
    word_id = np.array(word_id)
    word_id = word_id[np.newaxis, :]
    sequences = pad_sequences(word_id, maxlen=1500, padding='post')
    result = np.argmax(model.predict(sequences))
    if (result == 1):
        print("有效规则")
    else:
        print("无效规则")




predict(sys.argv[0])