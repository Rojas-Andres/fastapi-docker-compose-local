#!/bin/sh

uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload