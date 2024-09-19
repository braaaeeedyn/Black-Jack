import random
from art import logo



def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, Opponent has BlackJack!"
  elif user_score == 0:
    return "Win, you have BlackJack!"
  elif user_score >21:
    return "Lose, you went over!"
  elif computer_score > 21:
    return "Win, Opponent went Over!"
  elif user_score > computer_score:
    return "You Win!"
  else:
    return "You Lose!"
    
def blackjack():
  print(logo)
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"    Your Card: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  while computer_score != 0 and computer_score <17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  
  print(f"    Your Final Hand: {user_cards}, final score: {user_score}")
  print(f"    Computer's Final Hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n'") =="y":
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  blackjack()














