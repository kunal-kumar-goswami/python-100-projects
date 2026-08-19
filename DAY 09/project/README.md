# Day 09 — 🏆 Silent Auction Program

> Part of my [100 Days of Python](../../) journey — Angela Yu's Python Pro Bootcamp

A silent auction program where multiple bidders can enter their name and bid, and the program determines the winner by finding the highest bid in a dictionary.

## 💡 What it does

The program prints an auction house ASCII logo, then repeatedly asks for a bidder's name and bid amount, storing each as a key-value pair in a dictionary. After each entry it asks whether there are more bidders. Once the auction ends, it loops through all the bids to find and announce the winner.

**Example:**
```
[auction house logo]
Enter your name: Priya
Enter your bid: $250
Is there anybody else for bidding? Type 'yes' or 'no': yes
Enter your name: Arjun
Enter your bid: $300
Is there anybody else for bidding? Type 'yes' or 'no': no
The winner is Arjun with a bid of $300.
```

## 🎯 Concepts Practiced

- Dictionaries for storing name-value pairs
- Functions with parameters (`find_highest_bidder()`)
- `while` loops for repeated input
- Iterating over a dictionary to compare values

## 🔑 Key Takeaways

- A dictionary is a natural fit for this problem — each bidder's name (key) maps directly to their bid (value), with no need for a separate matching list
- Finding the highest value in a dictionary follows the same "running maximum" pattern as finding the max in a list: track the best value seen so far while looping through
- Splitting the winner-finding logic into its own function (`find_highest_bidder()`) keeps the main input loop focused on just collecting bids
- Importing the ASCII art from a separate `art.py` file keeps `main.py` focused on the actual program logic

## 🛠️ Tech Stack

`Python 3`
