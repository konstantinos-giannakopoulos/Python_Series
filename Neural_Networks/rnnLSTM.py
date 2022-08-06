import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.layers import Activation, Dense, LSTM
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


# 1) loading data
filepath = tf.keras.utils.get_file('shakespeare.txt','https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(filepath, 'rb').read().decode(encoding='utf-8').lower()

# 2) preparing data
text = text[300000:800000]

# 3) converting text
characters = sorted(set(text))
char_to_index = dict((c, i) for i,c in enumerate(characters))
index_to_char = dict((i, c) for i,c in enumerate(characters))

# 4) splitting text
SEQ_LENGTH = 40
STEP_SIZE = 3

sentences =  []
next_char = []

for i in range(0,len(text) - SEQ_LENGTH, STEP_SIZE):
    sentences.append(text[i:i + SEQ_LENGTH])
    next_char.append(i + SEQ_LENGTH)

# 5) convert to numpy format
x = np.zeros((len(sentences), SEQ_LENGTH, len(characters)),dtype=np.bool)
y = np.zeros((len(sentences), len(characters)),dtype=np.bool)

for i, satz in enumerate(sentences):
    for t, char in enumerate(satz):
        x[i, t, char_to_index[char]] = 1
    y[i, char_to_index[char]] = 1

# 6) build recurrent neural network
model = Sequential()
model.add(LSTM(8, input_shape=(SEQ_LENGTH, len(characters)))) #128
model.add(Dense(len(characters)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',optimizer=RMSprop(lr=0.01))
model.fit(x,y, batch_size=256, epochs=4)
print("OK")

# 7) helper function
def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(exps)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)
    
# 8) generating texts
def generate_text(length, temperature):
    start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
    generated = ''
    sentence = text[start_index: start_index + SEQ_LENGTH]
    generated += sentence
    for i in range(length):
        x_predictions = np.zeros((1, SEQ_LENGTH, len(characters)))
        for t, char in enumerate(sentence):
            x_predictions[0, t, char_to_index[char]] = 1
        predictions = model.predict(x_predictions, verbose=0)[0]
        next_index = sample(predictions, temperature)
        next_character = index_to_char[next_index]
    
        generated += next_character
        sentence =  sentence[1:] + next_character
    return generated

# 9) results
print(generate_text(300, 0.2)) # 
print(generate_text(300, 0.4)) # conservative
print(generate_text(300, 0.5)) # 
print(generate_text(300, 0.6)) # medium
print(generate_text(300, 0.7)) #
print(generate_text(300, 0.8)) # experimental
