using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sum_square_difference
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int sum = 0;
            int sumsquare = 0;
            for (int i = 0; i <= 100; i++)
            {
                sum += i;
                sumsquare += i * i;
            }
            Console.WriteLine(sum*sum-sumsquare);
            Console.ReadKey();
        }
    }
}
