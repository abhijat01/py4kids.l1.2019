# Objective 
This is the starting module. We will focus on installations, 
creating the environment, writing a hello world program in an editor 
and running it from the editor and from the command prompt. You 
will need an adult to help you with this section. 

# Downloading and installing python 

We will use anaconda, a really fat python distribution that comes with a lot 
of bells and whistles. You can download Anaconda from https://www.anaconda.com/products/individual. Make sure you get the latest version with graphic 
installer. At the time of this writing, latest version is for python 3.7. 

Install anaconda at the file system root on windows. Makes sure there are 
no whitespaces or special characters in the installation path. I have 
not installed Anaconda on Macs but you should have an option to install it 
within your child's home directory. 

The following discussion assumes that you  have installed anaconda at 
``c:/Anaconda3``. 

## First time configuration
Start command prompt, change directory to ``c:/Anaconda3/Scripts`` and 
run the command 

    conda 

If you are running this command for the first time, you will see a few 
instructions. Follow the instructions to add conda options to your path. 
Since I do not have a new computer to try this on, I cannot at this time 
provide exact instructions. 

## Create an insolated environment 
Kids will mess up their environment. Even adults do this hence the need for 
virtual environments. It will also help me manage dependencies to make sure 
we have a consistent python environment for all kids. Assuming that you configured  ``conda`` correctly in the previous step,  execute the following 
command in a windows command prompt (or mac/linux terminal). 

    
    conda create -n py4kids.l1  python=3.8.2 

If this goes well, last few lines of the output should look something like 

        #
        # To activate this environment, use
        #
        #     $ conda activate py4kids.l1
        #
        # To deactivate an active environment, use
        #
        #     $ conda deactivate

To check this environment, activate  and then type ``python`` on the command prompt. 

    conda activate py4kids.l1 


Your output should look like  

    C:\Users\vatsyaya>conda activate py4kids.l1

    (py4kids.l1) C:\Users\vatsyaya>python
    Python 3.8.2 (default, May  6 2020, 09:02:42) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

In the future, make sure you  are in the py4kids.l1 environment before you 
run steps for installing any of the packages. 

# Installling pycharm 

Pycharm has a free community version that you can download from https://www.jetbrains.com/pycharm/download/ . Download and install the editor. We will configure it to use the conda virtual environment interperter a little later. 

# Installing github 

You will find it useful to download programs and homework assignments using 
git instead of relying on  email or google drive.  Kids do not need to commit code, they just need to download the latest version using git clone. 
Pycharm also comes with a built in git client bnt  will post instructions for the 
command line git. Download and install the "windows setup" and not the "portable" distribution. from https://git-scm.com/download/win . 