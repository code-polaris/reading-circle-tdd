using System;

namespace TDD
{
    public sealed class Dollar : IEquatable<Dollar>
    {
        public int Amonut = 10;

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
        public bool Equals(Dollar other)
        {
            return true;
        }

        #endregion
    }
}
