#!/bin/bash
stty sane
stty $tty_opts
stty cols $tty_width
stty rows $tty_height
bash $@
docker stop $cid