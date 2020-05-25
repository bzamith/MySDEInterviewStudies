# Source: Cracking the Coding Interview, 16.10

# Problem: "Living People"

# Example: Given a list of people with their birth and
# death years, implement a method to compute the year 
# with the most number of people alive. You may assume that
# all people were born between 1900 and 2000.

# Brute-force solution: Use a hash. For each person, iterate
# through the interval and increment in the hash. 

# Approach: Two sorted arrays, by date and by death. Two-pointers 
# strategy.

# Complexity:
# O(N*log(N)) time, with N = number of people
# O(N) space

def maxYearLivingPeopleBestApproach(dates):
	if not dates:
		return None
	sortedBornDate = []
	sortedDeathDate = []
	for date in dates:
		sortedBornDate.append(date[0])
		sortedDeathDate.append(date[1])
	currMax = 0
	currMaxDate = None
	bornPointer = 0
	deathPointer = 0
	currCount = 0
	while bornPointer < len(dates) or deathPointer < len(dates):
		if bornPointer < len(dates) and deathPointer < len(dates):
			if sortedBornDate[bornPointer] < sortedDeathDate[deathPointer]:
				currCount += 1
				if currCount > currMax:
					currMax = currCount
					currMaxDate = sortedBornDate[bornPointer]
				bornPointer += 1
			else: 
				currCount -= 1
				deathPointer += 1
		elif bornPointer < len(dates):
			currCount += 1
			if currCount > currMax:
				currMax = currCount
				currMaxDate = sortedBornDate[bornPointer]
			bornPointer += 1
		elif deathPointer < len(dates):
			currCount -= 1
			deathPointer += 1
	return currMaxDate

def maxYearLivingPeople(dates):
	if not dates:
		return None
	countHash = {}
	for date in dates:
		for i in range(date[0],date[1]+1):
			if i not in countHash:
				countHash[i] = 0
			countHash[i] += 1
	currMax = 0
	currMaxDate = None
	for date in countHash.keys():
		if countHash[date] > currMax:
			currMax = countHash[date]
			currMaxDate = date
	return currMaxDate

if __name__ == '__main__':
	print(maxYearLivingPeople([]))
	print(maxYearLivingPeople([(1920, 1939), (1911, 1944), (1920, 1955), (1938, 1939)]))
	print(maxYearLivingPeopleBestApproach([(1920, 1939), (1911, 1944), (1920, 1955), (1938, 1939)]))