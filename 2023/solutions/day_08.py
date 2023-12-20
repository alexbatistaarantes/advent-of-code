from re import findall
from math import lcm

class HauntedWasteland():

    def get_steps_count(network):
        
        # instructions is a list of indices which should be accessed in the node (Right is 1, Left is 0)
        instructions, nodes_paths = HauntedWasteland.parse_network(network)
        instructions_count = len(instructions)

        node = "AAA"
        steps = 0
        while True:
            next_step_index = steps % instructions_count
            next_instruction = instructions[next_step_index]
            node = nodes_paths[node][next_instruction]
            steps += 1
            
            if node == "ZZZ":
                break
            
        return steps

    def get_ghost_steps_count(network):

        # instructions is a list of indices which should be accessed in the node (Right is 1, Left is 0)
        instructions, nodes_paths = HauntedWasteland.parse_network(network)
        instructions_count = len(instructions)

        nodes = [node for node in nodes_paths if node[-1] == "A"]
        step_counts_until_z = []
        steps = 0
        while len(nodes) > 0:
            next_instruction = instructions[steps % instructions_count]
            steps += 1
            
            index = 0
            while index < len(nodes):
                node = nodes[index]
                nodes[index] = nodes_paths[node][next_instruction]
                
                if nodes[index][-1] == 'Z':
                    step_counts_until_z.append(steps)
                    nodes.pop(index)
                    index -= 1
                index += 1
            
        return lcm(*step_counts_until_z)

    def parse_network(network):

        network = network.split('\n')
        instructions = [int(index) for index in list(network[0].replace('R', '1').replace('L', '0'))]
        nodes_paths = {match[0]: (match[1], match[2]) for match in [findall(r"(\w+) = \((\w+), (\w+)\)", line)[0] for line in network[2:]]}
        
        return instructions, nodes_paths
