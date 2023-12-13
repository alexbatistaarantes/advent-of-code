from re import finditer, MULTILINE
from functools import reduce

class GearRatios:
    
    def get_part_numbers_sum(schematic):
        
        symbols = GearRatios.parse_schematic(schematic)['symbols']

        part_numbers_sum = 0
        for symbol in symbols:
            part_numbers_sum += sum([number for number in symbol['adjacents']])

        return part_numbers_sum
        # OBS: The way it is, a number is count more than once, if it happens to be adjacent to more than one symbol

    def get_gear_ratio_sum(schematic):

        symbols = GearRatios.parse_schematic(schematic)['symbols']

        gear_ratio_sum = 0
        for gear in [symbol for symbol in symbols if symbol['value'] == '*' and len(symbol['adjacents']) >= 2]:
            gear_ratio_sum += reduce(lambda x, y: x*y, gear['adjacents'])

        return gear_ratio_sum

    def parse_schematic(schematic):

        # Width and Height of the schematic
        width = list(finditer("[\n$]", schematic))[0].span()[0]
        height = len(list(finditer("^.+", schematic, flags=MULTILINE)))
        
        # list of numbers (value and span in columns), splitted by line (one list for each line, in order)
        numbers = []
        # list of symbols (value, row, col, list of adjacent numbers' value)
        symbols = []
        for row, line in enumerate(schematic.split('\n')):
            numbers.append([{'value': int(number.group(0)), 'span': number.span()} for number in list( finditer("\d+", line) )])
            symbols += [{'value': symbol.group(0), 'row': row, 'col': symbol.span()[0], 'adjacents': []} for symbol in list( finditer("[^\d\.]", line) )]

        # For each symbol, will check which numbers are adjacent to it
        for symbol in symbols:
            min_row = max(symbol['row']-1, 0)
            max_row = min(symbol['row']+1, height)
            min_col = max(symbol['col']-1, 0)
            max_col = min(symbol['col']+1, width)

            # Iterate from previous to next row
            for row in range(min_row, max_row+1):
                # Iterate through numbers in current row
                for number in numbers[row]:
                    # Checks if either the beggining or the ending of the number range is in the adjacent area of the symbol
                    if min_col <= number['span'][0] <= max_col or min_col <= number['span'][1]-1 <= max_col:
                        symbol['adjacents'].append(number['value'])

        return {
            'width': width,
            'height': height,
            'numbers': numbers,
            'symbols': symbols
        }
