@echo off
PUSHD ..\tests

docker run -it --rm  --name web_hw_07  lexxai/web_hw_07

rem docker volume ls
                    

POPD