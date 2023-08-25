import os
import sys

print(sys.path)

#from portfolio import portfolio

#Adjust the import path to go one level up to access the portfolio package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("hello")