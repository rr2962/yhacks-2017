# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:55:30 2017

@author: udainagpal
"""



def breakeven_year(monthly_premium, mortality_benefit, age):
    yearly_cost = monthly_premium * 12
    exp_years = mortality_benefit/yearly_cost
    breakeven_year = exp_years + age
    return (breakeven_year)
    
#print(breakeven_year(150, 18000, 37))
  
"""  
#Converts a list of cashflows (1 per year) into total present value
def cashflow_present_value(all_cashflows, interest_rate_percentage):
    present_value = 0
    for cashflow in all_cashflows:
        adjusted_rate = (1 + interest_rate_percentage/100)**(all_cashflows.index(cashflow)+1)
        present_value = present_value + cashflow/adjusted_rate
    return(present_value)

#print(cashflow_present_value([3,5,4],4))    
    
def life_expectancy(age, mortality_rates):
    likelihood_alive = 1
    relevant_rates = mortality_rates[age+1:]
    for mort_rate in mortality_rates:
"""