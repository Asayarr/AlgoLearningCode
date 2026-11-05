using System;

class Program
{
    static void Main()
    {
        string[] input = Console.ReadLine().Split();
        long a = long.Parse(input[0]);
        long b = long.Parse(input[1]);
        long m = long.Parse(input[2]);

        long result = 1;
        a = a % m;

        while (b > 0)
        {
            if (b % 2 == 1)              // 二进制最低位是 1
                result = (result * a) % m;

            a = (a * a) % m;             // a 平方
            b /= 2;                      // b 右移
        }

        Console.WriteLine(result);
    }
}