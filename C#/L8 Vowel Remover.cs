/*
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"
*/

public class Kata
{
  public static string Shortcut(string input)
  {
    string vowels = "aeiou";
    string result = "";
    foreach (char letter in input){
      if(!(vowels.Contains(letter))){
        result += letter;
      }
    }
    return result;
  }
}
