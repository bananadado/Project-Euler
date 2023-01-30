using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _017___Number_letter_counts
{
    internal class Program
    {
        static string singleDigit(int num)
        {
            switch (num)
            {
                case 1:
                    return "one";
                case 2:
                    return "two";
                case 3:
                    return "three";
                case 4:
                    return "four";
                case 5:
                    return "five";
                case 6:
                    return "six";
                case 7:
                    return "seven";
                case 8:
                    return "eight";
                case 9:
                    return "nine";
            }
            return "";
        }
        static string doubleDigit(string num)
        {
            switch (num[0])
            {
                case '1':
                    switch (int.Parse(num[1].ToString()))
                    {
                        case 0:
                            return "ten";
                        case 1:
                            return "eleven";
                        case 2:
                            return "twelve";
                        case 3:
                            return "thirteen";
                        case 4:
                            return "fourteen";
                        case 5:
                            return "fifteen";
                        case 6:
                            return "sixteen";
                        case 7:
                            return "seventeen";
                        case 8:
                            return "eighteen";
                        case 9:
                            return "nineteen";
                    }
                    break;
                case '2':
                    return "twenty";
                case '3':
                    return "thirty";
                case '4':
                    return "forty";
                case '5':
                    return "fifty";
                case '6':
                    return "sixty";
                case '7':
                    return "seventy";
                case '8':
                    return "eighty";
                case '9':
                    return "ninety";
            }
            return "";
        }
        static void Main(string[] args)
        {
            //sadness i dont like this problem
            int total = 0;

            for (int i = 1; i <= 1000; i++)
            {
                string num = String.Format("{0:0000}",i);
                string word = "";

                if (num[0] != '0')
                {
                    word += singleDigit(int.Parse(num[0].ToString())) + "thousand";
                }
                if (num[1] != '0')
                {
                    word += singleDigit(int.Parse(num[1].ToString())) + ((num[2] == '0' && num[3] == '0')? "hundred":"hundredand");
                }
                if (num[2] != '0')
                {
                    word += doubleDigit(num.Substring(2));
                }
                if (num[3] != '0' && num[2] != '1')
                {
                    word += singleDigit(int.Parse(num[3].ToString()));
                }
                total += word.Length;
                Console.WriteLine(word);
            }
            Console.WriteLine(total);
            Console.ReadKey();
        }
    }
}
