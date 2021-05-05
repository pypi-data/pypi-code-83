class SimpleMapTokenizer(object):
    r''' Not even really a tokenizer, will take a list of tokens and
    covert them to IDs

    Args:
        tkn2id
        pad_id
        max_len
        start_id:
            If set it will be prepended to each input example
    '''
    def __init__(self, tkn2id, pad_id, max_len=50, start_id=None):
        self.tkn2id = tkn2id
        self.pad_id = pad_id
        self.max_len = max_len
        self.start_id = start_id


    def tokens_to_ids(self, tokens):
        out = [self.tkn2id[tkn] for tkn in tokens]
        if self.start_id is not None:
            out = [self.start_id] + out
        out = out[:self.max_len]

        return out


    def encode(self, examples):
        examples['input_ids'] = [self.tokens_to_ids(stream[:-1]) for stream in examples['stream']]

        return examples
