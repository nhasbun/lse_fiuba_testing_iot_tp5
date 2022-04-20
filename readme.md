# Testing IoT TP5
_Puerto Montt, 19 de abril de 2022, Nicolás Hasbún A._

Trabajo práctico 5 consiste en agregar iniciales estrategias de seguridad como 
parte del Master Test Plan entregado en la cursada y de la que se deja respaldo 
en este repositorio.

## Quick Install

* Python 3.6+ compatible library.

```bash
python3 -m venv venv && . ./venv/bin/activate && \
pip install -U pip setuptools wheel && \
pip install -e .
```

## Run Tests

```bash
. ./venv/bin/activate
pytest -v
```