using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Even_Fibonacci_numbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int total = 0;
            int previous = 1;
            int current = 2;
            while (current < 4000000)
            {
                if (current % 2 == 0)
                {
                    total += current;
                }
                current = current + previous;
                previous = current - previous;
            }
            Console.WriteLine(total);
            Console.ReadKey();
        }
    }
}
