from numpy import argsort

class CamelCards:

    hand_types = {
        "Five of a kind": 7, #AAAAA
        "Four of a kind": 6, #AA8AA
        "Full house": 5, #23332
        "Three of a kind": 4, #TTT98
        "Two pair": 3, #23432
        "One pair": 2, #A23A4
        "High card": 1 #23456
    }

    cards_strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    cards_strength_with_joker = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

    def get_total_winnings(hands_report, with_jokers=False):

        hands, bids = zip(*map(lambda m: (m[0], int(m[1])), [line.split() for line in hands_report.split('\n')]))
        hands_types = [CamelCards.get_hand_type(hand, with_jokers) for hand in hands]

        # Hand indices ordered by rank
        hand_index_rank_ordered = list(argsort(hands_types))[::-1]
        # For each type from the hands, reorder duplicates
        for hand_type in set(hands_types):
            # Indices for hands with current type in the rank list
            rank_type_indexes = [rank_index for rank_index, hand_index in enumerate(hand_index_rank_ordered) if hands_types[hand_index] == hand_type]
            if len(rank_type_indexes) > 1:
                start = rank_type_indexes[0]
                end = rank_type_indexes[-1] + 1
                hands_untie = [hands[hand_index] for hand_index in hand_index_rank_ordered[start:end]]

                new_order = [hand_index_rank_ordered[start+new_order_index] for new_order_index in CamelCards.untie_hands(hands_untie, return_index=True, with_jokers=with_jokers)]
                hand_index_rank_ordered[start:end] = new_order
                
        return sum([bids[index_hand]*(len(hands)-rank) for rank, index_hand in enumerate(hand_index_rank_ordered)])
        
    def get_hand_type(hand: str, with_jokers=False) -> int:

        cards, occurences = zip(*[ (card, len([1 for card_ in hand if card_==card])) for card in set(list(hand)) ])
        cards = list(cards)
        occurences = list(occurences)

        if with_jokers and 'J' in cards and len(cards) > 1:
            joker_index = cards.index('J')
            jokers_count = occurences[joker_index]
            occurences.pop(joker_index)
            # add the counts of jokers to the card with must occurences
            occurences[occurences.index(max(occurences))] += jokers_count

            cards.pop(joker_index)

        if len(cards) == 1:
            return CamelCards.hand_types['Five of a kind']
        if len(cards) == 2:
            if 4 in occurences:
                return CamelCards.hand_types['Four of a kind']
            return CamelCards.hand_types['Full house']
        if len(cards) == 3:
            if 3 in occurences:
                return CamelCards.hand_types['Three of a kind']
            return CamelCards.hand_types['Two pair']
        if len(cards) == 4:
            return CamelCards.hand_types['One pair']
        return CamelCards.hand_types['High card']
    
    def untie_hands(hands: list, return_index=False, with_jokers=False) -> list:
        
        strength = CamelCards.cards_strength_with_joker if with_jokers else CamelCards.cards_strength
        hands_sorted = sorted(hands, key=lambda hand: [strength.index(card) for card in hand])
        if return_index:
            return [hands.index(hand) for hand in hands_sorted]
        return hands_sorted
