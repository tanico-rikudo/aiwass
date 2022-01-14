#!/bin/bash 

#load common setting
eval 'source $BASE_DIR/geco_commons/shell/shell_config.conf'

function usage() {
cat <<_EOT_
Usage:
  $0 [-e fee]

Description:
  Launch aiwass api server

Options:
  -e  No assigned
_EOT_
exit 1
}

if [ "$OPTIND" = 1 ]; then
  while getopts e:h OPT
  do
    case $OPT in
      e)
        MODE=$OPTARG
        ;;
      h)
        usage
        ;;
      \?)
        echo "Try to enter the h option." 1>&2
        ;;
    esac
  done
else
  echo "No installed getopts-command." 1>&2
  exit 1
fi

shift $((OPTIND - 1))
source deactivate
source activate py37
python_interpritor=python
execute_path=$AIWASS_DIR
echo ${execute_path} 
cd ${execute_path}
command="${python_interpritor} run.py 1>${AIWASS_LOG} 2>${AIWASS_LOG}"

echo $command
eval $command
