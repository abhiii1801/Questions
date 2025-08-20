#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, arr):
        _max = arr[0]
        _min = arr[0]
        
        for i in arr:
            if i > _max:
                _max = i
            if i < _min:
                _min = i
                
        return _min, _max