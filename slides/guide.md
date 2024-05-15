---
title: Introduction to data platform integration and smart data models
date: 2024-04-18
format:
  revealjs: 
    footer: "Spoke 3 - University of Bologna"
---

# Data platform

![The data platform](https://github.com/w4bo/img-dump/assets/18005592/92c7a892-daec-4c17-851f-b05dba44c92e)

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

# Data model

![Data model](https://github.com/w4bo/img-dump/assets/18005592/6eb62a1e-084c-4dbe-ae4b-a94652ac0edb)

# Data collection

Collection of two main data types:

- Black box (images, videos) as files through SFTP 
- White box (JSON documents) as files through SFTP or to FIWARE through HTTP requests

Data collection comes with 2 (main) interfaces: SFTP and FIWARE

- *SFTP* (File Transfer Protocol through SSH) is a network protocol for transmitting files between computers over SSH connections
- *FIWARE* open source enabler for data collection

# SFTP

Integrating with SFTP is easy

- We give you user/password
- You upload files into the platform
  - E.g., using Filezilla
    - URL: `sftp://<IP>`
    - Port: `40021`
- Uploaded files are accessible only by its proprietary user
- Can only write data to the `data/` folder

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

Either we use SFTP or FIWARE, for intelligible documents we need to define a shared vocabulary and format, preferably FIWARE Smart Data Models

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
    "value": [0.22, 21.2],
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

# Example: [Camera](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Device/Camera/swagger.yaml)

A Data Model for camera installations in a city.

```js
{
  "id": "urn:ngsi-ld:Camera:Cam2",
  "type": "Camera",
  "cameraName": "Cam2",
  "streamName": "Agartala_OrientChowmuhani_Surv_Fixed_RSBhawan_Cam2",
  "streamURL": "https://drive.google.com/file/d/1eNmgWDvb2R34o03cZ9dPXrtEvsreQzQ4/view?usp=sharing",
  "imageSnapshot": "https://drive.google.com/file/d/1cLMYzvbaciGcRRD0HV3MAoK4XbNkOukr/view?usp=sharing",
  "cameraUsage": "SURVEILLANCE",
  "cameraType": "FIXED",
  "endDateTime": "2021-05-11T06:35:20.065Z",
  "startDateTime": "2021-05-11T06:30:00.020Z",
  "cameraOrientation": {
    "comments": "Camera facing RSBhawan",
    "annotatedMap": "https://drive.google.com/file/d/1RXDGogU5UMmzRppqFaNKTzcr69Kl0wjb/view?usp=sharing"
  },
  "location": {
    "type": "Point",
    "coordinates": [
      91.28076,
      23.831796
    ]
  },
  "cameraNum": 2,
  "on": true
}
```

# Example: [AgriFarm](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Agrifood/AgriFarm/swagger.yaml) ([AgriFood](https://github.com/smart-data-models/dataModel.Agrifood) domain)

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

# Example: [AgriParcel](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Agrifood/AgriParcel/swagger.yaml) ([AgriFood](https://github.com/smart-data-models/dataModel.Agrifood) domain)

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

# The `location` attribute

Georeferenced entities *must have* the `location` attribute

```js
"location": {
    "type": "Point",
    "coordinates": [-3.48043, 40.31308]
}
```

In FIWARE,

- Locations are represented using the [GeoJSON standard (RFC 7946)](https://datatracker.ietf.org/doc/html/rfc7946) (Point, LineString, Polygon), check [here](https://geojson.io/#map=2/0/20) to create valid GeoJSON geometries
- Coordinates must be represented using the standard WGS84 [EPSG:4326](https://en.wikipedia.org/wiki/EPSG_Geodetic_Parameter_Dataset) (2D coordinate reference system (CRS))
    - The one used by Google

# The `id`, `type`, and `name` attributes

- `type`: must be equal to the used smart data model
- `id`: must come with the pattern `urn:ngsi-ld:<type>:<uuid>`
    - `<type>` same as above
    - `<uuid>` check [here](https://en.wikipedia.org/wiki/Universally_unique_identifier#Textual_representation) to get a universal identifier
- `name`: user-friendly name of the entity

Example 

```js
{
    "id": "urn:ngsi-ld:Camera:9ea60389-9246-4dda-a083-3e3bcb444131",
    "type": "Camera",
    "name": "Front Camera RGB",
    ...
}
```

# The `timestamp` and `date` attributes

- `timestamp` must be set using [UNIX timestamp (in seconds)](https://www.unixtimestamp.com/) (e.g., 1714734840)
- `date*` must be formatted according to the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) (e.g., "2024-05-03T11:14:00Z")
