from unittest import TestCase

from pycompass.ontology_node import OntologyNode
from pycompass.biological_feature import BiologicalFeature
from pycompass.experiment import Experiment
from pycompass.ontology import Ontology
from pycompass.platform import Platform
from pycompass.plot import Plot
from pycompass.sample import Sample
from pycompass.sample_set import SampleSet


class TestCompendium(TestCase):

    def test_all(self):
        from pycompass import Compendium, Connect, BiologicalFeature, Module, SampleSet, Plot, Annotation, Experiment, Sample, Platform, Ontology, Sparql
        connect = Connect('http://fempc0734:8080/graphql')
        compendium = connect.get_compendium('vespucci')

        gene_names = ['VIT_00s0246g00220', 'VIT_00s0332g00060', 'VIT_00s0332g00110', 'VIT_00s0332g00160',
                      'VIT_00s0396g00010', 'VIT_00s0505g00030', 'VIT_00s0505g00060', 'VIT_00s0873g00020',
                      'VIT_00s0904g00010']
        bf = BiologicalFeature.using(compendium).get(filter={'name_In': gene_names})

        alias = []
        for n in ['B9S8R7', 'Q7M2G6', 'D7SZ93', 'B8XIJ8', 'Vv00s0125g00280', 'Vv00s0187g00140', 'Vv00s0246g00010',
                  'Vv00s0246g00080', 'Vv00s0438g00020', 'Vv00s0246g00200']:
            alias.append("{{?s <http://purl.obolibrary.org/obo/NCIT_C41095> '{n}'}}".format(n=n))
        sparql = 'SELECT ?s ?p ?o WHERE {{ {alias} }}'.format(alias=' UNION '.join(alias))

        for _bf in BiologicalFeature.using(compendium).by(sparql=sparql):
            bf.append(_bf)

        module_1 = Module.using(compendium).create(biofeatures=bf)

        print(module_1.sample_sets[0].short_annotation_description)
        #desc = module_1.get_enrichment()
        #print(desc)

        #OntologyNode.using(compendium).get(filter={''})



