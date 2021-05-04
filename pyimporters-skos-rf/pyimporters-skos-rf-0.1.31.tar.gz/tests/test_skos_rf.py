from pathlib import Path

from progress.bar import Bar
from pyimporters_plugins.base import Term

from pyimporters_skos_rf.skos_rf import SKOSRFKnowledgeParser, SKOSRFOptionsModel, RDFFormat


def test_xml():
    testdir = Path(__file__).parent
    source = Path(testdir, 'data/LL-RF_TerminoPayeFull_20210409.zip')
    parser = SKOSRFKnowledgeParser()
    options = SKOSRFOptionsModel(lang="fr", rdf_format=RDFFormat.xml)
    concepts = list(parser.parse(source, options.dict(), Bar('Processing')))
    assert len(concepts) == 1808
    homme = next(c for c in concepts if
                 c.identifier == 'https://revuefiduciaire.grouperf.com/referentiel/concept/thesaurus-paye#homme')
    assert homme.identifier == 'https://revuefiduciaire.grouperf.com/referentiel/concept/thesaurus-paye#homme'
    assert homme.preferredForm == 'Homme'
    assert len(homme.properties['altForms']) == 1
    assert homme.properties['altForms'] == ['hommes']


def test_standard_skosxml():
    testdir = Path(__file__).parent
    source = Path(testdir, 'data/lexicon.skos.rdf.zip')
    parser = SKOSRFKnowledgeParser()
    options = SKOSRFOptionsModel(lang="fr", rdf_format=RDFFormat.xml)
    concepts = list(parser.parse(source, options.dict(), Bar('Processing')))
    assert len(concepts) == 1
    c0: Term = concepts[0]
    assert c0.identifier == 'http://skos.um.es/unescothes/C02796'
    assert c0.preferredForm == 'Métier'
    assert len(c0.properties['altForms']) == 5
    assert set(c0.properties['altForms']) == {'Carrière', 'Occupation professionnelle', 'Profession',
                                              'Activité professionnelle', 'Poste'}
