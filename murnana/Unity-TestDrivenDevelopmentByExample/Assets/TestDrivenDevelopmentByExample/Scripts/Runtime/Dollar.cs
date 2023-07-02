namespace TDD
{
    public sealed class Dollar
    {
        public int Amonut = 10;

        public Dollar(int amount)
        {
            Amonut = amount;
        }

        public void Times(int multiplier)
        {
            Amonut *= multiplier;
        }
    }
}
