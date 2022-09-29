from style_transfer import *


for f in os.listdir('res'):
    if not f.endswith(".png"):
        continue
    os.remove(os.path.join('res', f))

#src
content_path = 'content.png'
style_path = 'style.jpg'

#hyperparams
num_iterations=5000
alpha=1e4 
beta=1
learning_rate = 5
epsilon = 1e-1

argList = sys.argv[1:]
options = "n:a:b:l:h"
long_options = ["numiter","alpha","beta","lr","help"]

try :
    args,vals = getopt.getopt(argList,options,long_options)

    for arg,val in args :
        if arg in ("-n","--numiter") :
            num_iterations = int(val)
        elif arg in ("-a","--alpha") :
            alpha = float(val)
        elif arg in ("-b","--beta") :
            beta = float(val)
        elif arg in ("-l","--lr") :
            learning_rate = float(val)
        elif arg in ("-h","--help") :
            print('''
                     -n <number> OR --numiter <number>  --> to choose number of iterations\n
                     -a <number> OR --alpha <number>    --> to choose alpha value\n
                     -b <number> OR --beta <number>     --> to choose beta value\n   
                     -l <number> OR --lr <number>       --> to chose learning rate\n
                     -h OR --help                       --> for help''')
            exit()

except getopt.error as err :
    print(err)

print("-"*10+"HYPERPARAMETERS"+"-"*10)

print(f"Number of iterations :{num_iterations:>5}")
print(f"Alpha :{alpha:>23}")
print(f"Beta :{beta:>18}")
print(f"Learning Rate : {learning_rate:>8}")
print(f"Epsilon : {epsilon:>16}")
print("\n(images are saved in res folder)")

#src
content_path = input("Enter Content Path : ")
style_path = input("Enter Style Path : ")

print("\n\n"+"*"*20+"RUNNING NEURAL STYLE TRANSFER"+"*"*20+"\n\n")


best_img = neural_style_transfer(content_path, 
                          style_path,
                          num_iterations=num_iterations,
                          alpha=alpha,
                          beta=beta,
                          learning_rate=learning_rate,
                          epsilon=epsilon)


im = Image.fromarray(best_img)
im.save(f'res/BEST.png')
