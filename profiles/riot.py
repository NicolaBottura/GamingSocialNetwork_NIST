import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def find_my_rank(request):
    current_user = request.user.userprofile

    summoner_name = current_user.game_tag
    my_region = current_user.region
    APIKey = "RGAPI-9e5ec0ed-b1f6-4b7e-8b7b-41f570313f80"

    summoner_data_url = "https://" + my_region + \
                        ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" \
                        + summoner_name + "?api_key=" + APIKey

    response = requests.get(summoner_data_url)
    print(response.status_code)
    summoner_data = response.json()
    print(summoner_data)

    if response.status_code != 200 and summoner_data['status']['status_code'] == 404:
        print("Non esiste nessun evocatore con questo nome!")  # aggiungere questo messaggio nella template
        return

    ID = summoner_data['id']

    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    session.get(summoner_data_url)

    ranked_data_url = "https://" + my_region + \
                      ".api.riotgames.com/lol/league/v4/positions/by-summoner/" \
                      + ID + "?api_key=" + APIKey

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

    Aggiornamento: aggiungo anche le vittorie e sconfitte per ogni tipo di lega.
    Inoltre gestisco sia se qualcuno ha fatto solo ranked SOLO che chi e' unranked.
    """
    if len(ranked_data) == 2 and ranked_data[1]['queueType'] == 'RANKED_FLEX_SR':
        current_user.ranked_flex = (
            ranked_data[1]['tier'], ranked_data[1]['rank'], ranked_data[1]['leaguePoints'])
        current_user.wins_flex = ranked_data[1]['wins']
        current_user.losses_flex = ranked_data[1]['losses']
        if ranked_data[0]['queueType'] == 'RANKED_SOLO_5x5':
            current_user.ranked_solo = (
                ranked_data[0]['tier'], ranked_data[0]['rank'], ranked_data[0]['leaguePoints'])
            current_user.wins_solo = ranked_data[0]['wins']
            current_user.losses_solo = ranked_data[0]['losses']
        else:
            current_user.ranked_solo = "Not enough solo queue played"
    elif len(ranked_data) == 2 and ranked_data[0]['queueType'] == 'RANKED_FLEX_SR':
        current_user.ranked_flex = (
            ranked_data[0]['tier'], ranked_data[0]['rank'], ranked_data[0]['leaguePoints'])
        current_user.wins_flex = ranked_data[1]['wins']
        current_user.losses_flex = ranked_data[1]['losses']
        if ranked_data[1]['queueType'] == 'RANKED_SOLO_5x5':
            current_user.ranked_solo = (
                ranked_data[1]['tier'], ranked_data[1]['rank'], ranked_data[1]['leaguePoints'])
            current_user.wins_solo = ranked_data[1]['wins']
            current_user.losses_solo = ranked_data[1]['losses']
        else:
            current_user.ranked_solo = "Not enough solo queue played"
    elif len(ranked_data) == 1 and ranked_data[0]['queueType'] == 'RANKED_SOLO_5x5':
        current_user.ranked_flex = "Not enough flex played"
        current_user.wins_flex = "0"
        current_user.losses_flex = "0"
        current_user.ranked_solo = (
            ranked_data[0]['tier'], ranked_data[0]['rank'], ranked_data[0]['leaguePoints'])
        current_user.wins_solo = ranked_data[0]['wins']
        current_user.losses_solo = ranked_data[0]['losses']
    elif len(ranked_data) == 0:
        current_user.ranked_flex = "Not enough flex played"
        current_user.ranked_solo = "Not enough solo queue played"
        current_user.wins_flex = "0"
        current_user.losses_flex = "0"
        current_user.wins_solo = "0"
        current_user.losses_solo = "0"

    current_user.save()




