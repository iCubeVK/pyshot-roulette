Buckshot Roulette beta 1.1 fatta da iCubeVK

Per avviare il gioco, apri il file APRIMI.bat
Se vuoi "toccare" il codice, fai prima un bakup della cartella(oppure conserva l'archivio)


Changelogs:

Changelog beta 1.0:
- riscritto completamente il programma rispetto alla alpha che non funzionava.
- Il bot ha ancora dei bug, ho bisogno di tempo per trovarli.
- multiplayer e' stato completato.
- aggiunto delle descrizioni a quasi tutto.
- sistemato le funzioni che uso molto spesso in Utility.py.

Changelog beta 1.1:
- cambiato ambiente di sviluppo in PyCharm(a voi non cambia nulla, a me si)
- completato il bot con i relativi debug
- quasi completato le descrizioni(accontentatevi pk e' una rottura di palle)
- aggiunto il file programma.bat per comodita'(mi servira' dopo)

Changelog beta 1.1.1:
- FIXATO errore che avveniva quando il bot usava la birra e finivano i proiettili (Error: index ran out of range, line 179), per farlo è stato aggiunto 'break' sulla riga 193.

Changelog beta 1.1.2:
- FIXATO il doppio uso del vetrino da parte del bot (riga 133).
- FIXATO il testo di utilizzo delle manette da parte del player (riga 229).
- SISTEMATO \n in fondo alla stringa di testo per estetica (me ne ero scordato) nella riga 143.
- SISTEMATO \n in fondo alla stringa di testo per estetica (me ne ero scordato) nella riga 174.
- RIDOTTA LA POSSIBILITA' che il bot usi piu di 1 oggetto da 3 a 2 (riga 113).
- RIDOTTA LA POSSIBILITA' che il bot utilizzi il coltellino senza sapere il proiettile dal 20 al 10%(riga 128).
- SISTEMATO la stringa in output per far sapere su chi usa le manette il bot(riga 115).
- SCOPERTO che l'aggiunta di 'break' (fatta nell'update precedente) causava problemi quando il bot utilizza il fucile su se stesso, il turno del bot finiva anche se non doveva.
- FIXATO il bug aggiungendo 'continue' in riga 148 e 179.
- FIXATO la morte "ritardata" di un player (aggiunte righe 39:41).
- SISTEMATO informazioni sulla vita del bot nel suo turno (riga 108).

Changelog beta 1.2:
- AGGIUNTO OGGETTO polarizzatore.
- AGGIUNTO OGGETTO telefono.
- MODIFICATO il numero max di proiettili nel barile da 8 a 12.
- RIDOTTA LA POSSIBILITA' che il bot usi il fucile su se stesso da 30 al 25% (riga 190).
- RIMOSSO \n in fondo alla stringa di testo (riga 143).
- RIMOSSO \n in fondo alla stringa di testo (riga 174).
- RIFATTO completamente il modo in qui il bot conosce i proiettili.
- SISTEMATA la modalita debug.



