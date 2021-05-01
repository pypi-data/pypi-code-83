import logging
import numpy as np

def get_embeddings_for_tokens(dataset, cdb, context_type='medium', special_tokens=['<PAD>', '<START>']):
    r''' Given a stream of tokens get the embeddings from MedCAT and make the required maps.

    Args:
        dataset
        cdb
        context_type
        special_tokens

    Returns:
        embeddings
        tkn2id
        id2tkn
    '''
    embeddings = []
    tkn2id = {}
    id2tkn = {}
    for tkns in dataset['stream']:
        for tkn in tkns:
            tkn = str(tkn)
            if tkn not in tkn2id:
                if tkn in cdb.cui2context_vectors and context_type in cdb.cui2context_vectors[tkn]:
                    vec = cdb.cui2context_vectors[tkn][context_type]
                else:
                    logging.info("Token not in CDB: " + tkn)
                    vec = np.random.rand(300)

                id2tkn[len(embeddings)] = tkn
                tkn2id[tkn] = len(embeddings)
                embeddings.append(vec)

    # Add special tokens
    for tkn in special_tokens:
        id2tkn[len(embeddings)] = tkn
        tkn2id[tkn] = len(embeddings)
        if tkn != '<PAD>':
            embeddings.append(np.random.rand(len(embeddings[0])))
        else:
            embeddings.append(np.zeros(len(embeddings[0])))

    return embeddings, tkn2id, id2tkn
