from py2neo import Graph
from py2neo import Node, Relationship

with open("/home/ubuntu/.neo4j_info/key","r") as f:
    passwd = f.readline()[:-1]

graph = Graph(password=passwd)

cmd = """
LOAD CSV WITH HEADERS FROM "file:///relationships.csv" AS line
WITH line
MATCH (a:Product),(b:Product)
WHERE a.asin = line.asin AND b.asin = line.also_viewed
MERGE (a)-[:ALSO_VIEWED]->(b)
"""

graph.run(cmd)
