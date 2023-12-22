
class MirageMaintenance():

    def get_extrapolated_values_sum(report, backwards=False):
        
        extrapolated_values_sum = 0
        for nums in [[int(num) for num in line.split(' ')] for line in report.split('\n')]:
            if backwards:
                diffs = MirageMaintenance.get_backwards_when_all_zeros(nums)
                extrapolated = 0
                for diff in diffs:
                    extrapolated = diff - extrapolated
                extrapolated_values_sum += extrapolated
            else:
                extrapolated_values_sum += sum(MirageMaintenance.get_last_column(nums))
        return extrapolated_values_sum
    
    def get_last_column(numbers: list[int]) -> list[int]:
        # although i don't doubt that there is a better way to accomplish what i was trying to do here, i didn't wanted
        # to settle with a solution where i just get every diff from every layer
        # here i did to get only the values necessary, until the first zero was found
        # that why it's so huge

        layers = [numbers]
        
        layer = 0
        while len(layers[-1]) == 0 or layers[-1][-1] != 0:
            # if next layer doesn't exist yet, create it
            if (len(layers)-1) < layer+1:
                layers.append([])
            
            # defines the index of number that we'll be getting the difference
            index_current_last = len(layers[layer]) - (len(layers[layer+1]) + 1)
            if index_current_last > 0:
              diff = layers[layer][index_current_last] - layers[layer][index_current_last-1]
              # add the difference to the beginning of next layer
              layers[layer+1].insert(0, diff)
            else:
              layer -= 1

            if 0 < len(layers[layer+1]) == (len(layers[layer]) - 1 - (index_current_last - 1)):
                layer += 1
            
        return [layer[-1] for layer in layers]

    def get_backwards_when_all_zeros(numbers: list[int]) -> list[int]:
        """ got lazy and didn't want to change the other function to handle both cases """
        # and still missed one case of my input by a difference of 1 of the correct answer

        layers = [numbers]
        
        while sum(layers[-1]):
            layers.append([])
            for i in range(0, len(layers[-2])-1):
                layers[-1].append(layers[-2][i+1] - layers[-2][i])
        
        return [layer[0] for layer in layers]

entries_txt = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

#r = MirageMaintenance.get_extrapolated_values_sum(entries_txt)
#r = MirageMaintenance.get_backwards_when_all_zeros([int(num) for num in entries_txt.split('\n')[2].split(' ')])

#print(r)
