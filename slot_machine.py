import random
MAX_LINES = 3
MIN_PAY = 1
MAX_PAY = 100

ROWS = 3
COLS =3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_checked = column[line]
            if symbol != symbol_checked:
                break

        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings , winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="!")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit ?  N")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")

        else:
            print("Please enter a number")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("lines must be greater than 0")

        else:
            print("Please enter a number")

    return lines


def get_pay():
    while True:
        pay = input("Enter the amount you wish to pay on each line ")
        if pay.isdigit():
            pay = int(pay)
            if MIN_PAY <= pay <= MAX_PAY:
                break
            else:
                print(f"Pay must be between N{MIN_PAY} - N{MAX_PAY}.")

        else:
            print("Please enter a number")

    return pay


def game(balance):
    lines = get_number_of_lines()
    while True:
        pay = get_pay()
        total_pay = pay * lines
        if total_pay > balance:
            print(
                f"Insufficient funds, The amount you are trying to pay is more than your deposit, your balance is N{balance}")
        else:
            break

    print(f"You are paying N{pay} on each line and total pay is equal to: {total_pay}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, pay, symbol_value)
    print(f"You won N{winnings}.")
    print(f"You won on lines", *winning_lines)
    return winnings - total_pay


def main():
    balance = deposit()
    while True:
        print(f"Current balance is N{balance}")
        answer = input("Press enter to spin(q to exit)")
        if answer == "q":
            break
        balance += game(balance)

    print(f"You left with N{balance}")


main()
