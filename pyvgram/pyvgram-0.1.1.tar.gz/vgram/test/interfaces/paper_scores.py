from typing import List

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import fetch_20newsgroups
from sklearn.pipeline import Pipeline
from vgram import VGramTokenizer, SplitLevel


class VGram:
    def __init__(self, size=10000, iter_num=10):
        self.tokenizer = VGramTokenizer(size, split_level=SplitLevel.LINE, verbose=True)
        self.iter_num = iter_num

    def fit(self, X: List, y: List = None, **kwargs):
        self.tokenizer.fit(X)
        return self

    def transform(self, X: List, y: List = None, **kwargs):
        seqs = self.tokenizer.encode(X)
        return [" ".join(str(id) for id in seq) for seq in seqs]


def basic_cls():
    # fetch data
    train, test = fetch_20newsgroups(subset='train'), fetch_20newsgroups(subset='test')
    data = train.data + test.data

    # make vgram pipeline and fit it
    vgram = Pipeline([
        ("vgb", VGram(size=10000, iter_num=10)),
        ("vect", CountVectorizer())
    ])
    # it's ok, vgram fit only once
    # vgram.fit(data)

    # fit classifier and get score
    pipeline = Pipeline([
        ("vgram", VGram(size=10000, iter_num=10)),
        ("vect", CountVectorizer()),
        ('tfidf', TfidfTransformer(sublinear_tf=True)),
        ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-4, max_iter=100, random_state=42))
    ])
    pipeline.fit(train.data, train.target)
    print("train accuracy: ", np.mean(pipeline.predict(train.data) == train.target))
    print("test accuracy: ", np.mean(pipeline.predict(test.data) == test.target))

    # show first ten elements of constructed vgram dictionary
    alpha = pipeline.named_steps["vgram"].decode(pipeline.named_steps["vgram"].alphabet())
    print("First 10 alphabet elements:", alpha[:10])


def main():
    basic_cls()


if __name__ == '__main__':
    main()

# train accuracy:  0.9916033233162453
# test accuracy:  0.8131970260223048
