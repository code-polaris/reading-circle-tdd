using System;

namespace TDD
{
    public sealed class Franc : Money, IEquatable<Franc>
    {
        public Franc(int amount)
        {
            Amonut = amount;
        }

        public Franc Times(int multiplier)
        {
            return new Franc (Amonut * multiplier);
        }

        #region Equality members

        /// <inheritdoc />
        public bool Equals(Franc other)
        {
            return Amonut == other!.Amonut;
        }

        #endregion
    }
}
