
# How to set an authorized folder on samba share

 1. Make sure that every user can access the common media folder on the unix side (without samba); alternatively, you can set force user in *smb.conf*
 2. Make sure each user has a samba password set. You can set it with:  
        
        sudo smbpasswd -a your_user

 3. Look at */etc/samba/smb.conf*: check if the line *security = your_user* is set in the *[GLOBAL]* section
 4. Set your shares in */etc/samba/smb.conf*, see example for single user share:

        [special]
            path = /home/your_user/only_your_user
            read only = no
            writeable = yes
            browseable = yes
            valid users = one
            create mask = 0640
            directory mask = 0750

5. Restart the samba server after the changes with:

        sudo service smbd restart
        # or     
        sudo systemctl restart smbd.service

6. After the changes, reload the configs:

        smbcontrol all reload-config

Enjoy your authoryzed shared folder! 

Thanks :)
