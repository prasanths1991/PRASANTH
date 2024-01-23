#!/bin/bash
pip install -r requirements.txt
python -m virtualenv afour
.\afour\Scripts\activate
python PATTERN/pattern.py
python FLIGHT/flight_status.py
sleep 10
deactivate
