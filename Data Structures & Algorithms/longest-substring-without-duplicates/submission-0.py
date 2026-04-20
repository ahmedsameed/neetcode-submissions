class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
                mapd={}
                l=0
                res=0
                for r in range(len(s)):

                        while mapd.get(s[r],0)>=1:
                                print("L9")
                                mapd[s[l]]-=1        
                                l=l+1

                        mapd[s[r]]=1+mapd.get(s[r],0)

                        leng=r-l+1
                        print("L15")
                        print(r)
                        print(l)
                        
                        res=max(res,leng)
                print(mapd)
                return res

                        




                
                
                
                
                
                
                

    
            