{{< include guide.md >}}

# Incontro (2024-05-17)

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
- Unificare i nomi (alcuni `temp`, altri `temperature`), dove possibile usare le `controlledProperty` di entity `Device`
- Attuatori (e.g, valvole, sono mappabili su device FIWARE)
- Connettore verso FIWARE

# Incontro (2024-09-17)

Esempio di creazione device

```js
{
    "id": "urn:ngsi-ld:Device:unipg:9845A",
    "type": "Device",
    "name": "...",
    "controlledProperty": ["SAP"],
    "dateInstalled": "2024-05-03T11:14:00Z",
    "location": {
        "type": "Point",
        "coordinates": [-3.48043, 40.31308] // [lon, lat] this is located in Madrid
    }, // ...
}
```

Esempio di creazione device meteo

```js
{
    "id": "urn:ngsi-ld:Device:unipg:1234A",
    "type": "Device",
    "controlledProperty": ["humidity", "windSpeed", "temperature"],
    // "value": [0.22, "nan", 21.2], ...
}
```

Esempio di update a seguito di nuovo measurement

```js
{
    "id": "urn:ngsi-ld:Device:unipg:9845A",
    "type": "Device",
    "value": [0.22],
    "dateObserved": "2024-05-04T10:00:00Z"
}
```

# Data models (UniBO)

- [WaterMeter (lorawan)](https://fiware-datamodels.readthedocs.io/en/stable/Environment/WaterQualityObserved/doc/spec/index.html)