namespace TDD
{
    public sealed class Franc : Money
    {
        public Franc(int amount, string currency)
        {
            Amonut     = amount;
            m_Currency = currency;
        }

        public override Money Times(int multiplier)
        {
            return Money.Franc (Amonut * multiplier);
        }
    }
}