
# misc

General use repository for code snippets and its descritpions grouped by purpose

## By the way, some in-hand commands
- Reset local keys with blank password:
    ```bash
    ssh-keygen -q -N "" -t ed25519
    ```

- Check how many CPUs are there in Linux system:
    ```bash
    lscpu 
    cat /proc/cpuinfo
    top 
    htop 
    nproc 
    dmidecode -t processor 
    getconf _NPROCESSORS_ONLN 
    ```

### References
[Markdown Basic Syntax](https://www.markdownguide.org/basic-syntax/)
