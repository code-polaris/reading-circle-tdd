// Dollarクラス

namespace Project
{
    public class Dollar
    {
        public int Amount { get; private set; }

        public Dollar(int amount)
        {
            Amount = amount;
        }

        public void Times(int multiplier)
        {
            Amount *= multiplier;
        }
    }
}