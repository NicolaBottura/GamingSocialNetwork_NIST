# NIST - Gaming Social Network

## Introduction
Social Network written in python using Django as web framework.
Over the classic functionalities proposed by a Social Network, we also want to allow the user to add in his profile data get from his real [League Of Legends](https://play.euw.leagueoflegends.com/it_IT) account.
To do this, you just need an API key, that can be found [here](https://developer.riotgames.com/).
This key must be added in our file [riot.py](https://github.com/NicolaBottura/GamingSocialNetwork_NIST/blob/master/profiles/riot.py) under the name of APIKey.
Now you are ready to test it, going through the edit profile page, /profiles/profile/edit_profile and adding the account's name(voice game_tag) and the region as an acronym(i.e. Europe west = euw1).
At this point the site just add in the database your fields game_tag and region and through the link you have just created you can get the account ID that will serve to find your account rankeds data.

## Requirements
To run NIST, you'll need Python on the current system, if is not already installed you can download the latest version here [Python](https://www.python.org/downloads/) official download page.

## Run NIST
Once you have downloaded [NIST](https://github.com/NicolaBottura/GamingSocialNetwork_NIST), you are ready to try it.

To run this program you just need to type in a shell
```bash
python manage.py runserver
```

or using the proposed functionalities by your IDE.

## Authors
* @Nicola Bottura
* @Stefano Remitti
