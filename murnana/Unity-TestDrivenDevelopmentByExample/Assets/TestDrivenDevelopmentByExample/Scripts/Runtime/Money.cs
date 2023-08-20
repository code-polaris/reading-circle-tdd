using System;

namespace TDD
{
    public abstract class Money : IEquatable<Money>
    {
        protected int Amonut = 10;

        public static Money Dollar(int amount)
        {
            return new Dollar (amount);
        }

        public static Money Franc(int amount)
        {
            return new Franc (amount);
        }

        public abstract Money Times(int multiplier);

        #region Equality members

        /// <inheritdoc />
        public bool Equals(Money other)
        {
            if (GetType() != other!.GetType())
            {
                return false;
            }

            return Amonut == other!.Amonut;
        }

        #endregion
    }
}