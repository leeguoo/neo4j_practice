import pandas as pd
from py2neo import Graph
from py2neo import Node, Relationship

with open("/home/ubuntu/.neo4j_info/key","r") as f:
    passwd = f.readline()[:-1]

df = pd.read_csv("../data/nodes.csv")

#graph = Graph(password=passwd)
#
#graph.run("CREATE INDEX ON :Product(asin)")
#
#cmd ="""
#LOAD CSV WITH HEADERS FROM "file:///nodes.csv" AS line
#WITH line
#MERGE (n:Product {asin:line.asin, title:line.title, price:line.price, brand:line.brand, description:line.description, imUrl:line.imUrl})
#"""
#
#graph.run(cmd)
