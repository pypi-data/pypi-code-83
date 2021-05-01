import elasticsearch


def make(url):
    return elasticsearch.Elasticsearch(url)
