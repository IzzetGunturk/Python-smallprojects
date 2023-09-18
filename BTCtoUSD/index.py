"""
    In this project, you'll create a program that that tells
    you when the value of your Bitcoin falls below $30,000.

    You will need to:
    - Create a function to convert Bitcoin to USD
    - If your Bitcoin falls below $30,000, print a message.

    You can assume that 1 Bitcoin is worth $40,000

"""

investment_in_bitcoin = 1.2
bitcoin_to_usd = 40000

# 1) write a function to calculate bitcoin to usd
def bitcoinToUsd(bitcoin_amount, bitcoin_value_usd):
    btcusd = bitcoin_amount * bitcoin_to_usd
    return btcusd

answer = bitcoinToUsd(investment_in_bitcoin, bitcoin_to_usd)

# 2) use function to calculate if the investment is below $30,000
alert = "Its below 30000"

if answer < 30000:
    print(alert)
else:
    print(answer)