{{< include guide.md >}}

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
- Step 5: (POLIMI) moving the processing to the platfrom using docker

# Data models (UniBO)

- *AgriFarm*: mapping Cadriano 
- *Single tree*: completely missing in terms of data models. Do we need entities or is it a simple measurement?
- *Task*: useful information from `metadata.yaml`
    - Goal: monitoring
    - Data start/end
    - Duration
    - How many cameras/video streams
- *Device*
    - Cameras (there is a specific entity [Camera](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Device/Camera/swagger.yaml))
        - How many FPS
        - How many images per camera
        - Positioning with respect to the center of mass of the robot
    - Simple (camera) vs composite (robot) device