import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A":2,
    "B":4,
    "C":5,
    "D":6
}

symbols_values = {
    "A":6,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol , symbol_count in symbols_count.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            values = random.choice(current_symbols)
            current_symbols.remove(values)
            column.append(values)
        columns.append(column)

    return columns

def print_slot_machine(columns):

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Enter the amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Invalid deposit amount. Please enter a positive number.")
        else:
            print("Invalid input. Please enter a numeric value.")
            
    return amount

def get_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-3): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Invalid number of lines. Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Invalid input. Please enter a numeric value.")
            
    return lines

def get_bet():
    while True:
        bet = input("Enter the amount to bet on each line: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Invalid bet amount. Please enter a number between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Invalid input. Please enter a numeric value.")
            
    return bet
def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}. Your current balance is ${balance}.")
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_values)
    print(f"You won ${winnings} on the line :", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current Balance is {balance}")
        ans = input("Press Enter to Spin (q to quit): ")
        if ans == 'q':
            break
        balance += spin(balance)

        print(f"You left with ${balance}")



main()