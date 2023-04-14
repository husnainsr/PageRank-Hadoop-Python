def get_updatedInput():
	out_nodes_list = set()
	with open('/home/hustle/A3/lastTry/updated_input.txt') as f:
		lines = f.readlines()
		for i in lines:
			i = i.strip()
			out_nodes_list.add(i)
		
	return out_nodes_list


def get_sourceNode():
	out_nodes_list = []
	with open('/home/hustle/A3/lastTry/sourceNodes.txt') as f:
		lines = f.readlines()
		for i in lines:
			i = i.strip()
			out_nodes_list.append(int(i))
		
	return out_nodes_list