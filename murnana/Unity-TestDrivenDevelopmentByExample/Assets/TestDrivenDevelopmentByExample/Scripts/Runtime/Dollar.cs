namespace TDD
{
    public sealed class Dollar : Money
    {
        public Dollar(int amount)
        {
            Amonut     = amount;
            m_Currency = "USD";
        }

        public override Money Times(int multiplier)
        {
            return new Dollar (Amonut * multiplier);
        }
    }
}