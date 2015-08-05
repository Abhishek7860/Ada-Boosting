"""
Implementation of Ada Boosting algorithm and Real AdaBoosting algorithm

Input:
**************************
T (an integer number).
n (an integer number).
epsilon (a small real number)
x (a list of n real numbers. These are assumed to be in increasing order).
y (a list of n numbers, each one is either 1 or -1).
p (a list of n nonnegative numbers that sum up to 1).

Output AdaBoosting :
1. The selected weak classifier: ht.
2. The error of ht: et.
3. The weight of ht: alphat.
4. The probabilities normalization factor: Zt.
5. The probabilities after normalization: pi.
6. The boosted classifier: ft.
7. The error of the boosted classifier: Et.
8. The bound on Et.

Output: Real AdaBoosting
*****************************
1. The selected weak classifier: ht.
2. The G error value of ht : Gerror.
3. The weights ct+, ct-.
4. The probabilities normalization factor: Zt.
5. The probabilities after normalization: pi.
6. The values ft(xi) for each one of the examples.
7. The error of the boosted classifier: Et.
8. The bound on Et.
"""
import math
from test.support import temp_cwd

class adaboosting:
    ffun = []
    rfinal = []    
    bound = 1
    bbound =1
    """Initiation of class variables"""
    def __init__(self,x,y,prob,t,eps,n):
        self.x=x
        self.y=y
        self.prob=prob
        self.t=t
        self.eps = float(eps)
        self.n = int(n)
        for i in range(0,int(n)):
            adaboosting.ffun.append(0)# contains Ft value for AdaBoosting
            #adaboosting.rfinal.append(0)# Contains ft value for Ral AdaBoosting
    """This function calculates the threshold array"""  
    def temp(self,temp):
        avg=(0+self.x[0])/2
        temp.append(avg)
        for i in range(0,len(self.x)-1):
            avg= (self.x[i]+self.x[i+1])/2
            temp.append(avg)
        #print(self.x[i+1])
        avg= self.x[i+1]+ 0.1
        temp.append(avg)        
        return temp
    
    """This function calculates the hypothesis array for threshold less than value"""
    def lesshypo(self,temp_error,value):
        for i,sign in enumerate(self.y):
            if(value > self.x[i]):
                temp_error.append(1)
            else:
                temp_error.append(-1)
        return temp_error
    """This function calculates the hypothesis array for threshold greater than value"""
    def greahypo(self,temp_error,value):
        for i,sign in enumerate(self.y):
            if(value < x[i]):
                temp_error.append(1)
            else:
                temp_error.append(-1)
        return temp_error
    """This function calculates the error in hypothesis"""
    def errorcalc(self):
        error =0
        for i,va in enumerate(self.temp_error):
            if (va != y[i]):
                    #print(va, y[i])
                error=error+prob[i]
        return error
    
    """This function implements F (f(x))function of AdaBoosting algorithms
    Returns the error calculated as per f function
    """
    def finallistcalc(self):
        te = []
        for i,valu in  enumerate(adaboosting.ffun):
            if(valu>0):
                te.append(1)
            else:
                te.append(-1)
        count_f=0
        for i,va in enumerate(te):
            if(va != y[i]):
                count_f =count_f+1
        return count_f
    
    """This function implements F (f(x))function of real AdaBoosting algorithms
    Returns the error calculated as per f function
    """
    def realfinallistcalc(self):
        te = []
        for i,valu in  enumerate(adaboosting.rfinal):
            if(valu>0):
                te.append(1)
            else:
                te.append(-1)
        count_f=0
        for i,va in enumerate(te):
            if(va != y[i]):
                count_f =count_f+1
        return count_f
    """
    This Function calculate the output for AdaBoosting foe weak classifiers
    """      
    def minierror(self):
        temp = []
        error_list = []
        list_error = []
        mark = []
        temp = self.temp(temp)
        for value in temp:
            temp_error=[]
            index ='Less than '+str(value)
            self.temp_error = self.lesshypo(temp_error,value)
            list_error.append(self.temp_error)
            mark.append(index)
            error = self.errorcalc()
            error_list.append(error)
            index ='Greater than '+str(value)
            mark.append(index)
            #print(error_list)
            temp_error=[]
            self.temp_error = self.greahypo(temp_error,value)
            list_error.append(self.temp_error)
            error =0
            error = self.errorcalc()
            error_list.append(error)
        
        print("   ")
        #print("Binary Classification")
        epsilon = min(error_list)
        print("Weak Classifier: " + mark[error_list.index(epsilon)])
        print("Error"+ str(epsilon))        
        temp_com = list_error[error_list.index(epsilon)]
        alpha = 0.5*math.log((1-epsilon)/epsilon)
        print("Weight "+str(alpha))
        totalsum = sum(self.prob)       
        qwrong = math.sqrt(epsilon/(1-epsilon))
        qcorrect = math.sqrt((1-epsilon)/epsilon)
        zvalue = 2* math.sqrt((1-epsilon)*epsilon)
        print("Z Value: "+str(zvalue))
        for i,wt in enumerate(self.prob):
            if(temp_com[i]==y[i]):
                inival = prob[i]
                prob[i]=qwrong*inival/zvalue
            else:
                inival = prob[i]
                prob[i]=qcorrect*inival/zvalue        
        print("Probablity after Normalization "+str(prob))
        adaboosting.rfinal.append(mark[error_list.index(epsilon)])
        for i,val in enumerate(temp_com):
            adaboosting.ffun[i]= alpha*val+adaboosting.ffun[i]     
        print("Boosted Clasifier: "+str(adaboosting.ffun)+str(adaboosting.rfinal))
         
        #print (adaboosting.rfinal)      
        count_f = self.finallistcalc()      
        adaboosting.bbound = adaboosting.bbound*zvalue
        print("Error of Boosted Classifier "+str(count_f/int(self.n)))
        print("Bound Error"+str(adaboosting.bbound) )
        #print("------------------------------------------------------------------------------------------")   
   

file_name = input("Enter the file name : ")
x = []
y = []
prob = []
with open(file_name) as f:
    for i, l in enumerate(f):
        if (i==0):
            (t,n,eps) = l.rstrip('\n').split(' ')
        if (i==1):
            l=l.split()
            if l:
                for j in l:
                    x.append(float(j))
        if (i==2):
            l=l.split()
            if l:
                for j in l:
                    y.append(int(j))
        if (i==3):
            l=l.split()
            if l:
                for j in l:
                    prob.append(float(j))

ada = adaboosting(x,y,prob,t,eps,n)
for i in range(0,int(t)):
    print(" ")
    print ("Iteration  "+ str(i))
    ada.minierror()


                    