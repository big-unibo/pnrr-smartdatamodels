{{< include guide.md >}}

# POLIMI (2024-04-28)

Esempio di Task (nelle slides precedente le specifiche per compilare `id`, `location`, `date*`)

```js
{
    "id": "urn:ngsi-ld:Task:polimi:....",
    "type": "Task",
    "name": "Weeding",
    "description": "Automatically weeding a parcel on 2024-04-01",
    "hasWorkingArea": "<id agrifarm/agriparcel>",
    "location": {
        "type": "LineString",
        "coordinates": [
            [-3.4817, 40.3133],
            [-3.4817, 40.3134],
            // ...
        ]
    },
    "dateStart": "2012-04-13T10:52:00Z",
    "dateEnd": "2012-04-13T10:57:00Z",
    "status": "finished",
    "result": "ok",
}
```

# POLIMI (2024-04-18)

Contesto: ricerca su vigneto località Cadriano.

Collezione dati:

- Raccolta di video multispettrali tramite diverse tipologie di telecamere (e.g. RGB, LIDAR Ouster OS0) posizionate su robot su 4 colture
- Ogni raccolta dati è di ~100GB​. 2 volte/mese​. 200 GB/mese​. 200GB * 8 mesi = 1.6TB​
- Bag ROS2 (5 telecamere). FILE ~100GB (check di FTP su performance, scp/rsync)​
    - Point cloud (lista 65K punti x, y, z). LIDAR margine di errore in mm​
    - `metadata.yaml`: fornisce info sulla ROS bag
    - Immagini 2D (identificazione di frutti, proietto immagine in point cloud)​
   
Goal analisi

- Riconoscere (e.g. clustering) ed estrarre informazioni sulle singole piante: contare fiori/frutti, stato di salute, livelli di azoto, etc. con l'obbiettivo di suggerire trattamenti (pesticidi, fertilizzanti, etc.)

# Integration steps (UniBO + POLIMI)

- Step 1: (UniBO) Mapping Cadriano
- Step 2: (POLIMI) Upload ROS bag and `metadata.yaml` files using FTP/SCP after every mission
- Step 3: (UniBO) visualization of such data in a georeferenced map
- Step 4: (POLIMI) upload the synthetic/processed data from bags (computed outside the platform)
- Step 5: (POLIMI) moving the processing to the platform using docker

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