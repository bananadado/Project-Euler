using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _012___Highly_divisible_triangular_number
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //triangle numbers = n(n+1)/2
            int current = 0;
            while (true)
            {
                current++;
                int divisors = 0;
                ulong triangle = (ulong)(current * (current + 1)) / 2;

                for (ulong i = 1; i <= Math.Round(Math.Sqrt(triangle), 0); i++)
                {
                    if (triangle % i == 0)
                    {
                        divisors+=2;
                    }
                    if (i == Math.Round(Math.Sqrt(triangle), 0))
                    {
                        divisors--;
                    }
                }
                if (divisors > 500)
                {
                    Console.WriteLine(triangle);
                    break;
                }
            }
            Console.ReadKey();
        }
    }
}
