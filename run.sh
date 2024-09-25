#!/bin/sh

echo Sleep 1...
sleep 1
/usr/local/bin/alembic upgrade head  
python src/main.py