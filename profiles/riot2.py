import requests
from profiles.models import UserProfile

def requestSummonerData(my_region, summonerName, APIKey):

    URL = "https://" + my_region + \
          ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" \
          + summonerName + "?api_key=" + APIKey

    print(URL)
    response = requests.get(URL)
    return response.json()

def requestRankedData(my_region, ID, APIKey):
    URL= "https://" + my_region + \
         ".api.riotgames.com/lol/league/v4/positions/by-summoner/" \
         + ID + "?api_key="+APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()

def main():

    summonerName = UserProfile.game_tag
    #summonerName = "Lumachino"
    my_region = UserProfile.region
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



    #print (responseJSON2[0]['tier'])
    #print (responseJSON2[0]['rank'])
    #print (responseJSON2[0]['leaguePoints'])


if __name__ == "__main__":
    main()

