{{< include guide.md >}}

# UniPG (2024-05-03)

Contesto: 

Collezione dati:

- 
   
Goal analisi

- 

# Integration steps (UniBO + UniPG)

- Step 1: 
- Step 2: 
- Step 3: 
- Step 4: 
- Step 5: 

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