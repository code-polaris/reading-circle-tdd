using System;

namespace TDD
{
    public sealed class Dollar : Money, IEquatable<Money>
    {
        public Dollar(int amount)
        {
            Amonut = amount;
        }

        public Dollar Times(int multiplier)
        {
            return new Dollar (Amonut * multiplier);
        }

        #region Equality members

        /// <inheritdoc />
        public bool Equals(Money other)
        {
            return Amonut == other!.Amonut;
        }

        #endregion
    }
}
