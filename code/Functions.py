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
    
