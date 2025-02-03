import pytest
from src.show_down import ShowDown

@pytest.mark.parametrize("community_cards, player_cards, expected_rank", [
    (["10H", "JH", "QH", "KH", "AH"], ["2D", "3C"], 10),  # Royal Flush
    (["8D", "9D", "10D", "JD", "QD"], ["2S", "3H"], 9),  # Straight Flush
    (["9S", "9H", "9D", "9C", "2H"], ["5D", "6H"], 8),  # Four of a Kind
    (["7S", "7H", "7D", "6C", "6H"], ["2D", "3H"], 7),  # Full House
    (["2H", "4H", "6H", "8H", "KH"], ["QH", "AH"], 6),  # Flush
    (["3D", "4S", "5H", "6C", "7D"], ["2H", "9C"], 5),  # Straight
    (["5D", "5H", "5C", "8S", "9H"], ["2S", "3D"], 4),  # Three of a Kind
    (["4D", "4H", "6S", "6C", "9H"], ["2S", "2D"], 3),  # Two Pair
    (["4D", "4H", "6S", "6C", "9H"], ["3S", "2D"], 3),  # Two Pair
    (["3D", "3H", "6S", "7C", "9H"], ["2S", "KH"], 2),  # One Pair
    (["2D", "4H", "6S", "9C", "KH"], ["3S", "JD"], 1),  # High Card
    # Royal Flush
    (["10H", "JH", "QH", "KH", "AH"], ["2D", "3C"], 10),  
    
    # Straight Flush
    (["8D", "9D", "10D", "JD", "QD"], ["2S", "3H"], 9),  
    
    # Four of a Kind
    (["9S", "9H", "9D", "9C", "2H"], ["5D", "6H"], 8),  
    
    # Full House
    (["7S", "7H", "7D", "6C", "6H"], ["2D", "3H"], 7),  
    
    # Flush
    (["2H", "4H", "6H", "8H", "KH"], ["QH", "AH"], 6),  
    
    # Straight
    (["3D", "4S", "5H", "6C", "7D"], ["2H", "9C"], 5),  
    
    # Three of a Kind
    (["5D", "5H", "5C", "8S", "9H"], ["2S", "3D"], 4),  
    
    # Two Pair
    (["4D", "4H", "6S", "6C", "9H"], ["2S", "2D"], 3),  
    
    # Two Pair (different values)
    (["4D", "4H", "6S", "6C", "9H"], ["3S", "2D"], 3),  
    
    # One Pair
    (["3D", "3H", "6S", "7C", "9H"], ["2S", "KH"], 2),  
    
    # High Card
    (["2D", "4H", "6S", "9C", "KH"], ["3S", "JD"], 1),
        
    # Edge Case: Flush
    (["2H", "4H", "6H", "8H", "KH"], ["3H", "JH"], 6), 
    
    # Edge Case: All Same Card (Four of a Kind in a hand with only one rank)
    (["9H", "9D", "9C", "9S", "8H"], ["2D", "3S"], 8),  # Four of a Kind
    
    # Edge Case: Full House with 3 of one rank and 3 of another
    (["7H", "7D", "7S", "3H", "3D"], ["2S", "3C"], 7),  # Full House
    
    # Edge Case: Flush with only 5 cards of the same suit, no straight
    (["2H", "9H", "4H", "5H", "6H"], ["7S", "KH"], 6),  # Flush
    
    # Edge Case: Straight with all the cards being different suits
    (["2H", "3D", "4S", "5C", "6H"], ["7S", "KC"], 5),  # Straight
    
    # Edge Case: Full House (3 cards of one rank, 2 cards of another)
    (["8H", "8D", "8S", "5H", "5D"], ["4C", "3D"], 7),  # Full House
    
    # Edge Case: Pair of Aces (with lower high cards)
    (["AH", "AC", "5D", "6H", "8S"], ["3D", "4C"], 2),  # One Pair (Aces)
    
    # Edge Case: Straight with a low Ace (Ace is low in straight)
    (["AH", "2D", "3H", "4S", "5C"], ["6S", "7D"], 5),  # Straight with Ace low
    
    # Edge Case: Ace-high flush with no pairs
    (["AH", "KH", "QH", "JH", "10H"], ["2S", "3D"], 10),  # Royal Flush
    
    # Edge Case: All cards same rank (e.g., Four Kings and random other cards)
    (["KS", "KC", "KH", "KD", "2H"], ["3S", "4C"], 8),  # Four of a Kind (Kings)
    
    # Edge Case: Straight with gaps (non-consecutive but part of a straight)
    (["4H", "5D", "6C", "7H", "8S"], ["3D", "2S"], 5),  # Straight with gaps
])
def test_evaluate_hand(community_cards, player_cards, expected_rank):
    showdown = ShowDown(community_cards)
    assert showdown.evaluate_hand(player_cards) == expected_rank