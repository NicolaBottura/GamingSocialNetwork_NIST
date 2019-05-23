from riotwatcher import RiotWatcher, ApiError
from profiles.models import UserProfile
from time import sleep
import requests
"""
watcher = RiotWatcher('RGAPI-e6eb6c3a-c2ec-4296-9771-fda4e4e6a768')

my_region = UserProfile.region
my_name = UserProfile.game_tag


def find_my_rank():
    me = watcher.summoner.by_name(my_region, my_name)
#print(me)

# all objects are returned (by default) as a dict
# lets see if I got diamond yet (I probably didn't)
    my_ranked_stats = watcher.league.positions_by_summoner(my_region, me['id'])
#print(my_ranked_stats)

    if my_ranked_stats[0]['queueType'] == 'RANKED_FLEX_SR':
        UserProfile.ranked_flex = (my_ranked_stats[0]['tier'], my_ranked_stats[0]['rank'], my_ranked_stats[0]['leaguePoints'])
        #print("Flex rank: ", my_rank_flex)
        UserProfile.ranked_solo = (my_ranked_stats[1]['tier'], my_ranked_stats[1]['rank'], my_ranked_stats[1]['leaguePoints'])
        #print("Solo: ", my_rank_soloq)
    elif my_ranked_stats[0]['queueType'] == 'RANKED_SOLO_5x5':
        UserProfile.ranked_solo = (my_ranked_stats[0]['tier'], my_ranked_stats[0]['rank'], my_ranked_stats[0]['leaguePoints'])
        #print("Solo: ", my_rank_soloq)

        # For Riot's API, the 404 status code indicates that the requested data wasn't found and
        # should be expected to occur in normal operation, as in the case of a an
        # invalid summoner name, match ID, etc.
        #
        # The 429 status code indicates that the user has sent too many requests
        # in a given amount of time ("rate limiting").
    try:
        response = watcher.summoner.by_name(my_region, 'this_is_probably_not_anyones_summoner_name')
    except ApiError as err:
        if err.response.status_code == 429:
            print('We should retry in {} seconds.'.format(err.response.headers['Retry-After']))
            print('this retry-after is handled by default by the RiotWatcher library')
            print('future requests wait until the retry-after time passes')
        elif err.response.status_code == 404:
            print('Summoner with that ridiculous name not found.')
        else:
            raise

    return UserProfile.ranked_flex, UserProfile.ranked_solo
"""


import requests
from profiles.models import UserProfile
from time import sleep
from requests.exceptions import RequestException
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def find_my_rank(request):
    UserProfile.game_tag = "lumachino"
    UserProfile.region = "euw1"
    summonerName = str(UserProfile.game_tag)
    my_region = str(UserProfile.region)
    APIKEY = "RGAPI-815befbe-31f4-486b-b20d-ff2a7a3f0111"

    #Prima parte
    URL_Summoner_data = "https://" + my_region + \
          ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" \
          + summonerName + "?api_key=" + APIKEY

    response = requests.get(URL_Summoner_data)

    summoner_data = response.json()
    ID = summoner_data['id']

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    #sleep(5)
    session.get(URL_Summoner_data)

    #Seconda parte
    URL_Ranked_data = "https://" + my_region + \
         ".api.riotgames.com/lol/league/v4/positions/by-summoner/" \
         + ID + "?api_key="+APIKEY

    response2 = requests.get(URL_Ranked_data)

    ranked_data = response2.json()

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.get(URL_Ranked_data)

    if ranked_data[0]['queueType'] == 'RANKED_FLEX_SR':
        UserProfile.ranked_flex = (
        ranked_data[0]['tier'], ranked_data[0]['rank'], ranked_data[0]['leaguePoints'])
        # print("Flex rank: ", my_rank_flex)
        UserProfile.ranked_solo = (
        ranked_data[1]['tier'], ranked_data[1]['rank'], ranked_data[1]['leaguePoints'])
        # print("Solo: ", my_rank_soloq)
    elif ranked_data[0]['queueType'] == 'RANKED_SOLO_5x5':
        UserProfile.ranked_solo_tier = ranked_data[0]['tier']
        UserProfile.ranked_solo_rank = ranked_data[0]['rank']
        UserProfile.ranked_solo_points = str(ranked_data[0]['leaguePoints'])

    print(str(UserProfile.ranked_solo_points))
    print(str(UserProfile.ranked_solo_tier))
    print(str(UserProfile.ranked_solo_rank))
        #UserProfile.ranked_solo = (
        #ranked_data[0]['tier'], ranked_data[0]['rank'], ranked_data[0]['leaguePoints'])
        # print("Solo: ", my_rank_soloq)

"""
def find_my_rank():

    summonerName = str(UserProfile.game_tag)
    #summonerName = "Lumachino"
    my_region = str(UserProfile.region)
    #my_region = "euw1"
    APIKey = "RGAPI-9a078723-0577-48de-9e62-aafe96534e27"
    responseJSON = requestSummonerData(my_region, summonerName, APIKey)

    print(responseJSON)
    ID = (responseJSON['id'])
    print(ID)

    responseJSON2 = requestRankedData(my_region, ID, APIKey)

    if responseJSON2[0]['queueType'] == 'RANKED_FLEX_SR':
        UserProfile.ranked_flex = (
        responseJSON2[0]['tier'], responseJSON2[0]['rank'], responseJSON2[0]['leaguePoints'])
        # print("Flex rank: ", my_rank_flex)
        UserProfile.ranked_solo = (
        responseJSON2[1]['tier'], responseJSON2[1]['rank'], responseJSON2[1]['leaguePoints'])
        # print("Solo: ", my_rank_soloq)
    elif responseJSON2[0]['queueType'] == 'RANKED_SOLO_5x5':
        UserProfile.ranked_solo = (
        responseJSON2[0]['tier'], responseJSON2[0]['rank'], responseJSON2[0]['leaguePoints'])
        # print("Solo: ", my_rank_soloq)

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    session.get(responseJSON)
    session.get(responseJSON2)

def requestSummonerData(my_region, summonerName, APIKey):

    URL = "https://" + my_region + \
          ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" \
          + summonerName + "?api_key=" + APIKey

    response = requests.get(URL)

    #try:
    #    response
    #except requests.exceptions.ConnectionError:
    #   response.status_code = "Connection refused"
    
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    session.get(URL)
    
    return response.json()

def requestRankedData(my_region, ID, APIKey):
    URL= "https://" + my_region + \
         ".api.riotgames.com/lol/league/v4/positions/by-summoner/" \
         + ID + "?api_key="+APIKey

    response = requests.get(URL)

    #try:
    #   response
    #except requests.exceptions.ConnectionError:
    #    response.status_code = "Connection refused"
    
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    session.get(URL)
    return response.json()





    #print (responseJSON2[0]['tier'])
    #print (responseJSON2[0]['rank'])
    #print (responseJSON2[0]['leaguePoints'])
"""

