# Fetch Rewards Backend Engineering Take Home Test

Hello, this is my submission for the Fetch Rewards Backend Engineering Take Home Test.

For dealing with a transaction which causes a payer's points to become negative, I have made it
so that that specific transaction takes place after one that makes the payer's 
balance sufficiently positive so as for it to not become negative after the formerly specified 
transaction is performed (in accordance with the second rule). If it is inevitable for a payer's
balance to end up negative, then I cause the funtion to return None after printing an error.

To run the code on Unix, `cd` into the directory where this repository is cloned and then run:
```
python3 mycode.py [points_to_spend]
```
For example:
```
python3 mycode.py 5000
```
On Windows, `cd` into the directory where this repository is cloned and then run:
```
python mycode.py [points_to_spend]
```
For example:
```
python mycode.py 5000
```
