# Django-harjoitus
Django-harjoitus 2022 syksy

## Asennus

1. Luo virtuaaliympäristö: ´python -m venv venv`
2. Aktivoi virtuaaliympäristö
    - esim. VSCodessa avaamalla jokin Python-tiedosto ja valitsemalla
      alhaalta Pythonin versionumeroa klikkaamalla `('venv': venv)`
    - muista käynnistää terminaali-ikkuna uudelleen ja tarkista, että
      venv on aktiivinen katsomalla, että siinä lukee `(venv)`
3. Asenna Django: `pip install django`

## Django tuturoiaali

https://docs.djangoproject.com/en/4.1/intro/tutorial01/

## Projektin luonti

1. Aja `django-admin startproject varaukset`
2. Siirrä varaukset kansion sisältö yhden ylemmäksi 
   hakemistopuussa.

## Kehityspalvelimen ajaminen
1. Aja ensin migraatiot: `python manage.py migrate`
2. Käynnistä 
```
python manage.py runserver
```
 
