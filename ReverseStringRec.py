class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def tukar(index, len_s, s):
            if index == (len_s+1) // 2 :
                return
            s[index], s[len_s-index] = s[len_s-index], s[index]
            tukar(index+1, len_s, s)
        len_s = len(s)-1
        tukar(0, len_s, s)

        