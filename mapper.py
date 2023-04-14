#!/usr/bin/env python3
from driver import *
import sys
updated_input=get_updatedInput()

source_node=get_sourceNode()
source_node = [str(num) for num in source_node] 
hops_defined=source_node[0] #number of hops to run 
source_node=source_node[1:] #saving all the out nodes of the starting nodes
three_sourceNode=source_node[0:3] #saving all the starting nodes
source_node=set(source_node)
lenght_source=len(three_sourceNode)
not_node='0.0'
total_nodes=6
dangling_nodes = set(range(1, total_nodes + 1))   # Dangling nodes

# Initializing the variables to hold current and previous nodes
current_node = None
prev_node = None
adj_list = set()
if hops_defined<='2':
    for line in sys.stdin:
        line = line.strip()
        if line[0]!='#':
            node, out_node = line.split()
            if node in source_node: #getting only source nodes only
                # If the node has changed, emit the previous node and its adjacency list
                if current_node != node and prev_node is not None:
                    if prev_node in three_sourceNode:
                        print(f"{prev_node}\t{1/lenght_source}\t{','.join(sorted(adj_list))}")
                    else:
                        print(f"{prev_node}\t{not_node}\t{','.join(sorted(adj_list))}")

                    adj_list = set()
                adj_list.add(out_node)        
                current_node = node
                prev_node = current_node
        #Emit the last node
    if current_node == prev_node:
        if prev_node in three_sourceNode:
            print(f"{prev_node}\t{1/lenght_source}\t{','.join(sorted(adj_list))}")
        else:
            print(f"{prev_node}\t{not_node}\t{','.join(sorted(adj_list))}")
else:
    all_node=set() #this will keep track of all nodes and outnode
    only_node=set() #this will keep track of only node
    for line in updated_input:
        node,page_rank,out_nodes=line.split('\t')
        print(f"{node}\t{page_rank}\t{out_nodes}")
        out_nodes = list(map(str, out_nodes.split(','))) 
        only_node.add(node) #adding only key node
        all_node.add(node)  
        for i in out_nodes:
            all_node.add(i)
    all_node=all_node.difference(only_node)
    for i in all_node:
        print(f"{i}\t{0.0}\t{','.join(sorted(three_sourceNode ))}")


