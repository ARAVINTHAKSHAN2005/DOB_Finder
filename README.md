# DOB_Finder
#### Has a GUI created using Tkinter, finds the DOB, after following certain steps and entering an input 
### Steps to follow:
 1. Take the number of the month in which you were born (Jan is 1, Feb is 2 and so on...)
 2. Double this number 
 3. Add 5, and then multiply by 5 
 6. Add a zero to the end of teh answer 
 7. Now, add your date of birth 
 8. Input this number int the textbox in the GUI 

### How does it work ?
  * Subtract 250 from the input 
  * The program uses floating point precision to seperate the last two digits from the rest of the new number 
  * The first set of numbers is the corespnding month
  * While the second set is the day on which he/she was born  
Example:
  1071 would become 821, which is the 8th month and 21st say so August 21 would be the DOB
