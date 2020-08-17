#!/bin/bash

collect_port=0
port="8080"
delim='='

for var in "$@"
do
    if [ "$collect_port" == "1" ]; then
       port=$var
       collect_port=0
    fi

    splitarg=${var%%$delim*}

    if [ "$splitarg" == "--port" ]; then
       if [ ${#splitarg} == ${#var} ]; then
         collect_port=1
       else
         port=${var#*$delim}
       fi
    fi
done

/etc/ou_module/tutorial_update.sh &

echo ""
echo ""
echo "#######################################################"
echo "You can now access the system at http://127.0.0.1:$port"
echo "#######################################################"
echo ""

EXTERNAL_PORT=''

if [ -z "$JUPYTERHUB_SERVICE_PREFIX" ]; then
    JUPYTERHUB_SERVICE_PREFIX='/'
    EXTERNAL_PORT=":$port"
fi

pserve /etc/ou_module/tutorial-server-config.ini http_port=${port} proxy_prefix="$JUPYTERHUB_SERVICE_PREFIX" home="${HOME}"
