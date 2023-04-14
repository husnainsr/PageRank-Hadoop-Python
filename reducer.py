#!/usr/bin/env python3
import sys
from driver import *

# Read input from stdin
def read_input(file):
    for line in file:
        yield line.strip().split("\t")

# Write output to file
def write_to_file(text, filename):
    with open(filename, "w") as f:
        for line in text.splitlines():
            f.write(line + "\n")

# Main function
def main():
    check_hops=get_sourceNode()
    source_nodes=set(check_hops[1:4]) #getting my source nodes 
    source_nodes = [str(num) for num in source_nodes] 
    input_lines = read_input(sys.stdin)
    new_nodes=[]
    if check_hops[0]<=3:
        for i in check_hops:
            new_nodes.append(i)
        final_output_path=""
        for line in input_lines:
            node, pagerank, out_nodes = line
            node, pagerank = node.strip(), float(pagerank)
            out_nodes = list(map(int, out_nodes.split(',')))
            for i in out_nodes:
                new_nodes.append(i)
            output_str=(f"{node}\t{pagerank}\t{','.join(map(str, out_nodes))}")
            final_output_path+=output_str+"\n"
            # print(f"{node}\t{pagerank}\t{','.join(map(str, out_nodes))}")
        hops_increase=int(new_nodes[0])
        hops_increase+=1
        new_nodes[0]=hops_increase   
        text = '\n'.join(map(str, new_nodes))
        write_to_file(text,"sourceNodes.txt")
        write_to_file(final_output_path, "updated_input.txt")
    else:
        damping_factor = 0.85        # Damping factor
        node_contributions = {}      # Node contributions
        out_nodes_dict = {}          # Outgoing nodes dictionary
        damping_factor = 0.85    # Damping factor
        total_nodes=set()
    # Process each input line
        for line in input_lines:
            node, pagerank, out_nodes = line
            node, pagerank = node.strip(), float(pagerank)
            out_nodes = list(map(str, out_nodes.split(',')))
            total_nodes.add(node)        #this will help keep track of total nodes and acessing them 
            
            out_nodes_dict[node] = out_nodes
            for out_node in out_nodes:
                if out_node not in node_contributions:
                    node_contributions[out_node] = 0.0
                node_contributions[out_node] += pagerank / len(out_nodes)
                
            # Reset the initial PageRank values for source nodes in the node_contributions dictionary
        values_output=""
        output_string=""
        for node, contributions in node_contributions.items():
            pagerank = (1 - damping_factor) / len(total_nodes) + damping_factor * contributions
            out_nodes = out_nodes_dict.get(node, [])

            
            out_nodes_str = ','.join(map(str, out_nodes))
            output_line = f"{node}\t{pagerank:.10f}\t{out_nodes_str}"
            output_string += output_line + "\n"
            
            rank_output = f"{pagerank:.10f}\t{node}"    
            values_output += rank_output + "\n"

        write_to_file(output_string, "updated_input.txt")
        write_to_file(values_output, "output.txt")





if __name__ == "__main__":
    main()
