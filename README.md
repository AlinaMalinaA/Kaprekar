## How to Start:

Open file main.py as text
Below you see the example of how code inside looks like. You can edit constants N, R and A as you wish.
Constant N is for number of digits in experiment number. If you want search Kaprekar points for numbers 1000 - 9999, then N should be 4 
Constant R is for number of operations (distracts) do, if there is no point. For example, if experimental number gives regular set of numbers, then there will be no point (one number that repeats), so we will have to stop at some time. You will not see the regularity if you stop too early (10 operations for example). The bigger the experimental number, the bigger the R should  be. If N is 4, then R is 10 (that is optimal constants)
Constant A is the number of random experiment numbers. If A=1, then it will be only one number taken for experiments. The more the better, but it will take some time. 

![Image of Code](/Images/How_to_start.PNG)

## What you will get:

See the pictire below
On top part there is Experiment number *number* and it' point or repeated period (if there is one)
On bottom part thereis array of reslts for every experimented number: 0 if no point was found and number which is actually the point. You can see that every resulted number is the same, so it is a real point. 

![Image of Code](/Images/Result.PNG)