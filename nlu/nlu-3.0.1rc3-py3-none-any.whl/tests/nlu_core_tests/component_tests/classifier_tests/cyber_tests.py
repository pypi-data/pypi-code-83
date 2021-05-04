

import unittest
from nlu import *
class TestCyber(unittest.TestCase):

    def test_quick(self):
        # p = '/tmp/i2b2_clinical_rel_dataset.csv'
        # import pandas as pd
        # df =pd.read_csv(p)
        #
        # # res = nlu.load('toxic',verbose=True).predict(" I LOCVE PEANUT BUTTEr. AND YELLY. AND FUCK YOU BITCH OK !@:!?!??!?!", output_level='document')
        # res =  nlu.load('en.classify.questions').predict('How expensive is the Watch? Whats the fastest way to Berlin?',output_level='sentence')
        # print(res.columns)
        # for c in res.columns : print(res[c])
        #
        # pipe = nlu.load('en.embed_sentence.biobert.pubmed_pmc_base_cased')
        model_path ='/home/ckl/Documents/freelance/jsl/nlu/nlu4realgit/tmp/dump/saved_model_testbug'
        # pipe.save(model_path, overwrite=True)
        loaded_pipe = nlu.load(request ='en.embed_sentence.biobert.pubmed_pmc_base_cased', path=model_path,verbose=True)
        res = loaded_pipe.predict('random text', output_level='sentence',multithread=False)
        for c in res.columns:  print(res[c])


    def test_pos_train_bug(self):

        import nlu
        # load a trainable pipeline by specifying the train. prefix  and fit it on a datset with label and text columns
        # Since there are no
        train_path = '/home/ckl/Documents/freelance/jsl/nlu/nlu4realgit/UD_French-GSD_2.3.txt'
        trainable_pipe = nlu.load('train.pos')
        fitted_pipe = trainable_pipe.fit(dataset_path=train_path)

        # predict with the trainable pipeline on dataset and get predictions
        preds = fitted_pipe.predict('Donald Trump and Angela Merkel dont share many oppinions')
        preds

def test_cyber_model(self):
        import pandas as pd
        pipe = nlu.load('sentiment',verbose=True)
        df = pipe.predict(['Peter love pancaces. I hate Mondays', 'I love Fridays'], output_level='token',drop_irrelevant_cols=False, metadata=True, )
        for c in df.columns: print(df[c])

if __name__ == '__main__':
    unittest.main()

