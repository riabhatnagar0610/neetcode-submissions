class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        # 1. Create frequency arrays for 26 lowercase letters
        s1_count = [0] * 26
        window_count = [0] * 26
        # 2. Fill the target (s1) and the first window of s2
        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
            
        # 3. Slide the window through the rest of s2
        # We stop at n2 - n1 because the window is n1 characters wide
        for i in range(n2 - n1):
            if s1_count == window_count:
                return True
            
            # Slide logic: "Drop" the leftmost and "Add" the next rightmost
            # The character leaving the window is at index i
            window_count[ord(s2[i]) - ord('a')] -= 1
            # The character entering the window is at index i + n1
            window_count[ord(s2[i + n1]) - ord('a')] += 1
            
        # 4. Final check for the very last window position
        return s1_count == window_count
