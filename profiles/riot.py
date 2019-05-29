import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def find_my_rank(request):
    current_user = request.user.userprofile
    summoner_name = current_user.game_tag
    my_region = current_user.region
    APIKEY = "RGAPI-688a82b1-1a46-4e75-b8c1-84928152a623"

    summoner_data_url = "https://" + my_region + \
          ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" \
          + summoner_name + "?api_key=" + APIKEY

    response = requests.get(summoner_data_url)

    summoner_data = response.json()
    ID = summoner_data['id']

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.get(summoner_data_url)

    ranked_data_url = "https://" + my_region + \
         ".api.riotgames.com/lol/league/v4/positions/by-summoner/" \
         + ID + "?api_key="+APIKEY

    response2 = requests.get(ranked_data_url)

    ranked_data = response2.json()

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.get(ranked_data_url)

    """
    Se il tipo di ranked e' FLEX allora aggiorno i campi relativi a quel tipo di coda
    e per la coda in SOLO, altrimenti se trova solamente il tipo SOLO, assegno il campo
    relativo a FLEX vuoto e vado ad inserire i dati per SOLO.
    
    Manca la condizione per chi non ha mai fatto ranked, quindi ranked_data = 0.
    (non so come farlo dioooo booono)
    """
    if ranked_data[0]['queueType'] == 'RANKED_FLEX_SR':
        current_user.ranked_flex = (
            ranked_data[0]['tier'], ranked_data[0]['rank'], ranked_data[0]['leaguePoints'])
        if ranked_data[0]['queueType'] != '':
            current_user.ranked_solo = (
                ranked_data[1]['tier'], ranked_data[1]['rank'], ranked_data[1]['leaguePoints'])
        else:
            current_user.ranked_solo = "Not enough solo queue played"
    elif ranked_data[0]['queueType'] == 'RANKED_SOLO_5x5':
        current_user.ranked_flex = "Not enough flex played"
        current_user.ranked_solo = (
            ranked_data[0]['tier'], ranked_data[0]['rank'], ranked_data[0]['leaguePoints'])

    current_user.save()

