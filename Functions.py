import numpy as np 
import matplotlib.pyplot as plt

#### Equação de uma reta simple
def reta(a0,a1,x):
    y= a0*x+a1
    return y

def plot(x,y):
   
    fig,ax=plt.subplots(figsize=(10,5),clear =True)
    
    ax.plot(x,y)
    ax.set_title('Equação da reta', fontsize=18)
    ax.set_xlabel(['X'], fontsize=15)
    ax.set_ylabel(['Y'])
    fig.tight_layout() 
    plt.show()

x=np.linspace(0,15,50, endpoint=True)
a0=-0.8
a1=2
y= reta(a0,a1,x)
plot(x,y) 

#### equação de uma parabola


def parabola(a,b,c,x):
    y=a*x**2+b*x+c
    return y

def plot(x,y):
   
    fig,ax=plt.subplots(figsize=(10,5),clear =True)
    
    ax.plot(x,y)
    ax.set_title('Equação da parabola', fontsize=18)
    ax.set_xlabel(['X'], fontsize=15)
    ax.set_ylabel(['Y'])
    fig.tight_layout() 
    plt.show()

x=np.linspace(0,15,50, endpoint=True)
a=2
b=4
c=-6
y= parabola(a,b,c,x)
plot(x,y) 
