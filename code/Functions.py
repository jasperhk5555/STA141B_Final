def searchfeatures(x,feature):
    '''
    Returns specific feature of a song from Spotify API
    
    Inputs: x=song code, feature: feature of song
    Output: Value of specific feature for the song, nan if no value found
    '''
    try:
        return spotify.audio_features(x)[0][feature]
    except:
        return np.nan
    

def rbo(list1, list2, p=0.9):
   import math
    # tail recursive helper function
   def helper(ret, i, d):
       l1 = set(list1[:i]) if i < len(list1) else set(list1)
       l2 = set(list2[:i]) if i < len(list2) else set(list2)
       a_d = len(l1.intersection(l2))/i
       term = math.pow(p, i) * a_d
       if d == i:
           return ret + term
       return helper(ret + term, i + 1, d)
   k = max(len(list1), len(list2))
   x_k = len(set(list1).intersection(set(list2)))
   summation = helper(0, 1, k)
   return ((float(x_k)/k) * math.pow(p, k)) + ((1-p)/p * summation)
