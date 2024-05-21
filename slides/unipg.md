{{< include guide.md >}}

# Incontro 2024-05-20

- Particelle: AgriParcel
- Device: Meteo, Coltivazione (due device distinti)
- Immagini: Camera (in standby)

## Esempio di creazione device

```js
{
    "id": "device-001",
    "type": "Device",
    "name": "...",
    "controlledProperty": ["SAP"],
    "value": [21.2],
    "dateCreated": "...",
    "dateUpdated": "...",
    "location": {
        // GeoJSON location. Da impostare solo in fase di creazione se sensore è statico
    }
}
```

Esempio di creazione device meteo
```js
{
    "id": "device-9845A",
    "name": "...",
    "type": "Device",
    "controlledProperty": ["humidity", "windSpeed", "temperature"],
    "value": [0.22, "nan", 21.2],
    ...
}
```

## Esempio di update rilevazione device

```js
{
    "id": "device-001",
    "type": "Device",
    "value": [0.22],
    "dateUpdated": "..."
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