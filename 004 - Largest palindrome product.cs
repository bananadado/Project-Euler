using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Largest_palindrome_product
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int highest = 0;
            for (int i = 100; i < 1000; i++)
            {
                for (int j = 100; j < 1000; j++)
                {
                    List<char> reverse = (i*j).ToString().ToCharArray().ToList();
                    reverse.Reverse();
                    if (int.Parse(String.Join("", reverse)) == i*j && i*j > highest)
                    {
                        highest = i*j;
                    }
                }
            }
            Console.WriteLine(highest);
            Console.ReadKey();
        }
    }
}
