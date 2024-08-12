import datetime
import prettytable as pt

balance = 0
logs = []

def input_decimal_validation(func):
  def wrapper(*args, **kwargs):
    number = args[0]
    max_decimal_places = 2
    # Convert the number to a string
    number_str = str(number)
    # Split the string by the decimal point
    decimal_index = number_str.index('.')
    if '.' in number_str and len(number_str) - 1 - decimal_index > 2:
      print(f"Format of the number is invalid. The number should be in the format of 1234.56")
    else:
      func(*args, **kwargs)

  return wrapper

@input_decimal_validation
def deposit(amount):
  global balance
  balance += amount
  write_log(action="deposit", amount=amount)
  print(f"You have deposited {amount} to your account. The total balance is {balance}\n")

@input_decimal_validation
def withdraw(amount):
  global balance
  if amount > balance:
    print(f"You do not have enough balance to withdraw. The total balance is {balance}\n")
  else:
    balance -= amount
    write_log(action="withdraw", amount=-amount)
    print(f"You have withdrawn {amount} from your account. The total balance is {balance}\n")

def show_logs():
  table = pt.PrettyTable()
  table.field_names = ["Created At", "Action", "Amount", "Balance"]
  for log in logs:
    table.add_row(log)
  print(table)

def write_log(action, amount):
  created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  logs.append([created_at, action, amount, balance])

def show_balance():
  print(f"Here is your balance: {balance}\n")

def show_menu():
  menu = """
  Please follow the menu and input the command
  0. System off
  1. Deposit
  2. Withdraw
  3. Show logs
  4. Show balance
  """
  print(menu)

while True:
  show_menu()
  try:
    instruction = int(input("Please follow the menu and input the command\n"))
    match instruction:
      case 0:
        print("System off\n")
        break
      case 1:
        deposit(float(input("How much do you want to deposit?\n")))
      case 2:
        withdraw(float(input("How much do you want to withdraw?\n")))
      case 3:
        show_logs()
      case 4:
        show_balance()
      case _:
        print("Invalid command\n")
  except ValueError:
    print("Invalid command\n")


