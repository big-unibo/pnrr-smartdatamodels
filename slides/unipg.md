{{< include guide.md >}}

# Incontro 2024-05-20

- Particelle: AgriParcel
- Device: Meteo, Coltivazione (device distinti)
- Immagini: Camera (in standby)

Esempio di creazione device

```js
{
    "id": "urn:ngsi-ld:Device:unipg:9845A",
    "type": "Device",
    "name": "...",
    "controlledProperty": ["SAP"],
    "value": [21.2],
    "dateInstalled": "2024-05-03T11:14:00Z",
    "dateObserved": "2024-05-03T11:14:00Z",
    "location": {
        // GeoJSON location. Da impostare solo in fase di creazione se sensore è statico
    }
}
```

Esempio di creazione device meteo

```js
{
    "id": "urn:ngsi-ld:Device:unipg:1234A",
    "name": "...",
    "type": "Device",
    "controlledProperty": ["humidity", "windSpeed", "temperature"],
    "value": [0.22, "nan", 21.2],
    ...
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

# Incontro 2024-05-03

Contesto:  Misurazioni su coltivazioni erbacee.

Collezione dati:

- Diverse tipologie di sonde puntuali;
- Misurazioni distruttive;
- Immagini/Video (as of deliverable)

Collezione as of now:

- Excel con misurazioni storiche fatte in campo (o in post-processing).
- Poche tuple (qualche migliaio)
- Nice to have (non utilizzati al momento): dati satellitari 
- NO georeferenziazione (di default)

Sensori:

- Puntuali
- Camere (su UAV) e.g. infrared, multispectral (as of deliverable)

Goal analisi

- Machine learning / addestramento modelli per suggerire trattamenti e/o irrigazioni.
- No output formale al momento, solo discussioni con parte agro

# Integration steps (UniBO + UniPG)

- Step 1: Determine which data to upload + georeferencing data (UniPG)
- Step 2: Determine which Smart Data Model fits the needs and the needed mappings (meeting UniBo + UniPG)
- Step 3: Upload historical processed data (structured) into platform (UniPG)
- Step 5 (nice to have): Upload raw data on platform (UniPG + UniBo)
- Step 6 (nice to have): Deploy docker processing containers on platform (UniPG + UniBo)
