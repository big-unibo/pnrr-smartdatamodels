{{< include guide.md >}}

# CNR (2024-04-18)

Contesto: ...

Goal analisi

- Output: per ogni cella delle griglia, indicatori sulla coltura
    - Pomodoro: stima della produttività tramite identificazione bacche mature 
    - Grano: valutare andamento grano, informazioni morfologiche (e.g., altezza del grano)

Collezione dati:

- Immagini (RGB, multispettrali, LIDAR) raccolte con droni su varie colture (pomodoro, grano) da 5/15m di altezza (40/60GB ogni volta)
    - 100 foto equidistanti, costruiscono ortoimmagine da cui si ricavano griglie di immagini (5x5m, 10x10m)
- Fogli Excel (pochi MB) con punti campionamento in castagneto
- Dati meteo e satellitari (utili da acquisire) in Italia (grano in ER, pomodoro in Puglia)

Tecnologie:

- Metashape (fotogrammetria e ortomappe)

# Integration steps (UniBO + CNR)

- Step 1: (UniBO) condivisione e flusso in uscita dati meteo ARPAE (sia in formato GRIB originale e corrispettivo tabellare)
    - Invio sample dato ARPAE
    - Giorno: latitudine e longitudine del centro del riquadro, con valori di temperatura, piogge, e umidità
    - Preparare API: data la lat/lon del giorno, restituire i dati meteo. GET con punto spaziale e range di date (max 3/4 mesi)
- Step 2: (CNR)
    - Cosa c'è in ogni cella?
    - Formato dell'output (GRIB? altro?)

# Data models (UniBO)

- AgriParcel
- Camera