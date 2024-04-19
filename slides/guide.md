---
title: Introduction to data platform integration and smart data models
date: 2024-04-18
format:
  revealjs: 
    footer: "Spoke 3 - University of Bologna"
---

# Data platform

![The data platform](https://github.com/big-unibo/pnrr-smartdatamodels/assets/18005592/68bac582-6104-4cc7-b514-c1e837600a9d)

# Integration with the data platform

Two levels of integration

1. *Data*
    1. Upload raw data
    2. Process your data on your machine and upload the processed data
2. *Processes*
    3. Move the processing to the platform

Collection APIs​

- *Black box*​: raw files
- *White box*​ (intelligible): JSON documents with known schemas

Data processes​

- **Platform**: internal processes known to the platform, typically shared tasks and standard data processing (Spark, Kafka, and Docker containers)​
- **User**: black-box processes that implement partner-specific analytics (Docker containers)​
    - Abbiamo acquistato 2 GPU NVIDIA RTX™ 6000 Ada Generation (48 GB GDDR6)

# Data collection

Data collection comes with 2 (main) interfaces: FTP and FIWARE

- *FTP* (File Transfer Protocol) is a network protocol for transmitting files between computers over TCP/IP connections
- *FIWARE* open source enabler for data collection

Collection of two main data types:

- Black box (images, videos) as files through FTP 
- White box (JSON documents) as files through FTP or to FIWARE through HTTP requests

Integrating with FTP is "easy": given user/password, upload files into the platform

# FIWARE

FIWARE offers APIs to upload/get/update the data.

- Examples of APIs are available [here](https://documenter.getpostman.com/view/513743/RWToNwzF#8ff1dc7a-3929-4e5b-a6c1-0b4a8074cc03) 
- Example of request

        curl --location 'http://localhost:1026/v2/entities/' \​
             --header 'Content-Type: application/json' \​
             --data ' {​
                 "id": "CropDevice010",
                 "type": "Device",​
                 "observedProperty": ["speed"],​
                 "value": [5]​
             }'

# Smart data models

Either we use FTP or FIWARE, for intelligible documents we need to define a shared vocabulary and format, preferably FIWARE Smart Data Models


What is the **Smart Data Models Initiative**?

- Joint collaboration to *support the adoption of a reference architecture and compatible common data models* that underpin interoperable and replicable solutions in multiple sectors
- A smart data model *includes four elements*: 
    - The schema
    - The specification of a written document for human readers
    - URI with a working URL with basic data about the attribute or the entity
    - Examples of the payloads for NGSIv2 and NGSI-LD versions.
- All data models are public and of *royalty-free nature*. The licensing mode grants 3 rights to the users:
    - Free use, free modification, free sharing of the modifications

Some examples:

- [AgriParcel (Environment)​](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Agrifood/AgriParcel/swagger.yaml)
- [Device (Measurement + Agent)​](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Device/Device/swagger.yaml)
- [DeviceMeasurement (Measurement)​](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Device/DeviceMeasurement/swagger.yaml)

# Questions on data collection and integration

1. Describe the processes for collecting/producing the data
    1. What is the volume and amount of data?
    1. What are the main subjects of the analysis? In other words, what data are valuable for your analysis?
1. What are the potential FIWARE data models to represent your data?

# Example: [Device](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Device/Device/swagger.yaml)

An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).

```js
{
    "id": "device-9845A",
    "name": "Top-right Camera",
    "type": "Device",
    "deviceCategory": ["sensor"],
    "controlledProperty": ["fillingLevel", "temperature"],
    "value": [D0.22, 21.2],
    "batteryLevel": 0.75,
    "serialNumber": "9845A",
    "deviceState": "ok",
    "dateFirstUsed": "2014-09-11T11:00:00Z",
    "owner": ["http://person.org/leon"],
    "location": {
        "type": "Point",
        "coordinates": [-3.48043, 40.31308]
    }
}
```

# Example: [AgriFarm](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Agrifood/AgriFarm/swagger.yaml) and [AgriParcel](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Agrifood/AgriParcel/swagger.yaml) ([AgriFood](https://github.com/smart-data-models/dataModel.Agrifood) domain)

**AgriFarm**: a generic farm made up of buildings and parcels

```js
{
    "id": "urn:ngsi-ld:AgriFarm:001",
    "name": "Wheat farm",
    "type": "AgriFarm",
    "description": "A farm producing wheat",
    "dateCreated": "2017-01-01T01:20:00Z",
    "dateModified": "2017-05-04T12:30:00Z",
    "location": {
        "type": "Polygon",
        "coordinates": [[[100, 0], [101, 0], [101, 1], [100, 1], [100, 0]]]
    },
    "ownedBy": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",
    "hasAgriParcel": [
        "urn:ngsi-ld:AgriParcel:001" //, ...
    ]
    "hasBuilding": [ ... ],
}
```

**AgriParcel**: a generic parcel of land

```js
{
    "id": "urn:ngsi-ld:AgriParcel:001",
    "type": "AgriParcel",
    "dateCreated": "2017-01-01T01:20:00Z",
    "dateModified": "2017-05-04T12:30:00Z",
    "location": {
        "type": "Polygon",
        "coordinates": // ...
    },
    "area": 200,
    "description": "Spring wheat",
    "category": "arable",
    "belongsTo": "urn:ngsi-ld:AgriFarm:001",
    "ownedBy": "urn:ngsi-ld:Person:fce9dcbc-4479-11e8-9de1-cb228de7a15c",
    "hasAgriCrop": "urn:ngsi-ld:AgriCrop:36021150-4474-11e8-a721-af07c5fae7c8",
    "cropStatus": "seeded",
    "lastPlantedAt": "2016-08-23T10:18:16Z",
    "hasAgriSoil": "urn:ngsi-ld:AgriSoil:429d1338-4474-11e8-b90a-d3e34ceb73df",
    "hasDevice": [
        "urn:ngsi-ld:Device:4a40aeba-4474-11e8-86bf-03d82e958ce6", // ...
    ],
    "soilTextureType": "Clay",
    "irrigationSystemType": "Drip irrigation"
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

# Integration steps

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