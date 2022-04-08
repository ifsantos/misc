
# Expanding partition to fill disk free space

1. lsblk

2. sudo growpart /dev/sdX1 1

3. sudo resize2fs /dev/root

4. df -h 
