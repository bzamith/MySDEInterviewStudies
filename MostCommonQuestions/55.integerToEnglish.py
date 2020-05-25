# Source: Cracking the Coding Interview, 16.8

def numberToWords(self, num: int) -> str:
    if not num or num == 0:
        return "Zero"
    
    first = ["", "One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
    firstDecimals = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    second = ["", "","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    third = ["", "Thousand", "Million", "Billion", "Trillion"]
    
    count = 0
    nbTriplets = 0
    triplet = [0,0,0]
    stack = []
    
    while num > 0:
        triplet[count] = num%10
        num = num//10
        if count == 0:
            stack.append(first[triplet[count]])
        if count == 1:
            if triplet[count] == 1:
                last = stack.pop()
                lastNumber = first.index(last)
                stack.append(firstDecimals[lastNumber])
            else:
                stack.append(second[triplet[count]])
        if count == 2:
            if nbTriplets >= 1:
                firstWord = stack.pop()
                secondWord = stack.pop()
                stack.append(third[nbTriplets])
                stack.append(secondWord)
                stack.append(firstWord)
            stack.append("Hundred")
            stack.append(first[triplet[count]])
            nbTriplets += 1
            count = -1
        count += 1
    
    if nbTriplets > 0 and not (stack[-2] in third or stack[-2] == "Hundred"):
        last = stack.pop()
        stack.append(third[nbTriplets])
        stack.append(last)
    
    resp = ""
    for i in range(len(stack)):
        resp += stack[-1-i]
        if resp[-1] != " ":
            resp += " "
    
    return resp.rstrip()

if __name__ == '__main__':
    print(numberToWords(1234567))