class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        n=len(A)
        if n>12 or n<4:
            return []
        l=[]
        s=A
        for i in range(1,n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    s=s[:i]+"."+s[i:]     
                    s=s[:j+1]+"."+s[j+1:] 
                    s=s[:k+2]+"."+s[k+2:] 
                    if self.isvalid(s):
                        l.append(s)
                    s=A
        return l

    def isvalid(self,s):
        s=s.split(".")
        for i in s:
            if len(i)>3 or int(i)<0 or int(i)>255:
                return False
            if len(i)>1 and int(i)==0:
                return False
            if len(i)>1 and int(i)>0 and i[0]=="0":
                return False
        return True
