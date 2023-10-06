import random
import art

#print logo
print(art.logo)

#print game rules
print("Our Blackjack House Rules\n")
print("The deck is unlimited in size.")
print("There are no jokers.")
print("The Jack/Queen/King all count as 10.")
print("The the Ace can count as 11 or 1.")
print("Use the following list as the deck of cards:")
print("cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]")
print("The cards in the list have equal probability of being drawn.")
print("Cards are not removed from the deck as they are drawn.")
print("The computer is the dealer.")
print("\nLet the game begin!\n")

is_game_over = False  #for our reference
continue_adding_card = False
draw_response = ""  #draw another card?
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def deal_card():
  """Randomly choose a card from the list."""
  return random.choice(cards)

def calculate_score(list):
  """ Take a list of cards and return the sum of list. """
  return sum(list)

  #checks if there is an Ace and 10
  if 11 in list and 10 in list and len(list) == 2:
    return 0

  #setermines the value of ace.
  if 11 in list and sum(list) > 21:
    list.remove(11)
    list.append(1)

#draw cards
for i in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

def check_score():
  """Checks the score iteratively."""
  
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  print(f"\nYour cards: {user_cards}, current score = {user_score}")
  print(f"\nComputer's first card: {computer_cards[0]}")

  if user_score == 0 or computer_score == 0:
    is_game_over = True
    print("\nGot a black jack. Game over!")
    return
  elif user_score > 21:
    is_game_over = True
    print(f"\nYour final hand: {user_cards}, final score = {user_score}")
    print(f"\nComputer's final hand: {computer_cards}, final score = {computer_score}")
    print("\nYou went over. You loose!")
    return
  draw_response = input("\nDo you want to draw another card? 'y' or 'n': ")
  if draw_response == "y":
    user_cards.append(deal_card())
    check_score()
    continue_adding_card = True
  if draw_response == "n":
    is_game_over = True
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
    print(f"\nComputer's final hand: {computer_cards}, final score = {computer_score}")
    if user_score == computer_score:
      print("\nSame score. Game draw!")
      return
    elif user_score > computer_score or computer_score > 21:
      print("\nYou win!")
      return
    else:
      print("\nComputer wins!")
      return
check_score()
