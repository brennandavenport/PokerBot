from typing import List, Tuple, Dict

from collections import Counter

class ShowDown:
    """
    10 - Royal Flush
    9 - Straight Flush
    8 - Four of a Kind
    7 - Full House
    6 - Flush
    5 - Straight
    4 - Three of a Kind
    3 - Two Pair
    2 - One Pair
    1 - High Card
    """
    def __init__(self, community_cards: List[str]):
        self.community_cards = community_cards
        self.rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                    '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def format_cards(self, cards: List[str]) -> List[Tuple[str, str]]:
        all_cards = cards + self.community_cards

        result = []

        for card in all_cards:
            rank = card[:-1]
            suit = card[-1]
            result.append((rank, suit))

        return result

    def evaluate_hand(self, cards: List[str]) -> int:
        all_cards = self.format_cards(cards)

        # Group cards by suit
        suits = {}
        for rank, suit in all_cards:
            if suit not in suits:
                suits[suit] = []
            suits[suit].append(rank)

        self.suits = suits
        self.ranks = [rank for rank, _ in all_cards]
        

        hand_rankings = [
            (self._is_royal_flush, 10),
            (self._is_straight_flush, 9),
            (self._is_four_of_kind, 8),
            (self._is_full_house, 7),
            (self._is_flush, 6),
            (self._is_straight, 5),
            (self._is_three_of_kind, 4),
            (self._is_two_pair, 3),
            (self._is_one_pair, 2)
        ]
        
        for check_function, score in hand_rankings:
            if check_function(all_cards):
                return score

        return 1  # High card

    def _is_royal_flush(self, cards: List[Tuple[str, str]]) -> bool:
        # Check if any suit has the Royal Flush ranks
        royal_ranks = {'10', 'J', 'Q', 'K', 'A'}
        for suit_ranks in self.suits.values():
            if royal_ranks.issubset(set(suit_ranks)):
                return True
        
        return False
    
    def _is_straight_flush(self, cards: List[Tuple[str, str]]) -> bool:
        # Check for a straight flush in each suit
        for suit_ranks in self.suits.values():
            if len(suit_ranks) < 5:
                continue  # Not enough cards for a straight flush
            
            # Convert ranks to numbers and sort
            sorted_ranks = sorted(self.rank_values[rank] for rank in suit_ranks)
            
            # Check for a consecutive sequence
            for i in range(len(sorted_ranks) - 4):
                if sorted_ranks[i:i+5] == list(range(sorted_ranks[i], sorted_ranks[i] + 5)):
                    return True
            
            # Special case: Ace-low straight (A, 2, 3, 4, 5)
            if {14, 2, 3, 4, 5}.issubset(set(sorted_ranks)):
                return True

        return False

    def _is_four_of_kind(self, cards: List[Tuple[str, str]]) -> bool:
        rank_count  = Counter(self.ranks)

        return 4 in rank_count.values()

    def _is_full_house(self, cards: List[Tuple[str, str]]) -> bool:
        rank_count  = Counter(self.ranks)

        counts = sorted(rank_count.values(), reverse=True)

        return counts[:2] == [3, 2] or counts[:2] == [3, 3]

    def _is_flush(self, cards: List[Tuple[str, str]]) -> bool:
        # Extract the suits from the cards
        suits = [suit for _, suit in cards]
        
        # Count the occurrences of each suit
        suit_counts = Counter(suits)
        
        # A flush requires at least 5 cards of the same suit
        return any(count >= 5 for count in suit_counts.values())

    def _is_straight(self, cards: List[Tuple[str, str]]) -> bool:
        ranks = [rank for rank, suit in cards]
    
    # Convert ranks to their corresponding values
        rank_values_in_hand = sorted(set(self.rank_values[rank] for rank in ranks))
        
        # A straight needs at least 5 consecutive values
        for i in range(len(rank_values_in_hand) - 4):
            if rank_values_in_hand[i + 4] - rank_values_in_hand[i] == 4:
                return True
        
        # Handle the Ace-low straight case: Ace is both high and low
        if set([self.rank_values['2'], self.rank_values['3'], self.rank_values['4'], self.rank_values['5'], self.rank_values['A']]).issubset(rank_values_in_hand):
            return True
        
        return False

    def _is_three_of_kind(self, cards: List[Tuple[str, str]]) -> bool:
        rank_count = Counter(self.ranks)

        return 3 in rank_count.values()

    def _is_two_pair(self, cards: List[Tuple[str, str]]) -> bool:
        rank_count = Counter(self.ranks)

        pairs = [count for count in rank_count.values() if count == 2]

        return len(pairs) >= 2

    def _is_one_pair(self, cards: List[Tuple[str, str]]) -> bool:
        rank_count = Counter(self.ranks)

        return 2 in rank_count.values()

