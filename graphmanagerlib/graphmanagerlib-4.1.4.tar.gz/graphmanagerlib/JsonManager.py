import json
from graphmanagerlib.Node import Node
from graphmanagerlib.Document import Document

def GetJsonFromFile(jsonPath):
    with open(jsonPath, encoding="utf-8-sig") as file:
        reader = json.load(file)
        return reader

def ConvertJsonToDocumentsObjects(json):
    listOfDocuments = []
    for i in json:
        width = i["Width"]
        height = i["Height"]
        nodes = i["Nodes"]
        listOfNodes = []
        for j in nodes:
            node = Node(XMin=j["XMin"], YMin=j["YMin"], XMax=j["XMax"], YMax=j["YMax"], Object= j["Object"], Tag=j["Tag"])
            listOfNodes.append(node)
        doc = Document(width=width, height=height, nodes=listOfNodes)
        listOfDocuments.append(doc)
    return listOfDocuments

def ConvertPredictionToJson(predictionTab):
    return json.dumps(predictionTab, separators=(',', ':'))