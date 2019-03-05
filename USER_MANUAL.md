# Server User Manual

##### Recent Updates (2019-3-5): 
* [PyTorch](#323-pytorch) has been updated to the latest stable version **v1.0.1** (CUDA support version: CUDA-10.0) for both Python3 and Python2;
* cuDNN has been updated to v7.4.2;

##### Recent Updates (2018-12-13): 
* [CUDA](#322-cuda-90)-9.2 has been uninstalled;
* PyTorch has been updated to the v1.0 (with CUDA-10.0);
* How to properly use GPUs to run your [tensorflow](#324-tensorflow-v112) program.


##### NOTICE
* If you need to run a program which uses multi-GPUs, please **do not use more than 4 GPU cards**. You can add an environment variable in your terminal to set the specific GPU cards for your program, e.g., 
    Make 'GPU-0', 'GPU-1' and 'GPU-2' available for you:
    ```bash
    export CUDA_VISIBLE_DEVICES=0,1,2
    ```


##### Contents
* [1. Apply for Server Account](#1-apply-for-server-account)
    * [1.1 Checking for exisiting SSH keys](#11-checking-for-exisiting-ssh-keys)
    * [1.2 Generating a new SSH key](#12-generating-a-new-ssh-key)
* [2. Login](#2-login)
    * [2.1 Login with command line](#21-login-with-command-line)
    * [2.2 Login from SSH config file](#22-login-from-ssh-config-file)
    * [2.3 Login from MobaXterm (Windows only)](#23-login-from-mobaxterm-windows-only)
    * [2.4 Port Forwarding](#24-port-forwarding)
    * [2.5 X11 Forwarding](#25-x11-forwarding)
* [3. Softwares](#3-softwares)
    * [3.1 Tools](#31-tools)
    * [3.2 Python and Deep Learning packages](#32-python-and-deep-learning-packages)
        * [3.2.1 Anaconda](#321-anaconda)
        * [3.2.2 CUDA 9.0](#322-cuda-90)
        * [3.2.3 PyTorch](#323-pytorch)
            * [3.2.3.1 torchvision](#3231-torchvision)
            * [3.2.3.1 tensorboardX](#3232-tensorboardx)
        * [3.2.4 TensorFlow](#324-tensorflow)
* [4. Datasets](#4-datasets)

## 1. Apply for Server Account
Please send your following information to any administrator with the subject in the format as **"Apply Server-4 Account_YourName"** to apply a server account:
* Full name
* Email address (frequently used)
* Phone number
* SSH **public key** file named `username.pub` (e.g., `zhangqinchuan.pub`) as an attachment into the email

You can check to see if you have any existing SSH keys you are using on other devices. If you don't have an existing public and private key pair, or don't wish to use any that are available to connect to the server, then [generate a new SSH key](#12-generating-a-new-ssh-key).

For the sake of safety, **it is recommended to [generate a new SSH key](#12-generating-a-new-ssh-key)** to connect to this server.

### 1.1 Checking for exisiting SSH keys
1. Open Terminal.
2. Enter `ls -al ~/.ssh` to see if existing SSH keys are present:
    ```bash
    $ ls -al ~/.ssh
    # Lists the files in your .ssh directory, if they exist
    ```
3. Check the directory listing to see if you already have a public SSH key.

By default, the filename of the public key is `id_rsa.pub`.

### 1.2 Generating a new SSH key
If you don't already have an SSH key, you must generate a new SSH key to use for authentication. If you're unsure whether you already have an SSH key, check for [existing keys](#11-checking-for-exisiting-ssh-keys).

1. Open Terminal (for **Linux** and **Mac**) or [Git Bash](https://git-scm.com/downloads) (for **Windows**).
2. Paste the text below, substituting in your email address.
    ```bash
    $ ssh-keygen -t rsa -b 4096 -P '' -C "your_email@example.com"
    ```
    This creates a new ssh key, using the provided email as a label.
3. When you're prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.
    ```bash
    "Enter a file in which to save the key (/home/username/.ssh/id_rsa):[Press enter]"
    ```
4. Rename the generated public key file `id_rsa.pub` to `$username.pub` (e.g., `zhangsan.pub`).


## 2. Login
### 2.1 Login with command line
1. Open Terminal (for **Linux** and **Mac**) or [Git Bash](https://git-scm.com/downloads) (for **Windows**)
2. Execute the command below, substituting in your username.
    ```bash
    ssh -p port $USERNAME@server_IP
    ```
    
    By default, **the password of your account is the same as your username**.

    **Please change your password after you login the server ASAP** by entering the command below:
    ```bash
    $ passwd
    ```

    You can add a `-i` option to specify your private key for authentication which eliminates the need for typing a password whenever logging in to the server:
    ```bash
    ssh -p port -i ~/.ssh/id_rsa $USERNAME@server_IP
    ```

You can get more information about [SSH command line options]((https://www.ssh.com/ssh/command/#sec-SSH-command-line-options)).

### 2.2 Login from SSH config file
The `ssh` program on a host receives its configuration from either the [command line](#21-login-with-command-line) or from the configuration file `~/.ssh/config`. Setting options in `~/.ssh/config` makes life easier for end users, saves overhead, and reduces support load.

Open (or create) the configuration file `~/.ssh/config` to configure options for your login, e.g.,
<!-- {.line-numbers} -->
```vim
Host host-name  # specify a host name by yourself
    HostName server_IP  # IP address
    User $USERNAME
    Port port
    IdentityFile ~/.ssh/id_rsa  # the path to your private key
```

After the configuration, you can easily login the server by the command below:
```bash
$ ssh host-name
```

If you need to transfer files between the server and your local host, you can use `scp` or `sftp` command, e.g.,
* Copy a file from your local host to the server:
    ```bash
    $ scp /path_to_your_file host-name:~/dst_path_under_your_root_directory
    ```
You can get more information about the usage of **[scp](https://linux.die.net/man/1/scp)** and **[sftp](https://linux.die.net/man/1/sftp)**
You can get more information about [commonly used SSH configuration options](https://www.ssh.com/ssh/config/#sec-Commonly-used-configuration-options).

### 2.3 Login from MobaXterm (Windows only)
1. Download and install [MobaXterm](https://mobaxterm.mobatek.net/download-home-edition.html)
2. Create a new remote session by click the "Session" button
![Create a session](https://raw.githubusercontent.com/SJTU-VLG/server_utilities/master/imgs/mobaxterm_create_session.jpg)
3. Configure the session as the instructions below:
![Config a session](https://raw.githubusercontent.com/SJTU-VLG/server_utilities/master/imgs/mobaxterm_config_session.png)
4. When you have configured a session, you can easily login the server by double clicking the session icon in the side bar.
![Start a session](https://raw.githubusercontent.com/SJTU-VLG/server_utilities/master/imgs/mobaxterm_side_bar.jpg)


### 2.4 Port Forwarding
When you are using [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/latest/public_server.html) or some other **Web servers** (e.g., [tensorboard](https://www.tensorflow.org/guide/summaries_and_tensorboard)), you will find that you can only connect the server through port `port` and all the other ports are closed. So you need to configure the **port forwarding (Tunnel)** to access your web server.

Suppose your web server uses port `123` and you want to access it through `http://localhost:456` (or `https` is you configured encrypted communication using OpenSSL) in your local web browser.

1. Check to see which ports are being used by other users and system by executing the command below:
    ```bash
    nmap -sT localhost
    ```
2. Enable port forwarding when login to the server:
    * [Login with command line](#21-login-with-command-line)
        ```bash
        $ ssh -L 123:localhost:456 -p port -i ~/.ssh/id_rsa $USERNAME@server_IP
        ```
    * [Login from ssh config file](#22-login-from-ssh-config-file)
        ```vim
        Host host-name  # specify a host name by yourself
            HostName server_IP  # IP address
            User $USERNAME
            Port port
            ForwardAgent yes
            IdentityFile ~/.ssh/id_rsa  # the path to your private key
            LocalForward 123 localhost:456
        ```
    * [Login from MobaXterm](#23-login-from-mobaxterm-windows-only)
        1. Create a SSH tunnel by following the instructions below:
        ![Click Tunnneling](https://raw.githubusercontent.com/SJTU-VLG/server_utilities/master/imgs/mobaxterm_tunnel_1.jpg)
        ![Create a new SSH tunnel](https://raw.githubusercontent.com/SJTU-VLG/server_utilities/master/imgs/mobaxterm_tunnel_2.jpg)
        ![Configure port forwarding](https://raw.githubusercontent.com/SJTU-VLG/server_utilities/master/imgs/mobaxterm_tunnel_3.jpg)
        ![Start port forwarding](https://raw.githubusercontent.com/SJTU-VLG/server_utilities/master/imgs/mobaxterm_tunnel_4.jpg)
        2. Open web browser to access `http://localhost:456`

### 2.5 X11 Forwarding
X11 forwarding is used to run graphical applications remotely (e.g., display images or play videos on the server, launch applications with GUI remotely).<!-- However, enabling **X11 forwarding** (and **agent forwarding**) increase the risk of an attack spreading from a compromised server to a user's desktop, so  -->
**It is recommended not to enable X11 forwarding if unnecessary**. If you need to view images (especially videos) from the server, you can first download these media files to your local device then open them locally, or by [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/latest/public_server.html).  **Please do not open them directly in your terminal through X11 forwarding.**

Enable X11 forwarding when login to the server:
* [Login with command line](#21-login-with-command-line)
    ```bash
    ssh -X -p port $USERNAME@server_IP
    ```
    It is recommended to replace `-X` with `-Y4C` to speed up SSH connections:
    ```bash
    ssh -Y4C -p port $USERNAME@server_IP
    ```
* [Login from ssh config file](#22-login-from-ssh-config-file)
    ```vim
    Host host-name  # specify a host name by yourself
        HostName server_IP  # IP address
        User $USERNAME
        Port port
        IdentityFile ~/.ssh/id_rsa  # the path to your private key
        X11Forwarding yes
    ```
* [Login from MobaXterm](#23-login-from-mobaxterm-windows-only)
Edit your session settings:
![Enable X11 forwarding](https://raw.githubusercontent.com/SJTU-VLG/server_utilities/master/imgs/mobaxterm_x11.jpg)


## 3. Softwares
If you find that there is some software or package you need to use which is not installed in the server yet, please contact the administrator.
### 3.1 Tools
* tmux
`tmux` is a terminal multiplexer. It lets you switch easily between several programs in one terminal, detach them (they keep running in the background) and reattach them to a different terminal. And do a lot more. See the [tmux manual page](http://man.openbsd.org/OpenBSD-current/man1/tmux.1) and [the README](https://raw.githubusercontent.com/tmux/tmux/master/README).

* Aria2
`Aria2` is a lightweight, multi-connection download utility. 
E.g., download a file from `http://foo.org/bar.zip` into `~/downloads/myfile.zip` using 2 connections.
    ```bash
    $ aria2c -x 2 -d ~/downloads -o myfile.zip http://foo.org/bar.zip
    ```

    You can get more information about [aria2c options](https://aria2.github.io/manual/en/html/aria2c.html#options)

* feh
`feh` is an image viewer for console users ([X11 forwarding](#25-x11-forwarding) required). You can view an image in the terminal by entering the command below:
    ```bash
    $ feh /path_to_image/image.jpg
    ```

* htop
You can dynamically monitor the status of CPU and Memory using `htop` or `top`. **When you are running your program and you have no idea how much resource it occupies, please run `htop` first.** This is important to avoid a server crash.
You can get more information from the [htop official website](http://hisham.hm/htop/).


### 3.2 Python and Deep Learning packages
#### 3.2.1 Anaconda
Please select `Anaconda2` or `Anaconda3` as your default python interpreter, in which many basic packages are installed. The configuration is as follows:

* **Anaconda3 (Python 3.6.8)**
    Before you use `Anaconda3`, you need to add the `bin` path into the `$PATH` environment variable by adding the following line into your bash config file `~/.bashrc`:
    ```bash
    export PATH="$PATH:/usr/local/anaconda3/bin"
    ```
    Save and exit `~/.bashrc`, then activate the change by executing the command below:
    ```bash
    $ source ~/.bashrc
    ```

* **Anaconda2 (Python 2.7.15)**
    It is recommended to use Python 3 in the future rather than Python 2 since [Python 2.7 will not be maintained past 2020](https://www.python.org/dev/peps/pep-0373/). You can read officical documents about [Automated Python2 to 3 code translation](https://docs.python.org/2/library/2to3.html) to convert your Python 2 code to valid Python 3.x code.

    By default, `Anaconda2` is installed as an environment of `Anaconda3` located in `/usr/local/anaconda3/envs/py2`. If you have already configured `Anaconda3`, you can easily switch between Python 3 and Python 2:
    1. Check to see if you have already configured `Anaconda3` by entering the command below:
        ```bash
        $ which python
        /usr/local/anaconda3/bin/python
        ```
    2. Switch from `Anaconda3` (Python 3) to `Anaconda2` (Python 2):
        ```bash
        $ source activate py2
        (py2) $ which python
        /usr/local/anaconda3/envs/py2/bin/python
        ```
    3. Switch from `Anaconda2` (Python 2) back to `Anaconda3` (Python 3):
        ```bash
        $ source deactivate
        (py2) $ which python
        /usr/local/anaconda3/bin/python
        ```

    If you want to only use `Anaconda2` and don't want to switch from `Anaconda3` to `Anaconda2` every time you login, you can add the `bin` path of `Anaconda2` to the `$PATH` environment variable by adding the following line into your `~/.bashrc`:
    ```bash
    export PATH="$PATH:/usr/local/anaconda3/envs/py2/bin"
    ```

**Please do not install an entire Anaconda package in your own directory,** which occupies much unnecessary space of the server. When you need to import some packages which has not been installed in the system Anaconda yet (normally you will get `ModuleNotFoundError`), you can choose one of the following solutions:
   1. Contact the administrator, tell the administrator what packages you need, and the administrator will install these packages into the system Anaconda directory.
   2. Install packages in your directory by entering the following commands:
      * Install by [`pip install`](https://pip.pypa.io/en/stable/reference/pip_install/#options) with `--user` option
      ```bash
      $ pip install package_name --user
      ```
      * Install by [`conda install`](https://conda.io/docs/commands/conda-install.html) with `-p` option
      ```bash
      $ conda install package_name -p /path/to/your/directory
      ```
For creating an isolate Python environment for one of your projects when necessary, see ["Create an environment with conda"](https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands) for more information.

#### 3.2.2 CUDA 9.0
CUDA 9.0 is installed in `/usr/local/cuda-9.0` with **cuDNN 7.4.2** which is in support of [TensorFlow](#324-tensorflow-v112) (so far). Before importing these deep learning libraries to run your program, you need to configure the environment by adding the following lines into your `~/.bashrc`:
```bash
export PATH="$PATH:/usr/local/cuda-9.0/bin"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda-9.0/lib64"
```

#### 3.2.3 PyTorch
* version: v1.0.1

PyTorch is installed by `conda` with CUDA support by `cudatoolkit-10.0.130`. As for now, CUDA-10.0 has not been installed in the system so **you don't need to configure the `$PATH` for CUDA**. All you need to do is to make sure you have configured the correct [CONDA_PATH](#321-anaconda).

Read [official documents](https://pytorch.org/docs/stable/index.html) for the usage of PyTorch.

##### 3.2.3.1 torchvision
* version: v0.2.2

`torchvision` is installed by `conda`. Read [official documents](https://pytorch.org/docs/stable/torchvision/index.html) for the usage of torchvision.

##### 3.2.3.2 tensorboardX
tensorboardX is a simple interface to log events within PyTorch and then show visualization in Google's tensorflow's tensorboard which is a web server to serve visualizations of the training progress of a neural network.

Here's an example about how to launch tensorboardX to visualize your tensorboard events:
1. Open a terminal (`tmux` or `screen`)
2. Launch tensorboardX with your specified log directory:
    ```bash
    $ tensorboard --logdir /path/to/your/log/directory
    ```
3. Open a web browser and access `http://localhost:123` in your local machine.

By default, tensorboard uses port `123` for the web server, you need to enable [port forwarding](#24-port-forwarding) to access the web page in your local web browser.

See official [github](https://github.com/lanpa/tensorboardX) and [documents](https://tensorboardx.readthedocs.io/en/latest/tensorboard.html) for the usage of tensorboardX.

#### 3.2.4 TensorFlow
* version: v1.12

By default, **your tensorflow program which runs on GPUs takes up all available GPU resources**, which may cause some troubles to other users. It is recommended to add the following codes in the head of your main program to use limited GPU resources (memories):
```python
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # only use GPU-0
import tensorflow as tf
config = tf.ConfigProto()
# Solution-1: Allocate GPU memories exactly according to your program
config.gpu_options.allow_growth = True

# Solution-2: Set the percentage of maximum gpu memories used for running this program
config.gpu_options.per_process_gpu_memory_fraction = 0.5  # e.g., 50% of total gpu memories on this GPU card
sess = tf.Session(config=config)

#### Your Code Below ####
```

See official [github](https://github.com/tensorflow) and [API docs](https://www.tensorflow.org/api_docs/python/tf?hl=zh-cn) for the usage of TensorFlow.

## 4. Datasets
All datasets directories are put in `/data/datasets/`. Please see [DATASETS.md](https://github.com/SJTU-VLG/server_utilities/blob/master/Datasets.md) for more information about each dataset.

If the dataset you need to use has not been downloaded to the server yet, you can first add the download links into [download_datasets.py](https://github.com/SJTU-VLG/server_utilities/blob/master/scripts/download_datasets.py) and relevant information (basic introduction, links) into [DATASETS.md](https://github.com/SJTU-VLG/server_utilities/blob/master/Datasets.md) by creating a [new pull request](https://github.com/SJTU-VLG/server_utilities/pull/new/master), then contact the administrator to help you download the dataset to the server.

Welcome to help us collect more valuable datasets to enrich our research. **Your contribution will be greatly appreciated :)**

---
TBD...