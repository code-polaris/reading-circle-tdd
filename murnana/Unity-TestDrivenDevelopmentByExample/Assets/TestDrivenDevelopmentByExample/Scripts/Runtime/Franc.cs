namespace TDD
{
    public sealed class Franc : Money
    {
        public Franc(int amount)
        {
            Amonut = amount;
        }

        /// <inheritdoc />
        public override string Currency()
        {
            return "CHF";
        }

        public override Money Times(int multiplier)
        {
            return new Franc (Amonut * multiplier);
        }
    }
}