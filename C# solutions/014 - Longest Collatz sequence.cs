using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _014___Longest_Collatz_sequence
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int highest = 0;
            int highestChain = 0;
            for (int i = 2; i < 1000000; i++)
            {
                long num = i;
                int chain = 0;
                while (num != 1)
                {
                    if (num % 2 == 0)
                    {
                        num /= 2;
                    }
                    else
                    {
                        num = num * 3 + 1;
                    }
                    chain++;
                }
                if (chain > highestChain)
                {
                    highest = i;
                    highestChain = chain;
                }
            }
            Console.WriteLine(highest);
            Console.ReadKey();
        }
    }
}
