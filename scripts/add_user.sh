#!/bin/bash
# This script creates a new user on the server and authorizes the user
# using the public key from the user's application email.
# Only administrators with sudo privileges can execute this script.

# Usage:
#   1) Upload the user's public key file to your directory
#   2) Run command `sudo ./add_user.sh username /path/to/user_key_file.pub`
###########################################################################


# validate arguments
if [ $# != 2 ]; then
    echo "Usage: $0 username user_key.pub"
    echo "E.g.: $0 zhangsan ~/zhangsan.pub"
    exit 1
fi

username=$1
user_key=$2

# validate user's public key file
if [ ! -f $user_key ]; then
    echo "Error: $user_key not found."
    echo "Create user '$username' unsuccessfully :("
    exit -1
elif [ "${user_key##*.}"x != "pub"x ]; then
    echo "Error: $user_key is not a valid public rsa key."
    echo "Create user '$username' unsuccessfully :("
    exit -1
fi
# rename user's public key file
pub_key=~/$username.pub
mv $user_key $pub_key

# add user
echo "sudo adduser $username"
sudo adduser $username

# configure user's public key in .ssh dir
ssh_dir=/home/$username/.ssh
if [ ! -d $ssh_dir ]; then
    echo "create .ssh dir in: $ssh_dir"
    sudo mkdir $ssh_dir
fi
if [ ! -f $ssh_dir/$pub_key ]; then
    sudo cp $pub_key $ssh_dir
fi
auth_keys=$ssh_dir/authorized_keys
echo "cat $user_key >> $auth_keys"
cat $pub_key | sudo tee -a $auth_keys >/dev/null
sudo chmod 600 $auth_keys
sudo chmod 755 $ssh_dir
sudo chown -R $username:$username $ssh_dir

echo "delete $user_key"
rm $pub_key
echo "Create user '$username' successfully :)"
