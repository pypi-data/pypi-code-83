import torch
import numpy as np
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from transformers import (BertConfig, BertLMHeadModel, BertModel,
                          EncoderDecoderModel)


class PhonetizerModel:

    phon_tokenizer = {
        'e': 7, 'i': 8, 'R': 9,
        'a': 10, 'o': 11, 't': 12,
        's': 13, 'l': 14, 'k': 15,
        'p': 16, 'm': 17, 'n': 18,
        'd': 19, 'y': 20, '@': 21,
        'f': 22, 'z': 23, 'b': 24,
        '§': 25, 'v': 26, '2': 27,
        '1': 28, 'Z': 29, 'g': 30,
        'u': 31, 'S': 32}
    phon_untokenizer = {v: k for k, v in phon_tokenizer.items()}
    char_tokenizer = {
        'e': 7, 'i': 8, 'a': 9,
        'r': 10, 'o': 11, 's': 12,
        't': 13, 'n': 14, 'l': 15,
        'é': 16, 'c': 17, 'p': 18,
        'u': 19, 'm': 20, 'd': 21,
        '-': 22, 'h': 23, 'g': 24,
        'b': 25, 'v': 26, 'f': 27,
        'k': 28, 'y': 29, 'x': 30,
        'è': 31, 'ï': 32, 'j': 33,
        'z': 34, 'w': 35, 'q': 36}

    def __init__(self, device='cpu', model=None):
        vocabsize = 37
        max_length = 50
        encoder_config = BertConfig(
            vocab_size=vocabsize,
            max_position_embeddings=max_length+64,
            num_attention_heads=4,
            num_hidden_layers=4,
            hidden_size=128,
            type_vocab_size=1)
        encoder = BertModel(config=encoder_config)

        vocabsize = 33
        max_length = 50
        decoder_config = BertConfig(
            vocab_size=vocabsize,
            max_position_embeddings=max_length+64,
            num_attention_heads=4,
            num_hidden_layers=4,
            hidden_size=128,
            type_vocab_size=1,
            add_cross_attentions=True,
            is_decoder=True)
        decoder_config.add_cross_attention = True
        decoder = BertLMHeadModel(config=decoder_config)

        # Define encoder decoder model
        self.model = EncoderDecoderModel(encoder=encoder, decoder=decoder)
        self.model.to(device)
        self.device = device
        if model is not None:
            self.model.load_state_dict(torch.load(model))

    def phonetize(self, word):
        word = word.replace('à', 'a')
        word = word.replace('û', 'u')
        word = word.replace('ù', 'u')
        word = word.replace('î', 'i')
        word = word.replace('ç', 'ss')
        word = word.replace('ô', 'o')
        word = word.replace('â', 'a')
        word = word.replace('qu', 'k')
        word = word.replace('ê', 'e')
        assert set(word).issubset(set(PhonetizerModel.char_tokenizer.keys()))
        encoded = torch.tensor(
            [0] +
            [PhonetizerModel.char_tokenizer[p] for p in word] +
            [2]
        )
        output = self.model.generate(
            encoded.unsqueeze(0).to(self.device),
            max_length=50,
            decoder_start_token_id=0,
            eos_token_id=2,
            pad_token_id=1,
            ).detach().cpu().numpy()[0]
        bound = np.where(output == 2)[0][0] if 2 in output else 1000
        phon_pred = ''.join(
            [PhonetizerModel.phon_untokenizer[c]
             for c in output[:bound]
             if c > 6])
        return phon_pred

    def check_phonetization_error(self, word, phon):
        prediction = self.phonetize(word)[:5]
        score = pairwise2.align.globalms(
            list(phon[:5]), list(prediction),
            2, -1, -1, -.5,
            score_only=True, gap_char=['-']
        ) / len(phon[:5])
        return score
