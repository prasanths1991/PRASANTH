#!/bin/bash
pip install -r requirements.txt
python -m virtualenv afour
.\afour\Scripts\activate
python pattern.py
python flight_status.py
sleep 10
deactivate
