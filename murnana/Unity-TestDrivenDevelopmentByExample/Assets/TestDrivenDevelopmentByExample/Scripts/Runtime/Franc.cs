namespace TDD
{
    public sealed class Franc : Money
    {
        public Franc(int amount)
        {
            Amonut = amount;
        }

        public Money Times(int multiplier)
        {
            return new Franc (Amonut * multiplier);
        }
    }
}