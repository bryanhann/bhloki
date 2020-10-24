
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


_alias wl   $PWD/wl
_alias ti   $PWD/wl -i pytest
_alias tn   $PWD/wl -n

