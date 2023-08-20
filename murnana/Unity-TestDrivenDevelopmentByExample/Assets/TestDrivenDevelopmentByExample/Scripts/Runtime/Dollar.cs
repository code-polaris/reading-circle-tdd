namespace TDD
{
    public sealed class Dollar : Money
    {
        public Dollar(int amount, string currency)
        {
            Amonut     = amount;
            m_Currency = currency;
        }

        public override Money Times(int multiplier)
        {
            return Money.Dollar (Amonut * multiplier);
        }
    }
}