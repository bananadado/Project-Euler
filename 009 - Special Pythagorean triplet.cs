using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Special_Pythagorean_triplet
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> squares = new List<int>();
            for (int c = 0; c < 1000; c++)
            {
                squares.Add(c*c);
            }
            for (int b = 1; b < 1000; b++)
            {
                for (int a = 1; a < b; a++)
                {
                    if (squares.Contains(a*a + b*b) && a+b+squares.IndexOf(a * a + b * b) == 1000)
                    {
                        Console.WriteLine(a * b * squares.IndexOf(a * a + b * b));
                    }
                }
            }
            Console.ReadKey();
        }
    }
}
