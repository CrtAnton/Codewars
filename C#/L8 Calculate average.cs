/*Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.*/

class AverageSolution
{
  public static double FindAverage(double[] array)
  {
    if (array.Length == 0){
      return 0;
    }
    else{
      double sum = 0;
      for (int i=0; i<=array.Length-1; i++){
        sum += array[i];
      }
      return sum/array.Length;
    }
    
  }
} 
