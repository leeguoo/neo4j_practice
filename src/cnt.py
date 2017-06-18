from py2neo import Graph
from py2neo import Node, Relationship

with open("/home/ubuntu/.neo4j_info/key","r") as f:
    passwd = f.readline()[:-1]

graph = Graph(password=passwd)

import time
from py2neo import NodeSelector

#print(graph.run("MATCH (n:Product) return count(n);").dump())
#print(graph.run("MATCH (n:Product) return count(n);").dump())
print(graph.run("MATCH (:Product)-[n:ALSO_VIEWED]->(:Product) return count(n);").dump())

#from py2neo import NodeSelection
#
#selection = NodeSelection(graph)
#print(selection.first())

#cmd = """
#MATCH (node:Product)-[r:ALSO_VIEWED]->() 
#WHERE node.asin='0974671517' 
#RETURN count(r)
#"""
#
#print(graph.run(cmd).dump())
#
#cmd = """
#MATCH ()-[r:ALSO_VIEWED]->(node:Product) 
#WHERE node.asin='0974671517' 
#RETURN count(r)
#"""
#
#print(graph.run(cmd).dump())

#cmd = """
#MATCH (node:Product)
#WHERE exists(node.price)
#RETURN count(node)
#"""
#
#print(graph.run(cmd).dump())

#cmd = """
#MATCH (node:Product)
#WHERE node.description CONTAINS "stroller"
#RETURN count(node)
#"""
#
#print(graph.run(cmd).dump())
