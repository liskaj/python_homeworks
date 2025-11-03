# Přehled

## Komponenty
Aplikaci tvoří 3 kontejnery popsané níže. Kontejnery jsou spojené do sítě `app-net`.

### Database
Kontejner obsahuje databázový server běžící na databázi MongoDB. Databáze slouží k ukládání dat o spotřebě energie. Data jsou získávána manuálním exportem z portálu ČEZ Distribuce.

Struktura:
- energy - databáze
  - power_consumption - kolekce

### Importer
Kontejner obsahuje skript pro načtení dat ze souboru [pwr_consumption.csv](./data/pwr_consumption.csv). Soubor obsahuje informace o spotřebě energie z portalů ČEZ Distribuce.

### API
Kontejner obsahuje REST Server, který umožňuje přistupovat k datům v databázi prostřednictvím REST API:

#### GET power_consumption

##### Parametry
| název | typ       | datový typ                   | popis       |
|-------|-----------|------------------------------|-------------|
| from  | Volitelný | číslo (čas ve formátu epoch) |             |
| to    | Volitelný | číslo (čas ve formátu epoch) |             |

## Spuštění
Pro spuštění použijte následující příkaz:
`docker-componse up -d`

Přikaz postupně spustí všechny tři kontejnery na pozadí.

Pro ukončení použijte:
`docker-componse down`

## Poznámky
1. Je třeba nainstalovat poslední aktualizaci pro Docker a WSL.
2. V případě změn je potřeba znovu vyztvořit kontejner příkazem `build`:
   `docker-componse build <<název kontejneru>>`
