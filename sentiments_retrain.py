#!/usr/bin/env python

from data_load_amz import SentimentsData
from keras.models import load_model
from keras.optimizers import Adam
from keras.preprocessing import sequence

print("Loading the model...")
model = load_model("sentiments_full_glove_embeddings.hdf5")
model.compile(loss='binary_crossentropy',
              optimizer=Adam(),
              metrics=['accuracy'])

model.summary()

print("Getting the complete data to predict on...")
sd = SentimentsData()
print('Loading training and test data...')
(x_train, y_train), (x_test, y_test) = sd.load()

max_features = sd.corpus_size
maxlen = 1000 #sd.max_size  # cut texts after this number of words (among top max_features most common words)
batch_size = 64
sd.create_embeddings_matrix()

print('Padded sequences (samples x time)')
x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

print('Training...')
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=5,
          validation_data=(x_test, y_test))
score, acc = model.evaluate(x_test, y_test,
                            batch_size=batch_size)
print('Testing Data Score:', score)
print('Testing Data Accuracy:', acc)

model.save("models/sentiments_full_glove_embeddings_1.hdf5")
