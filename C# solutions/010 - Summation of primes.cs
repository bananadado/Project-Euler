using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Summation_of_primes
{
    internal class Program
    {
        static bool isPrime(int num)
        {
            for (int i = 2; i < (int)Math.Sqrt(num) + 1; i++)
            {
                if (num % i == 0)
                {
                    return false;
                }
            }
            return true;
        }
        static void Main(string[] args)
        {
            long total = 0;
            int current = 1;
            while (current < 2000000)
            {
                current++;
                if (isPrime(current))
                {
                    total+=current;
                }
            }
            Console.WriteLine(total);
            Console.ReadKey();
        }
    }
}
