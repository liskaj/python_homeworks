# Přehled

## Komponenty

### Database
Kontejner obsahuje databázový server běžící na databázi MongoDB.

### Importer
Kontejner obsahuje skript pro načtení dat ze souboru [pwr_consumption.csv](./data/pwr_consumption.csv). Soubor obsahuje informace o spotřebě energie z portalů ČEZ Distribuce.

### API
Kontejner obsahuje REST Server, který umožňuje přistupovat k datům v databázi prostřednictvím REST API:

#### GET power_consumption

##### Parametry
| název | typ       | datový typ    | popis       |
|-------|-----------|---------------|-------------|
| from  | Volitelný | číslo (epoch) |             |
| to    | Volitelný | číslo (epoch) |             |

## Spuštění
Pro spuštění použijte následující příkaz:
`docker-componse up -d`

Přikaz postupně spustí všechny tři kontejnery na pozadí.

Pro ukončení použijte:
`docker-componse down`

## Poznámky
1. Je třeba nainstalovat poslední aktualizaci pro Docker a WSL.