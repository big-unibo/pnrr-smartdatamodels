{{< include guide.md >}}

# UniPR (2024-05-17)

Contesto: raccolta dati sensoriali in open field.

Goal analisi: 

- Indicatori agronomici (e.g., GDD per pomodoro e luppolo)
- Controllo irrigazione

Collezione dati:

- Campo aperto su pomodoro e luppolo. Qualcosa anche in serra.
- Sensori statici, georeferenziati nel momento dell'installazione
    - Water meter ogni 10 minuti. Valore in byte?
    - Milesight
    - Sensori aggregati/composti
- Allineare i payload a FIWARE
- Unificare i nomi (alcuni `temp`, altri `temperature`)
- Attuatori (e.g, valvole, sono mappabili su device FIWARE)
- Connettore verso FIWARE

# Integration steps (UniBO + UniPR)

- Step 1: (UniPR) avere un'esempio di entity per tipo
- Step 2: (UniBO) predisporre API per dati meteo, dato storico, dati satellitari

# Data models (UniBO)

- [WaterMeter (lorawan)](https://fiware-datamodels.readthedocs.io/en/stable/Environment/WaterQualityObserved/doc/spec/index.html)