using System;

namespace MyExtensions
{
    public static class ShadyExtension
    {
        public static int GetDeterministicHashCode(this string str)
        {
            unchecked
            {
                int hash1 = (5381 << 16) + 5381;
                int hash2 = hash1;

                for (int i = 0; i < str.Length; i += 2)
                {
                    hash1 = ((hash1 << 5) + hash1) ^ str[i];
                    if (i == str.Length - 1)
                        break;
                    hash2 = ((hash2 << 5) + hash2) ^ str[i + 1];
                }

                return hash1 + (hash2 * 1566083941);
            }
        }
    }
}

namespace MyApp 
{
    using MyExtensions;
    internal class Program
    {
        static void Main(string[] args)
        {
            var seed = args[0].GetDeterministicHashCode();
            var r = new Random(seed);
            Console.WriteLine(r.NextInt64());
        }
    }
}