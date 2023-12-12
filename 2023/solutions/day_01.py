from re import findall, sub, MULTILINE

class Trebuchet:

    def get_calibration_from_document(document: str) -> int:

        firsts = findall(r"\D*(\d).*$", document, flags=MULTILINE)
        lasts = findall(r".*(\d)\D*$", document, flags=MULTILINE)
        
        # ∑ first digit * 10 + last digit
        calibration = sum([ int(num)*10 for num in firsts ]) + sum([ int(num) for num in lasts ])
        
        return calibration

    def get_calibration_from_document_with_spelled_numbers(document: str) -> int:

        # oneight should become 18
        # this way it becomes 1on8eight in the string since I couldn't find any other way
        document = sub("(?=(one|two|three|four|five|six|seven|eight|nine))", lambda m: Trebuchet.replace_written_number(m.group(1)), document, flags=MULTILINE)
        
        return Trebuchet.get_calibration_from_document(document)

    def replace_written_number(written_number: str) -> int:
        
        text_number_map = {text: number+1 for number, text in enumerate("one two three four five six seven eight nine".split(' '))}
        
        return str( text_number_map[written_number] )
