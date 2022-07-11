/*
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
*/

  using System;
  public static class Clock
  {
    public static int Past(int h, int m, int s)
    {
      int time = 0;
      return time += s*1000 + m*60000 + h*3600000;
    }
  }
