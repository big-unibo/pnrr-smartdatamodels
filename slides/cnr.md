{{< include guide.md >}}

# CNR (2024-04-18)

Contesto: ...

Goal analisi

- Output: per ogni cella delle griglia, indicatori sulla coltura
    - Pomodoro: stima della produttività tramite identificazione bacche mature 
    - Grano: valutare andamento grano, informazioni morfologiche (e.g., altezza del grano)

Collezione dati:

- Immagini (RGB, multispettrali, LIDAR) raccolte con droni su varie colture (pomodoro, grano)
- Fogli Excel (pochi MB) con punti campionamento in castagneto
- Dati meteo e satellitari (utili da acquisire) in Italia (grano in ER, pomodoro in Puglia)

Tecnologie:

- Metashape (fotogrammetria e ortomappe)

# Integration steps (UniBO + CNR)

- Step 1: (UniBO) condivisione e flusso in uscita dati meteo ARPAE (sia in formato GRIB originale e corrispettivo tabellare)
    - Giorno: latitudine e longitudine del centro del riquadro, con valori di temperatura, piogge, e umidità
    - Preparare API: data la lat/lon del giorno, restituire i dati meteo
    - Invio sample dato ARPAE
- Step 2: (CNR) ...

# Data models (UniBO)

- ...