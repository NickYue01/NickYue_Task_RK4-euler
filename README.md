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

###Problems Meet
In the file test_odesolve.py, in the function 'test_solveto', some piece of code looks odd. The code can pass the questions in 'test_solveto', except the last question, 'assert abs(xguess - xtrue) < 1e-10 / h**0.5'. 
The answer will be more accurate as h becomes smaller, but on the right-hand side, 1e-10 / h**0.5 will become bigger when h decreases. The left-hand side formula and right-hand side formula change in the opposite tendency. From my program, it only outputs True when h =  1e-5. I have also tried to solve the inaccuracy caused by the binary storage, as the computer can't store accurate decimal numbers, like 0.1. The accuracy increases slightly but is still far from the aimed value on the right-hand side. 
Problem found and updated in 20220722
