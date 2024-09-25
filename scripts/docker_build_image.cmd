@echo off
PUSHD ..

docker build . -t lexxai/web_hw_07
docker images

POPD