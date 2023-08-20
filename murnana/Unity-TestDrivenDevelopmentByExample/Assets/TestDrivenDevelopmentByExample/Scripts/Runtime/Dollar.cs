namespace TDD
{
    public sealed class Dollar : Money
    {
        public Dollar(int amount, string currency)
            : base (amount: amount, currency: currency)
        {
        }

        public override Money Times(int multiplier)
        {
            return Money.Dollar (m_Amount * multiplier);
        }
    }
}