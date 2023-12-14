from re import *

class Scratchcards:

    def get_total_points(cards_report: str) -> int:
        
        cards = Scratchcards.parse_cards(cards_report)
        
        total_points = 0
        for card in cards.values():
            qtd_match = len(card['intersection'])
            total_points += pow(2, qtd_match-1) if qtd_match > 0 else 0

        return total_points

    def get_cards_count(cards_report: str) -> int:

        cards = Scratchcards.parse_cards(cards_report)

        cards_count = 0
        for id in list(cards.keys())[::-1]:
            
            cards_won = len(cards[id]['intersection'])
            # sum the quantity of cards won from the cards that this current card gives you
            cards_won += sum([cards[id_]['cards_won'] for id_ in range(id+1, min(id+cards_won+1, len(cards)))])

            cards[id]['cards_won'] = cards_won

            cards_count += 1 + cards_won
        
        return cards_count

    def parse_cards(cards_report: str) -> dict:

        cards_patterns = findall(r"Card +(\d+): {1,2}((?:\d+ *)+) \| {1,2}((?:\d+ *)+)", cards_report, flags=MULTILINE)
        
        # {1: {'winning': [1, 2, 3, 4], 'have': [3, 4, 5, 6]}, ...}
        cards = {int(card[0]): {'winning': set(split("\s+", card[1])), 'have': set(split("\s+", card[2]))} for card in cards_patterns}

        for card in cards.values():
            card['intersection'] = set.intersection(card['winning'], card['have'])
        
        return cards
