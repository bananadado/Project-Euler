using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Multiples_of_3_or_5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int total = 0;
            for (int i = 0; i < 1000; i++)
            {
                if (i % 3 == 0 || i % 5 == 0)
                {
                    total += i;
                }
            }
            Console.WriteLine(total);
            Console.ReadKey();
        }
    }
}
