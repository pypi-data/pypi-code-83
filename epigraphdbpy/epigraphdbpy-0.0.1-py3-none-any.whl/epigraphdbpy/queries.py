"""Queries
"""
import os, json, requests
import epigraphdbpy.constants as cons
from retry import retry
from urllib.parse import urljoin

MAX_TRIES = 10
TRIES_DELAY = 5  # seconds
TRIES_BACKOFF = 2


@retry(tries=MAX_TRIES, delay=TRIES_DELAY, backoff=TRIES_BACKOFF)
def queryAPI(endpoint, query):
    """Run a query against the API, returning JSON response
    Parameters:
        endpoint: an endpoint path on the API
        query: a valid dictionary
    Returns:
        response: json response for query
    """
    path = endpoint
    url = urljoin(cons.url, path)
    response = requests.post(url, json=query)
    metadata = response.json()["metadata"]
    results = response.json()["results"]
    return (metadata, results)


def geneToProtein(
    gene_name_list=[], gene_id_list=[], by_gene_id="false", fulldata="false"
):
    """Retrieve Uniprot ID for a list of gene IDs
    Parameters:
        gene_name_list: list of HGNC identifiers
        gene_id_list: list of Ensembl gene identifiers
        by_gene_id: string boolean, false for HGNC identifiers, true for Ensembl
        fulldata: whether to return metadata and full results or just genes/proteins
    Returns:
        metadata: json object containing query
        data: json object containing gene identifiers and protein identifiers
        output: list of gene/protein combinations
    """
    path = "/mappings/gene-to-protein"
    query = {
        "gene_name_list": gene_name_list,
        "gene_id_list": gene_id_list,
        "by_gene_id": by_gene_id,
    }
    metadata, results = queryAPI(path, query)
    if fulldata == "true":
        return (metadata, results)
    else:
        output = []
        for gene in results:
            output.append(
                [
                    gene["gene"]["name"],
                    gene["gene"]["ensembl_id"],
                    gene["protein"]["uniprot_id"],
                ]
            )
        return output
