/*
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
*/

public class Kata
{
  public static string AbbrevName(string name)
  {
    char first =  name[0];
    char second = name[name.IndexOf(" ")+1];
    return $"{first}.{second}".ToUpper();
  }
}
