from enum import Enum
TrackState = Enum('TrackState', ['NEW_TRACK', 'UPDATE_IN_PROGRESS', 'PAUSED_TRACK', 'NOT_PLAYING'])
AuthFlow = Enum('AuthFlow', ['AUTHORIZATION_CODE_FLOW', 'CLIENT_CREDENTIALS_FLOW'])

AUTH_FLOW = AuthFlow.AUTHORIZATION_CODE_FLOW

SPOTIPY_REDIRECT_URI = ""
SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""
SPOTIPY_USERID = ""

alphaValue = 200
resolutionToTextRatio = 30

CONST_DEFAULT_UPDATE_TRACK_FREQUENCY = 0.1
CONST_LYRICS_PROVIDER = "Musixmatch"
CONST_DEFAFULT_TOKEN_REFRESH_FREQUENCY = 45
CONST_INF_SLEEP_FREQUENCY = float('inf')
CONST_CHECK_IS_PLAYING_FREQUENCY = 30


