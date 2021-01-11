# Initializing our blockchain list
blockchain = []
open_transactions = []
owner = 'Bob'

def get_last_blockchain_value():
  """ Returns the last value of the current blockchain """
  if len(blockchain) < 1:
    return None 
  return blockchain[-1]

def add_transaction(recipient, sender="owner", amount=1.0):
  """ Append a new value as well as the last blockchain value to the blockchain\n   
  Arguments:
    :send: The sender of the coins
    :recipient: The recipient of the coins.
    :amount: The amount of the coins sent with the transaction (default = 1.0)
  """
  transaction = {'sender': sender, "recipient": recipient, "amount": amount}
  open_transactions.append(transaction)

def mine_block():
  pass

def get_transaction_value():
  """ Returns the input of the user (a new transaction amount) as a float"""
  tx_recipient = input('Enter the recipient of the transaction: ')
  tx_amount = float(input('Your transaction amount please: '))
  return (tx_recipient, tx_amount)

def get_user_choice():
  return input('Your choice: ')

def print_blockchain_elements():
  for block in blockchain:
    print('Outputting Block')
    print(block)
  else:
    print('-' * 20)

def verify_chain():
  is_valid = True
  for block_index in range(len(blockchain)):
    if block_index == 0:
      continue
    elif blockchain[block_index][0] == blockchain[block_index-1]:
      is_valid = True
    else:
      is_valid = False
      break
  return is_valid
# add_value(get_transaction_value())
# add_value(last_transaction=get_last_blockchain_value(), transaction_amount=get_user_input())
# add_value(get_user_input(), get_last_blockchain_value())

waiting_for_input = True

while waiting_for_input:
  print('Please choose')
  print('1: Add a new transaction value')
  print('2: Output the blockchain blocks')
  print('h: Manipulate the chain')
  print('q: Quit')
  user_choice = get_user_choice()
  if user_choice == '1':
    tx_data = get_transaction_value()
    recipient, amount = tx_data
    add_transaction(recipient, amount=amount) #lets us skip sender which has default
    print(open_transactions)
  elif user_choice == '2':
    print_blockchain_elements()
  elif user_choice == 'h' or user_choice == 'H':
    if len(blockchain) >= 1:
      print('Blockchain manipulated')
      blockchain[0][0] == [2] #doesn't work
      print(blockchain[0][0])
    else:
      print('No blockchain to manipulate')
      continue
  elif user_choice == 'q' or user_choice == 'Q':
    waiting_for_input = False
    # continue
  else:
    print("Input was invalid. Please pick a value from the list")
  if not verify_chain():
    print('Invalid blockchian')
    waiting_for_input = False
  # print('Choice registered')
else:
  print("User left")