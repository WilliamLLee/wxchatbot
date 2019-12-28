#!/bin/bash
echo "Begin deploy chatbot"
source venv/bin/activate
python train.py
python retrain.py
nohup python main.py 80 &
echo "finish deploy"