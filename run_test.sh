#!/bin/bash
source nenv/bin/activate
pip install -r requirements.txt
pytest
