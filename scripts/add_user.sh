#!/bin/bash

# This script executes sudo commands for adding a new user
# Usage: ./add_user.sh username

username=$1
# the public rsa key file from user's application email
pub_key_file=~/$username.pub

if [ ! -f $pub_key_file ]; then
    echo "Error: $pub_key_file not found."
    echo "create user '$username' unsuccessfully :("
    exit -1
fi

echo "sudo adduser $username"
sudo adduser $username

ssh_dir=/home/$username/.ssh
if [ ! -d $ssh_dir ]; then
    echo "create dir: $ssh_dir"
    sudo mkdir $ssh_dir
fi

if [ ! -f $ssh_dir/$pub_key_file ]; then
    sudo cp $pub_key_file $ssh_dir
fi

echo "cat $pub_key_file >> $ssh_dir/authorized_keys"
cat $pub_key_file | sudo tee -a $ssh_dir/authorized_keys >/dev/null
sudo chmod 600 $ssh_dir/authorized_keys
sudo chmod 755 $ssh_dir
sudo chown -R $username:$username $ssh_dir

echo "remove $pub_key_file"
rm $pub_key_file
echo "create user '$username' successfully :)"
