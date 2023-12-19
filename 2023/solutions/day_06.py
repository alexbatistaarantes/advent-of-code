from re import findall, MULTILINE

class WaitForIt:
    
    def get_product_of_number_of_ways_to_beat_record(sheet):

        time = [int(time) for time in findall(r"\d+", sheet.split('\n')[0])]
        record_distances = [int(distance) for distance in findall(r"\d+", sheet.split('\n')[1])]

        product_number_of_ways = 1
        for race, time in enumerate(time):
            record = record_distances[race]
            number_of_ways = WaitForIt.get_number_of_ways_to_beat_record(time, record)
            product_number_of_ways *= number_of_ways
        
        return product_number_of_ways

    def get_number_of_ways_to_beat_record_from_sheet(sheet):

        time, record = map(lambda m: int(m.replace(' ', '')), findall(r"((?:\d+ *)+)", sheet, flags=MULTILINE))
        return WaitForIt.get_number_of_ways_to_beat_record(time, record)

    def get_number_of_ways_to_beat_record(time, record):
        return len([1 for time_holding in range(1, time) if (time-time_holding)*time_holding > record])

