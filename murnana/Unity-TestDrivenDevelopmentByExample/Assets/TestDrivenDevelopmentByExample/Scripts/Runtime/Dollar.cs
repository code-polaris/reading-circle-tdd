namespace TDD
{
    public sealed class Dollar
    {
        public int Amonut = 10;

        public Dollar(int amount)
        {
            Amonut = amount;
        }

        public Dollar Times(int multiplier)
        {
            return new Dollar (Amonut * multiplier);
        }
    }
}
