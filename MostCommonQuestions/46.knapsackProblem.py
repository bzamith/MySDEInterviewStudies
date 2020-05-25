# Source: https://www.youtube.com/watch?v=xCbYmUPvc2Q

# Problem: "Knapsack Problem"

# Example: Write a program that selects a subset of items has
# a maximum value and satisfies a given weight constraint

# Solution 1: Not Sorting + Dynamic Programming
# Solution 2: Sorting by cost-benefit

def knapsackProblemBestApproach(items, maxWeight): #[value, weight]
	if not items or not maxWeight:
		return 0
	memo = [[-1 for i in range(maxWeight + 1)] for j in range(len(items) + 1)] 
	# If weight of the nth item is  
	# more than Knapsack of capacity,  
	# then this item cannot be included  
	# in the optimal solution 
	return knapsackProblemBestApproachHelper(memo, items, maxWeight)

def knapsackProblemBestApproachHelper(memo, items, maxWeight):
	n = len(items)
	if n == 0 or maxWeight == 0:
		return 0
	if memo[n][maxWeight] != -1: 
		return memo[n][maxWeight] 
	if items[n-1][1] > maxWeight: 
		memo[n][maxWeight] = knapsackProblemBestApproachHelper(memo, items[0:n-1], maxWeight) 
		return memo[n][maxWeight]
	else:
		option1 = items[n-1][0] + knapsackProblemBestApproachHelper(memo, items[0:n-1], maxWeight-items[n-1][1])
		option2 = knapsackProblemBestApproachHelper(memo, items[0:n-1], maxWeight) 
		memo[n][maxWeight] = max(option1, option2)
		return memo[n][maxWeight]

def knapsackProblem(items, maxWeight): #[value, weight]
	if not items or not maxWeight:
		return None
	benefitItems = []
	for item in items:
		benefitItems.append([(item[0]/item[1]),item[0],item[1]])
	benefitItems.sort(reverse=True)
	currWeight = 0
	maxValue = 0

	for i in range(0,len(benefitItems)):
		if currWeight + benefitItems[i][2] <= maxWeight:
			currWeight += benefitItems[i][2]
			maxValue += benefitItems[i][1]
	return maxValue

if __name__ == '__main__':
	print(knapsackProblemBestApproach([(60,5),(51,3),(70,2),(30,1)],4))
	print(knapsackProblem([(60,5),(51,3),(70,2),(30,1)],4))