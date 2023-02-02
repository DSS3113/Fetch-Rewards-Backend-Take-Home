"""
NOTE:
For dealing with a transaction which causes a payer's points to become negative, I have made it
so that that specific transaction takes place after one that makes the payer's 
balance sufficiently positive so as for it to not become negative after the formerly specified 
transaction is performed (in accordance with the second rule). If it is inevitable for a payer's
balance to end up negative, then I cause the funtion to return None after printing an error.
"""

import csv
from datetime import datetime
import sys

def points_spender(csv_file, points_to_spend):
    transactions = []
    remaining_transactions = []
    payer_points_bal = {}
    points_spent = 0
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        dt = datetime.strptime(line[2], '%Y-%m-%dT%H:%M:%SZ')
        if line[0] not in payer_points_bal:
            payer_points_bal[line[0]] = 0
        transactions.append((line[0], int(line[1]), dt))

    # Sorting the transactions in accordance with the first rule
    transactions = sorted(transactions, key=lambda record: record[2])

    # Performing the transactions
    for t in transactions:
        if points_spent+t[1] > points_to_spend:
            payer_points_bal[t[0]] += points_spent + t[1] - points_to_spend
            points_spent = points_to_spend
        elif points_spent == points_to_spend:
            if payer_points_bal[t[0]] + t[1] < 0:
                remaining_transactions.append(t)
            else:
                payer_points_bal[t[0]] += t[1]
        else:
            points_spent += t[1]
    
    # Performing the remaining transactions (if any)
    for rt in remaining_transactions:
        if payer_points_bal[t[0]] + rt[1] < 0:
            sys.stderr.write(f"Error: This series of transactions can't be performed without resulting in a negative payer balance for {rt[0]}. Hence, the script is exiting.")
            return
        else:
            payer_points_bal[t[0]] += rt[1]

    return payer_points_bal

def main():
    points_to_spend = int(sys.argv[1])
    f = open("transactions.csv", "r")
    result = points_spender(f, points_to_spend)
    if result != None:
        print(result)
    f.close()
   

if __name__ == "__main__":
    main()