from vgram import VGramTokenizer


def learn_big_dict():
    data_dir = "/Users/aleksandr.khvorov/jb/grazie/grazie-datasets/data/"
    # files = [data_dir + "stardust/all-texts.txt"]
    files = [data_dir + "openwebtext-parts-100/0.txt"]

    size = 20000
    tokenizer = VGramTokenizer(size, words_level=True, verbose=True)
    tokenizer.train(files, iters=1)
    encoded_seq = tokenizer.encode("hello world")
    print(encoded_seq)
    decoded = tokenizer.decode(encoded_seq)
    assert decoded == "hello world"
    print([tokenizer.decode([i]) for i in tokenizer.encode("fix bug")])
    print([tokenizer.coder.decode(i) for i in tokenizer.get_vocab()[:10]])

    tokenizer.save_pretrained(f"../saved/{size // 1000}k_owta_0.json")


if __name__ == '__main__':
    learn_big_dict()
