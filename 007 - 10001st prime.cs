using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _10001prime
{
    internal class Program
    {
        static bool isPrime(int num)
        {
            for (int i = 2; i < (int)Math.Sqrt(num)+1; i++)
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
            int primes = 0;
            int current = 1;
            while (primes < 10001)
            {
                current++;
                if (isPrime(current))
                {
                    primes++;
                }
            }
            Console.WriteLine(current);
            Console.ReadKey();
        }
    }
}
