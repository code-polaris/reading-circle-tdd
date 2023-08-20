namespace TDD
{
    public sealed class Dollar : Money
    {
        public Dollar(int amount)
        {
            Amonut = amount;
        }

        /// <inheritdoc />
        public override string Currency()
        {
            return "USD";
        }

        public override Money Times(int multiplier)
        {
            return new Dollar (Amonut * multiplier);
        }
    }
}