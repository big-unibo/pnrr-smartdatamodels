---
title: Introduction on smart data models
date: 2024-04-18
format:
  revealjs: 
    footer: "Spoke 3 - University of Bologna"
---

# Data platform

![image](https://github.com/big-unibo/pnrr-smartdatamodels/assets/18005592/68bac582-6104-4cc7-b514-c1e837600a9d)

# Integration with the data platform

Two levels of integration

1. Data
  1. Upload raw data
  2. Process your data on your machine and upload processed data
2. Processes
  3. Move the processing directly to the platform

Collection APIs​

- Black box​: raw files
- White box​ (intelligible): JSON documents with known schemas

Data processes​

- Platform: internal processes known to the platform, typically shared tasks and standard data processing (Spark, Kafka, and Docker containers)​
- User: black-box processes that implement partner-specific analytics (Docker containers)​
- Abbiamo acquistato 2 GPU NVIDIA RTX™ 6000 Ada Generation (48 GB GDDR6)

# Data collection

Data collection comes with 2 (main) interfaces: FTP and FIWARE

- FTP (File Transfer Protocol) is a network protocol for transmitting files between computers over Transmission Control Protocol/Internet Protocol (TCP/IP) connections
- FIWARE open source enabler for data collection

Two main data types:

- Black box (images, videos) as files through FTP 
- Intelligible JSON documents as files through FTP or to FIWARE through HTTP requests

Integrating with FTP is "easy": given user/password, upload files into the platform

# FIWARE

FIWARE offers APIs to upload/get/update the data.

- Examples of APIs are available [here](https://documenter.getpostman.com/view/513743/RWToNwzF#8ff1dc7a-3929-4e5b-a6c1-0b4a8074cc03) 
- Example of request

        curl --location 'http://localhost:1026/v2/entities/' \​
             --header 'Content-Type: application/json' \​
             --data ' {​
                 "id":"CropDevice010",
                 "type":"Device",​
                 "observedProperty": ["speed"],​
                 "value": [5]​
             }'

# Smart data models

Either we use FTP or FIWARE, for intelligible documents we need to define a shared vocabulary and format, preferably FIWARE Smart Data Models


What is the Smart Data Models Initiative?

- Joint collaboration initiative to support the adoption of a reference architecture and compatible common data models that underpin a digital market of interoperable and replicable smart solutions in multiple sectors, starting with Smart Cities.
- A smart data model includes four elements: the schema, or technical representation of the model defining the technical data types and structure, the specification of a written document for human readers, a URI with a working URL with basic data about the attribute or the entity, and the examples of the payloads for NGSIv2 and NGSI-LD versions.
- All data models are public and of royalty-free nature. The licensing mode grants 3 rights to the users:
    - Free use
    - Free modification
    - Free sharing of the modifications

Some examples:

- [AgriParcel (Environment)​](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Agrifood/AgriParcel/swagger.yaml)
- [Device (Measurement + Agent)​](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Device/Device/swagger.yaml)
- [DeviceMeasurement (Measurement)​](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Device/DeviceMeasurement/swagger.yaml)

# Example: [Device](https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Device/Device/swagger.yaml)

An apparatus (hardware + software + firmware) intended to accomplish a particular task (sensing the environment, actuating, etc.).

```js
{
  "id": "device-9845A",
  "type": "Device",
  "deviceCategory": ["sensor"],
  "controlledProperty": ["fillingLevel", "temperature"],
  "batteryLevel": 0.75,
  "serialNumber": "9845A",
  "value": [D0.22, 21.2],
  "deviceState": "ok",
  "dateFirstUsed": "2014-09-11T11:00:00Z",
  "owner": ["http://person.org/leon"]
}
```

# Questions on data collection

- What is the volume and amount of data?
- What are the main subjects of the analysis? In other words, what data are valuable for your analysis?