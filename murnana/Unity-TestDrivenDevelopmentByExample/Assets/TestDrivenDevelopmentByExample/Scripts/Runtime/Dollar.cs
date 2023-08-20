namespace TDD
{
    public sealed class Dollar : Money
    {
        public Dollar(int amount)
        {
            Amonut = amount;
        }

        public Money Times(int multiplier)
        {
            return new Dollar (Amonut * multiplier);
        }
    }
}