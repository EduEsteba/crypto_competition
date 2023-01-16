# CRYPTO - Competition

A continuació hi ha un fitxer de passwords d'una empresa real que va tancar les seves portes fa temps a la comarca de girona. 

A partir del moment en què presento aquesta pràctica comença la competició. 

**Com puntuaré?**
La puntuació serà vers el nombre de hashos que aconsegueixis, la intenció és fer un barem en funció dels resultats generals. 

El que més hashos aconsegueixi tindrà la nota més alta. 

Contestar les preguntes i passar el challenge amb el professor pot assegurar-te un 5 tot i no tenir cap hash aconseguit.  

**També es treballa:**
**M05 - 4.2** Compromet contrasenyes a través d'atacs de diccionari, taules rainbow i força bruta contra els seus versions encriptades.

## TASQUES

- Instal·la l'eina hashcat o demostra que la tens instal·lada i la seva versió

```
C:\Users\Eduard\Desktop\hashcat-6.2.6>hashcat.exe --version
v6.2.6
```

- Quin tipus de hash hi ha al fitxer hashes.txt?
```
Hi ha el hash MD5 amb "salt", començen per $1$. 
```
- Cerca informació sobre el tipus de hash i descriu-me quant de vulnerable és.
```
MD5 no és considerat insegur per al seu ús en xifrat de contrasenyes a causa de diverses vulnerabilitats identificades a l'algoritme. En primer lloc, és vulnerable a atacs de col·lisió, cosa que significa que és possible crear dos missatges diferents amb el mateix hash. 

En segon lloc, és vulnerable a atacs de diccionari, cosa que significa que un atacant pot generar una taula de hash precomputada per intentar desxifrar contrasenyes xifrades. Tot i que l'ús d'una "salt" pot ajudar a mitigar aquests atacs, l'algorisme MD5 continua sent considerat insegur a llarg termini.
```
- Com ho faries per petar hashos més ràpid que els demés?
```
Intentaria buscar patrons com a exemple un patró seria que hi hagués noms amb dígits al final (Eduard872). A part generaria diccionaris propis a partir dels patrons i controlaria les contrasenyes que provo per no repetir contrasenyes.
```
- Què vol dir que un hash col·lisiona?
```
En informàtica, una col·lisió hash és el que passa quan dues entrades diferents a una funció hash produeixen el mateix resultat.
```
- Fes servir hashcat per petar el màxim de hashos que puguis

172 hash, https://github.com/AngelMascaro/girona_crack_hash_challenge 



Comanda per executar diccionaris

```
hashcat.exe -m500 -a0 -o final.txt hashes.txt diccionari.txt -0 -S
```

Comanda per executar diccionaris amb mascara

```
hashcat.exe -m500 -a6 -o final.txt hashes.txt diccionari.txt ?d?d
```

Webs on es poden trobar diccionaris:

- https://weakpass.com/
- https://wiki.skullsecurity.org/index.php/Passwords
 


