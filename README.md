# PSRS readme

Personalized Smartphone Recommendation System

Language: Python

The goal of this project is to build a personalized smartphone recommendation system (PSRS) based on customers' shopping behavior for smartphones.

The data set of customers' shopping behavior is stored in the file: shopping.csv

The main file: psrs.py

Introduction:

1. PSRS provides an interface that requires us to type in a customer's name (for example: C) and a smartphone brand (for example: S).

2. Based on the analysis on the data set of shopping behavior, PSRS returns following similarity information:

    2.a) A customer similarity list: Customers on this list are ranked by the similarity of shopping behavior between them and C.
    
    2.b) A smartphone similarity list: Smartphones on this list are ranked by the similarity of buyers between them and S.

3. PSRS returns following recommendation list:

    3.a) A smartphone recommendation list for C. Each smartphone brand has a recommendation value. The higher value means the higher 
    probability that C may like the corresponding smartphone.
    
    3.b) A customer remcommendation list for S: Each customer has a recommendation value. The higher value means the higher probability
    that S may be liked by the corresponding customer.
