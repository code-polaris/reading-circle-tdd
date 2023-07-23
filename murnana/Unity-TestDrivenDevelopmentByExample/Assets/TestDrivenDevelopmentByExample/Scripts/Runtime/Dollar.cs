using System;

namespace TDD
{
    public sealed class Dollar : IEquatable<Dollar>
    {
        private int Amonut = 10;

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
