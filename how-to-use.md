# Getting Started 

---

## Prerequisites
- Linux 18.04 or above
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) installed on system

## Installation
1. Navigate to a directory of your choice and download 'environment.yml' and 'script.sh'. enter following commands in terminal:
    > wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/environment.yml

    > wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/script.sh
2. Run the following commands in order. They create a new conda environment, download the necessary dependencies and the source files in new folder 'nst'.<br> 
**Say yes to any installation asked**. the commands might take a while to complete.

    create environment : 
    >conda env create -f environment.yml

    activate environment : 
    >conda activate nst
    
    change script permission :
    >chmod +x script.sh

    run script :
    >source script.sh

3. You're all set! <br> To perform Neural Style Transfer on your own images **you can put the content and style image in the nst folder** and run the following command
    > python3 main.py

    it'll ask you to specify the name of content and style images (**including extensions** like .png, .jpg, etc) and then run the style transfer.
    The **results will be saved in 'res' directory**.
    
    if you run into any error regarding some **DNN library or shared library not found**, run the following command before running main.py
    > export LD\_LIBRARY_PATH=LD_LIBRARY_PATH:$CONDA_PREFIX/lib/


---


As a bonus point you can also **run Style Transfer with hyperparameters of your choice**.

To do that run :

    python3 main.py -h
![](https://i.imgur.com/KUGRB1S.png)

    
for example :
- choose number of iterations : 
    > python3 main.py -n 2000            
    
    runs style style transfer for 2000 iterations.
    default no. of iterations = 5000.

-  choose alpha : 
    > python3 main.py --alpha 1e5

    runs style transfer with alpha = 1e5.
    default alpha = 1e4.
- choose beta value : 
    > python3 main.py --beta 1e-1           

    runs style transfer with beta = 1e-1.
    default beta = 1.

- choose learning rate :     
    > python3 main.py -l 20         
      
    runs style transfer with learning rate = 20.
    default learning rate = 5.
    

