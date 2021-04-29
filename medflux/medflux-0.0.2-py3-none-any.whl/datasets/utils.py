def tokens_to_ids(examples, token2id, name='stream'):
    r''' Convert tokens to ids, used as a map function in the datasets module from HF.

    Args:
        examples (
        token2id (`Dict[str, int]`, `required`):
            Map from tokens to ids.
        name (`str`, `optional`, defaults to `stream`):
            What `key` in examples contains the data that has to be converted.
    '''
    examples[name] = [[token2id[tkn] for tkn in example] for example in examples[name]]

    return examples


def stream_to_separate_examples(examples):
    r''' Convert a stream to separate examples that can be used to train
    a next concept predictor unable to handle sequences. Use with HF datasets map function.

    '''
    out = {}
    out['input_ids'] = [example[0:i+1] for example in examples['stream'] for i in range(len(example) - 1)]
    out['labels'] = [example[i+1] for example in examples['stream'] for i in range(len(example) - 1)]

    return out


def filter_by_count(dataset, min_count=5, min_length=5):
    r''' Filters tokens of a dataset and leaves only the ones with frequencey >= min_count

    Args:
        dataset
        min_count
        min_length:
            Examples below will be removed, in other words patients with less than min_length concepts
    '''
    token_cnt = {}
    for stream in dataset['stream']:
        for tkn in stream:
            token_cnt[tkn] = token_cnt.get(tkn, 0) + 1

    dataset = dataset.map(function=lambda example: {'stream': [token for token in example['stream'] if token_cnt[token] >= min_count]},
                      load_from_cache_file=False)

    if min_length > 0:
        dataset = dataset.filter(function=lambda example: len(example['stream']) >=  min_length)

    return dataset
