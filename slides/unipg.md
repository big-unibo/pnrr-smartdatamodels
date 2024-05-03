{{< include guide.md >}}

# UniPG (2024-05-03)

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
- Step 2: Determine which Smart Data Model fit the needs and the needed mappings (meeting UniBo + UniPG)
- Step 3: Upload historical processed data (structured) into platform (UniPG)
- Step 5 (nice to have): Upload raw data on platform (UniPG + UniBo)
- Step 6 (nice to have): Deploy docker processing containers on platform (UniPG + UniBo)


# Data models (UniBO)

- Meteo potrebbe servire per post-processing
- *AgriFarm*: mapping Cadriano. Sentire con contatti (~fine Maggio) per avere rilevazioni GPS puntuali e fare mappatura.
- *Single tree*: completely missing in terms of data models. Do we need entities or is it a simple measurement?
- *Task*: useful information from `metadata.yaml`
    - Name/Description (linguaggio naturale)
    - Goal: monitoring
    - Data start/end, duration
    - CropType e interfilare (informazioni che prendo da AgriParcel, cioè quando registro il task specifico la parcel in cui è avvenuto)
    - Location (traiettoria linestring Geojson)
    - How many cameras/video streams
- *Device*
    - Cameras (there is a specific entity [Camera](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Device/Camera/swagger.yaml))
        - How many FPS
        - How many images per camera
        - Positioning with respect to the center of mass of the robot
    - Simple (camera) vs composite (robot) device