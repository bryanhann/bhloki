
_alias () {
    key=$1
    shift
    alias $key="$*"
}

clean () {
    rm -rf  o
    rm -rf o.*
    rm -rf *.egg-info
}


_alias wl   $PWD/with-venv
_alias ti   $PWD/with-venv -i pytest
_alias tn   $PWD/with-venv -n

