import numpy as np;
import matplotlib.pyplot as plt;

def two_ord_function(a,b,c):
    def _inner(x):
        y=a*x**2+b*x+c;
        return y;
    return _inner;



if __name__=="__main__":
    x=np.random.randint(-10,10,size=(3,1));
    f=two_ord_function(2,1,3);
    y=f(x);
    X=np.r_["1",x**2,x,np.ones_like(x)];
    w=np.linalg.inv(X)@y;
    print(w);

    fig=plt.figure();
    ax=fig.add_subplot(111);
    ax.scatter(x,y,c="red");
    t=np.linspace(-10,10,1000);
    y_true=f(t);
    ax.plot(t,y_true,c="black");
    dir="/home/jovyan/work/";
    fig.savefig(dir+"test2-1.png",dpi=300);