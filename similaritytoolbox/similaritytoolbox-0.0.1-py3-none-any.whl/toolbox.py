import pandas as pd
import numpy as np
from transformers import BertModel, BertConfig
import torch, gc, os
from transformers import AutoTokenizer
import re
import pickle
import faiss
import json
import os


class SimilarityToolbox():
    
    def __init__(self):
        device = torch.device("cuda")
        cuda_available = torch.cuda.is_available()
        model_name = 'Contrastive-Tension/BERT-Base-Swe-CT-STSb'
        #model_name = "Contrastive-Tension/RoBerta-Large-CT-STSb"
        #model_name = "Contrastive-Tension/BERT-Large-CT-STSb"
        tokenizer = AutoTokenizer.from_pretrained(model_name, do_lower_case=False,  model_max_length=512)
        model = BertModel.from_pretrained(model_name)
        model.eval()
        model.half()
        model.to(device)
        self.model = model
        self.tokenizer = tokenizer
        
        dim = 768
        res = faiss.StandardGpuResources()
        index_flat = faiss.IndexFlatL2(dim)
        gpu_index_flat = faiss.index_cpu_to_gpu(res, 0, index_flat) 
        gpu_index_flat.reset()

        self.vector_to_faiss = np.array([])
        
        self.gpu_index_flat = gpu_index_flat
        self.device = device
        
        self.local_sentences =  []
        self.model = model
    
    def get_sentence_vector_p(self,sentence):
        inputs = self.tokenizer(sentence, padding=True, return_tensors="pt", truncation=True).to(self.device)
        output = self.model(**inputs, output_hidden_states=False).last_hidden_state
        vector = self.masked_mean_pooling(output, inputs.attention_mask).astype(np.float32)
        return vector
    

   
    # Pooling
    def masked_mean_pooling(self,embs, mask):
        f = lambda x: np.array(x.cpu().detach())

        embs, mask = f(embs), f(mask)
        # Solve potential Padding issues. This can be removed if sufficient precautions are taken
        if (embs.shape[1] > mask.shape[1]):
            mask = np.concatenate(
                [mask, np.zeros((embs.shape[0], embs.shape[1] - mask.shape[1]))], axis=1)
        if (embs.shape[1] < mask.shape[1]):
            mask = mask[:, :embs.shape[1]]

        # Mask the output before calculating the final sentence embedding by taking the mean
        maskedEmbs = embs * np.expand_dims(mask, axis=-1)
        summedEmbs = np.sum(maskedEmbs, axis=1)
        lengths = np.sum(mask, axis=-1, keepdims=True)
        return summedEmbs / lengths
    
    
    def add_sentence(self,sentence):
        sentence = [sentence]
        mean_vector = self.get_sentence_vector_p(sentence)
        self.local_sentences.append(sentence)
    
        if len(self.vector_to_faiss) == 0: self.vector_to_faiss = mean_vector
        else:self.vector_to_faiss = np.vstack([self.vector_to_faiss, mean_vector])
    
    
    
    # Custom tokenizer?    
       
       
    def search_by_query(self,query_vector, nb_similar, gpu_index_flat):
        D,I = gpu_index_flat.search(query_vector, nb_similar)
        return I[0],D[0]
    
    def get_similar(self,sentence,limit=15):
        ''' Similar by index'''
        print(len(self.local_sentences))
        
        if not self.local_sentences:
            return ([],[])
        
        # TODO: Not great
        self.fix_faiss()
        sentence =[sentence]
        print(sentence)
        query_sentences = sentence

        print(query_sentences)
        query_vector = query_sentences
     
        query_vector = self.get_sentence_vector_p(query_vector)
        
        return self.search_by_query(query_vector, limit, self.gpu_index_flat)

    def get_similar_text(self,sentence,limit=15,distance=100):
        ''' json friendly ''' 

        similar_idx, relation = self.get_similar(sentence,limit)
        print("-----------")
        results = []
        for i, x in enumerate(similar_idx):    
            #print(str(int(relation[i]))+" "+str(self.local_sentences[x]))
            if(int(relation[i])<=distance):
                res = {
                    "distance": int(relation[i]),
                    "text": self.local_sentences[x]
                }
                results.append(res)

        return results


    def print_similar(self,sentence,limit=15):
        similar_idx, relation = self.get_similar(sentence,limit)
        print("-----------")

        for i, x in enumerate(similar_idx):    
            print(str(int(relation[i]))+" "+str(self.local_sentences[x]))

    
    # TODO: NOT OPTIMAL
    def fix_faiss(self):
        # Do not add every time
        self.gpu_index_flat.reset()
        self.gpu_index_flat.add(self.vector_to_faiss.astype(np.float32)) 
    
    def save(self,folder_path):
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        #with open(folder_path+'/sentences.json', 'w') as filehandle:
        #    json.dump(self.local_sentences, filehandle)
    
        with open(folder_path+'/sentences.json', 'w', encoding ='utf8') as json_file:
            json.dump(self.local_sentences, json_file, ensure_ascii = False)
    
        # Sentences (Lookup elsewhere?) - Sentence repo? change name
        # Index
        # Model must match as well
        
        #faiss.write_index(index, filename)
        #from numpy import asarray
        #from numpy import save
        
        # save to npy file
        np.save(folder_path+'/sentences_to_index.npy', self.vector_to_faiss)
    
    def load(self,folder_path):
        with open(folder_path+"/sentences.json",encoding ='utf8') as json_file:
            self.local_sentences = json.load(json_file)
        # Id => String
        # index
        self.vector_to_faiss = np.load(folder_path+'/sentences_to_index.npy')
    
    def get_sentences(self):
        return self.local_sentences
    
    # TODO: Load whole pandas (As examples)    