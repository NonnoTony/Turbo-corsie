# Turbo Corsie

Gioco di corse di mini 4WD su piste giocattolo, pensato per il telefono.

- 11 piste da 3 giri, ognuna in un ambiente diverso (dalla cameretta al pianeta alieno)
- Garage 3D: crea, colora e modifica le tue auto, con 15 categorie di pezzi e la vista interna del telaio
- In due sullo stesso dispositivo (schermo diviso) oppure online con chiunque, con un codice stanza
- 7 lingue: italiano, inglese, tedesco, spagnolo, giapponese, arabo, russo

## Giocare

Il gioco è pubblicato con GitHub Pages dalla cartella `docs/`: basta aprire l'indirizzo del sito
(per esempio `https://NOMEUTENTE.github.io/turbo-corsie/`). Sul telefono si può aggiungere alla schermata Home
e si apre come un'app.

## Come è fatto

- `index.html`: il gioco completo in un solo file (HTML, CSS e JavaScript).
- `build_web.py`: crea `docs/index.html`, la versione per il sito, aggiungendo l'intestazione della pagina,
  il manifest e le icone.
- `docs/`: il sito pubblicato.

Librerie caricate da CDN: three.js r128 (grafica 3D) e PeerJS 1.5.4 (gare online tramite WebRTC).
I progressi dei giocatori restano salvati nel loro browser.

## Aggiornare il gioco

1. Modificare `index.html`.
2. Eseguire `python3 build_web.py`.
3. Fare commit e push: GitHub Pages pubblica la nuova versione in un paio di minuti.
