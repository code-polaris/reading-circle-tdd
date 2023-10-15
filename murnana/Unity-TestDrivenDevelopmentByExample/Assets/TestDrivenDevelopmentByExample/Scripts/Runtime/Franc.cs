namespace TDD
{
    public sealed class Franc : Money
    {
        public Franc(int amount, string currency)
            : base (amount: amount, currency: currency)
        {
        }

        public override Money Times(int multiplier)
        {
            return new Money (amount: m_Amount * multiplier, currency: m_Currency);
        }
    }
}
