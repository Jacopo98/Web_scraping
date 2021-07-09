# Installazione delle librerie utili
pip install beautifulsoup4
pip install requests

import requests
from bs4 import BeautifulSoup as bs
r = requests.get("https://www.ilmeteo.it/meteo/Roma")
contenuto = bs(r.text)
print(contenuto.title)            # per ottenere l’intero tag HTML possiamo utilizzare la proprietà title
print(contenuto.title.string)     # per ottenere solamente il testo all’interno del tag dobbiamo accedere alla proprietà string del tag

# Possiamo anche ottenere paragrafi e link della pagina web
print(contenuto.p)
print(contenuto.a)

# Se invece vogliamo accedere ad un attributo specifico di un tag HTML, possiamo specificare l’attributo tra parentesi quadre nel seguente modo:
print(contenuto.a["href"])

# Per ottenere tutti i tag HTML di una pagina web sotto forma di lista python possiamo usare la funzione  findAll() 
# Vediamo un esempio dove otteniamo tutti i link ( tag <a> ) nella pagina.
for link in contenuto.findAll("a"):
    print(link.get("href"))
    
# Web scraping: Come ottenere tutti i tag con classe specifica con Python
import requests
from bs4 import BeautifulSoup as bs
r = requests.get("https://www.ilmeteo.it/meteo/Roma")
contenuto = bs(r.text)
temps = contenuto.findAll("span", {"class": "tmax"})
for temp in temps:
    print(temp.text)
    
    # Quando eseguiamo questo codice, vedremo in output tutte le temperature della settimana per Roma

# Web scraping: Come ottenere tutti i tag con id specifico con Python
temps = contenuto.findAll("span", {"id": "tmax"})
# Come potete vedere l’unica cosa che cambia è il nome ‘class’ che diventa ‘id’.

    
    
    
    
    
    
