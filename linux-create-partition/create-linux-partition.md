
# Creating linux partition on disk free space

1. Verify the partitions available on the server: 

        fdisk -l

2. Choose which device you wish to use (such as /dev/sda or /dev/sdb)
3. Run fdisk as follows (where X is the device you would like to add the partition to):

        fdisk /dev/sdX

4. Type ‘n’ to create a new partition.
5. Specify where you would like the partition to end and start.  You can set the number of MB of the partition instead of the end cylinder.  For example:  **+1000M**
6. Type ‘p’ to view the partition, and type ‘w’ to save the partition
7. Run the command below to have the OS detect the new partition table.  If it still does not detect the partition table, you might need a reboot:

        partprobe

8. Format the partition by doing the following, where X is the number of the partition you have created:  

        mke2fs -j /dev/sdaX  

9. Create a directory where you wish to mount the new drive, for example: /newpartition.  

        mkdir -p /newpartition

10. To mount, you can use the following command: 
        
        mount /dev/sdaX /newpartition

11. If you would like the drive to be mounted automatically each time you boot, add the following to /etc/fstab: 

        /dev/sdaX /newpartition ext4 defaults 1 2

For next time we will have a script to automate this.

Thanks :P


### References
 - [Crucial Blog Post](https://www.crucial.com.au/blog/2009/11/18/how-to-create-a-new-partition-on-a-linux-server/?__cf_chl_jschl_tk__=pmd_XMcoD.s2ylnrRhO4.f8afqRZ89W..Lm8kLfnvXET_J8-1630719931-0-gqNtZGzNAmWjcnBszQhl)