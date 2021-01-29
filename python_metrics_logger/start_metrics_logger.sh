#!/bin/bash
# Absolute path to this script, e.g. /home/user/bin/start_metrics_logger.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
# Start the metrics logger in the background
nohup python $SCRIPTPATH/metricslogger.py >> metricslogger.log 2>&1 &
