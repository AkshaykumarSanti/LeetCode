class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(v) for v in version1.split(".")]
        v2 = [int(v) for v in version2.split(".")]
        
        maxi = max(len(v1), len(v2))
        v1.extend([0] * (maxi - len(v1)))
        v2.extend([0] * (maxi - len(v2)))
        
        if v1 < v2:
            return -1
        elif v1 > v2:
            return 1
        return 0