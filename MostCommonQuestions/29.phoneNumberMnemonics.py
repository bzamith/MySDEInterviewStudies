# Source: https://www.youtube.com/watch?v=a-sMgZ7HGW0

# Problem: "Compute All Mnemonics For A Phone Number"

# Example: 
#   {1: ''
#    2: 'A','B','C'
#    3: 'D','E','F'
#    4: 'G','H','I'
#    5: 'J','K','L'
#    6: 'M','N','O'
#    7: 'P','Q','R','S'
#    8: 'T','U','V'
#    9: 'W','X','Y','Z'
#   }
# So for "23" -> ["AD","AE","AF","BD","BE","BF","CD","CE","CF"]

# Approach: Backtracking!

def phoneNumberMnemonics(string):
	def getPhoneNumberMnemonics(currString):
		currSize = len(currString)
		if currSize == len(string):
			resp.append(currString)
		else:
			digit = int(string[currSize])
			for element in phoneNumbers[digit]:
				getPhoneNumberMnemonics(currString+element)

	phoneNumbers = {1: [' '],2: ['A','B','C'], 3: ['D','E','F'],
		4: ['G','H','I'], 5: ['J','K','L'], 6: ['M','N','O'],
		7: ['P','Q','R','S'], 8: ['T','U','V'], 9: ['W','X','Y','Z']}
	resp = []
	getPhoneNumberMnemonics('')
	return resp

if __name__ == "__main__":
	print(phoneNumberMnemonics("234"))
	print(phoneNumberMnemonics("1"))
	print(phoneNumberMnemonics("113"))
	print(phoneNumberMnemonics("23"))
	print(phoneNumberMnemonics(""))