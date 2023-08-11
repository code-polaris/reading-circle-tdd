using System;

namespace TDD
{
    public sealed class Dollar : Money, IEquatable<Dollar>
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
        public bool Equals(Dollar other)
        {
            return Amonut == other!.Amonut;
        }

        #endregion
    }
}
