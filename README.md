# Mip-matching

**mip_matching** er en Python-pakke for å tildele intervjutider til søkere basert på ledige tider for søkere og komitéer.

Pakken brukes i [opptakssystemet til Linjeforeningen Online](https://github.com/appKom/cappelini). 

Algoritmen baserer seg på MIP-programmering (Mixed Integer Linear Programming). Se [Modellering.md](./src/Modellering.md) for detaljer.

## Installering

Pakken kan installeres med pip:
```bash
python -m pip install mip-matching @ git+https://github.com/appKom/vermicelli.git
```

Eller putt følgende i `requirements.txt`-filen:
```
mip-matching @ git+https://github.com/appKom/vermicelli.git
```