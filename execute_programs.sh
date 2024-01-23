#!/bin/bash
pip install -r requirements.txt
python -m virtualenv afour
source .\afour\Scripts\activate
python PATTERN/pattern.py
python FLIGHT/find_flight_status.py
sleep 10
deactivate
