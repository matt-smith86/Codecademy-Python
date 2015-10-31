#Create a calculator that will add the cost of a meal with a predetermined tax and tip 

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
