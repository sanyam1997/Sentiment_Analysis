# Sentiment Analysis

This is a sentiments analysis example using LSTM( Long short-term memory ). I tried on 2 different datasets
  
a. Amazon food review dataset - https://www.kaggle.com/snap/amazon-fine-food-reviews

b. News sentiments on Dow Jones Index - https://www.kaggle.com/aaron7sun/stocknews

Amazon dataset is over 25Mb so it has to be downloaded from the link and should be placed in the amazon folder.

Install 

>Python 2.7

>Pandas

>Nltk

>Numpy

>Keras

Stock news dataset is small and all attempts to learn on such small dataset do not generalize. 
The training accuracy gets up to 99.1% but the validation accuracy does not exceed 55.1%.

Amazon food review data set is large with around 0.5M data points. I train on first 50k examples and use a stacked LSTM
network with Embedding layer. I downloaded the Glove weights for the embedding layer.
This training accuracy gets up to 94.9% and the validation accuracy is around 92.8%. When I run it on the next 100k unseen examples
the accuracy drops to 82.1%.

## Files

The following module loads the Stock news dataset
> data_load.py

The following module loads first 50k of the amazon dataset, it expects embeddings/glove.6B.100d.txt and amazon/Reviews.csv
It considers 0 & 1 stars as negative reviews, removes 3 stars and considers 4 & 5 stars as positive reviews
> data_load_amz.py

The following module trains the LSTM for sentiments analysis 
> sentiments.py

The following module loads the last saved module and retrains it for more epochs
> sentiments_retrain.py

The following module loads the trained model and uses it to predict sentiments on a dataset. You would need to adjust the 
dataset on which to train in the load_data_amz.py
> predict.py
