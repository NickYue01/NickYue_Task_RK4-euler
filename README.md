# Ziqi_Yue_Reassessment
### Environment
these programs are running on Spyder (python 3.8)  
System: Windows 10
CPU: AMD
System chosen: China, using beta unicode UTF-8

### Information of the Files
-file odesolve.py stores the functions of arithmetics, like euler, rk4, solveto_ ......   
-file test_odesolve.py contains all the test data can will call the functions in the file odesolve.py. This file also shows how many function passed (how the program is finished).   
-file eulercheck.py contains the euler methode. It is a place for try if teh code for euler methode works.  
-file RK4check.py contains the euler methode. It is a place for try if teh code for Rk4 methode works.  
-file Pass parameters.py is used to try for the situation in solveto function. To find out how the default parameter works.    
-file array_test.py extract the array part from test_odesolve.py for testing one by one when the output is wrong. Used for debuging and solving problem.  
-file error_plt.py caculated the diffrernce of estimated value by euler and rk4 method with the real value under different h. Ploting a diagram to show the result.  
-file odesolve backup.py is used for backup for the odesolve.py. Also used for debuging as all the functions are contained in this file.   
-file solveto_debuging.py extract the solveto part from test_odesolve.py for testing one by one when the output is wrong. Used for debuging and solving problem.  
-file test_odesolve.py use the code provided inthe PDF to test the solveto function and plot a diagram.   
-file temp_test_file.py is used to test the code which are not sure how to use and what it used for.  
-file test_arrays.py is the code provided from the PDF to test is array functions normal.   
-file solveto_check.py contains multiple sets of data from test_solveto function from test_odesolve.py. This program is used when the first problem list in the 'Problem Meet' is met. 

###Problems Meet
In the file test_odesolve.py, in the function 'test_solveto', some piece of code looks odd. The code can pass the questions in 'test_solveto', except the last question, 'assert abs(xguess - xtrue) < 1e-10 / h**0.5'. 
The answer will be more accurate as h becomes smaller, but on the right-hand side, 1e-10 / h**0.5 will become bigger when h decreases. The left-hand side formula and right-hand side formula change in the opposite tendency. From my program, it only outputs True when h =  1e-5. I have also tried to solve the inaccuracy caused by the binary storage, as the computer can't store accurate decimal numbers, like 0.1. The accuracy increases slightly but is still far from the aimed value on the right-hand side. 
Problem found and updated in 20220722
problem solved by replace '//' with '/'. 20220726

Using the odesolve_test code provided from the PDF,the ploting can't work.   
The code plt.plot(t,Xt.T) can't output a diagram as the array is not specified.  
Using the code below instead can output a right diagram.  
plt.plot( t,Xt.T[0])  
plt.plot(t,Xt.T[1])  
problem found and updateed in 20220724  
