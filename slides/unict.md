---
title: Introduction to data platform integration and smart data models
date: 2024-04-18
format:
  revealjs: 
    footer: "Spoke 3 - University of Bologna"
---

{{< include guide.md >}}

# UniCT (2024-04-23)

*Contesto & goal analisi*: stima di probabilità basati su dati georeferenziati

*Collezione dati*:

- Dati in input:
    - Globali: soil grid (raster). Ho degli indicatori per porzione di suolo
    - Regionali: shapefile regionale. No farm.
    - Più immagini e più tipi di sorgenti (38 raster/variabili differenti: meteo, crop, ...)
- Output principale: 
    - Tiff (raster): mappe di presenza/assenza. Ogni pixel contiene 0/1 se non c'è/c'è la pianta
    - Shapefile (vettoriale): altri output, non particolarmente utile per la piattaforma

*Tecnologie*:

- QGIS per analizzare dati
- Maxent: Taglio di raster in base a area di studio, campionamento, e cambio sistema di riferimento
- Vistassm (alternativa a notebook R/python)
- ML: random forest, BRT, ...

# Integration steps (UniBO + UniCT)

- Step 1 (UniBO):
    - Scegliere sistema di riferimento. WGS84, UTM (cartografiche). GeoServer.
    - Accesso a FTP
- Step 2 (UniCT): Quali parametri inserire nel descrittore JSON?
    - Coltura e SDM
    - Predittori scelti e iperparametri (e.g., per Maxent)
    - ... TODO
- Step 3 (UniCT): Caricare mappa di presenza/assenza e descrittore JSON

# Data models (UniBO)

- Principalmente Measurement & Environment
- No farm, si mappa tutta l'area della Sicilia