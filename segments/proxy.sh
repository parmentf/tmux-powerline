
run_segment() {

    local proxy=$(cat /opt/inist-tools/env/.it_env_shell)
    if [[ $proxy -eq "0" ]]; then
        echo "#[fg=colour202]🛡  Proxy"
    fi
    return 0
}