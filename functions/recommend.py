import pandas as pd
import numpy as np
from gensim.models.word2vec import Word2Vec
from gensim.models import Word2Vec
from konlpy.tag import Okt

# data import
combine_df = pd.read_csv('test_data.csv', encoding="utf-8")
place_df = pd.read_csv('p_data.csv', encoding="utf-8")

# train
train_data = combine_df['keyword_reviews']

tokenized_data=[]
for sentence in train_data:
    keywords = sentence.split('\r\n')
    tokenized_data.append(keywords)

combine_df['tag'] = tokenized_data

split_data=[]
for sentence in place_df['keyword_reviews']:
    keywords = sentence.split('\r\n')
    split_data.append(keywords)

place_df['tag'] = split_data

model = Word2Vec(sentences=tokenized_data, vector_size=100, window = 5, min_count = 5, workers = 4, sg = 0)

def recommend_places(input_string, target_age=None):
    similar_words = model.wv.most_similar(input_string, topn=3)
    similar_words = [word[0] for word in similar_words]

    if target_age:
        filtered_df = place_df[(place_df['tag'].apply(lambda x: any(word in x for word in similar_words))) &
                               ((place_df['target_age'] == target_age) | (place_df['target_age'].isnull()))]
    else:
        filtered_df = place_df[place_df['tag'].apply(lambda x: any(word in x for word in similar_words))]

    filtered_df = filtered_df.sort_values(['rating', 'rating_count', 'review_count'], ascending=[False, False, False]).head(5)

    return filtered_df

recommended_places = recommend_places("컨셉이 독특해요")
print(recommended_places['name'])