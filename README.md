[![Build Status](https://travis-ci.org/sustineri/sustineri.svg?branch=master)](https://travis-ci.org/sustineri/sustineri)

# Sustineri

A project for the HackZurich 2018.

## Prerequisites

* Docker 18 or later

## Setup

```bash
# Get the code, cd to sustineri, setup sustineri in Docker
git clone git@github.com:lucachristen/sustineri.git \
    && cd sustineri \
    && make 
```

## Run

```bash
make start
```

## Server API

### POST `/api/post_something`

**Required:**
```json
{
    "hello": "test",
}
```

**Result:**
```json
{
    "hello": "test"
}
```

### GET `/api/get_something`

**Result:**
```json
{
    "hello": "world"
}
```

## Idea

- [ ] Screen 1  
* Defintion Reduction des "CO2" Werte
- [ ] Screen 2  
* Übersicht pro Kunde und Woche des co2 wertes
- [ ] Screen 3  
* Brackdown auf die einzelnen Kategorien
- [ ] Screen 4  
* Investment Screen mit Empfehlung, in welche Produkte investiert werden muss, um die Reductionsziele zu erreichen       
- [ ] Screen 5  
* eBanking Screen mit Transctions-Daten und sustineri-Widget

## Tasks 

- [ ] Application Deployment  
- [ ] PDF Parsing  
- [ ] Expose Bühler Data via API  
- [ ] Matching Receipt to Bühler Products  
- [ ] Create Frontend  
- [ ] Suggest environmentally friendly ETF based on current Co2 use

*Optional*
- [ ] Connect to AXA Health and find out your food healthyness
