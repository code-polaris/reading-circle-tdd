namespace TDD
{
    public sealed class Franc : Money
    {
        public Franc(int amount)
        {
            Amonut = amount;
        }

        public Franc Times(int multiplier)
        {
            return new Franc (Amonut * multiplier);
        }
    }
}