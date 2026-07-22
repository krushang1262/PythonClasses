import pandas as pd 
import matplotlib.pyplot as plt

def bayes_churn_probability(prior_churn, prob_email_given_churn, prob_email):
    """
    Computes P(Churn | Email) using Bayes' Theorem:
    P(A|B) = (P(B|A) * P(A)) / P(B)
    """
    output = (prob_email_given_churn * prior_churn) / prob_email
    return output

pc = 0.15
peg = 0.6
pem = 0.25

result = bayes_churn_probability(pc,peg,pem)
print("Probability of bayes churn probability", result)