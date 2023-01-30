using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Largest_prime_factor
{
    internal class Program
    {
        static void Main(string[] args)
        {
            long num = 600851475143;
            int current = 2;
            while (num > 1)
            {
                current = 2;
                while (num % current != 0)
                {
                    current++;
                }
                num = num / current;               
            }
            Console.WriteLine(current);
            Console.ReadKey();
        }
    }
}
