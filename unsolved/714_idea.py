# On a particular day, we have the following choices:
# 1. Sell on this day, buy from any earlier date.
#    For 1 <= j < i, we can buy from jth day and sell
#    on ith day, with profit as follows:
#    profit = profit[j] + (price[i] - price[j] - 2)
# 2. Hold. Dont do anything => How to denote this case?
#    Maybe for 1 <= j < i, the maximum ith day profit
#    is the maximum profit attainable from profit[1..j]?

# Think about the above conditions and come up with an optimal substructure.
