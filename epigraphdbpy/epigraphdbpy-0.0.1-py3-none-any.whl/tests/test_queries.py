#!/usr/local/bin/python3
import epigraphdbpy


def test_geneToProtein():
    data1 = epigraphdbpy.geneToProtein(["IGF2", "IGF1"], fulldata="false")
    metadata, data2 = epigraphdbpy.geneToProtein(["IGF2", "IGF1"], fulldata="true")
    assert data1[0][2] == "P01344"
    assert data2[1]["protein"]["uniprot_id"] == "P05019"
