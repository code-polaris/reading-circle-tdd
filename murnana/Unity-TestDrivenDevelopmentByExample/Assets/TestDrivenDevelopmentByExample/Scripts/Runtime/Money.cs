using System;

namespace TDD
{
    public class Money : IEquatable<Money>
    {
        protected int Amonut = 10;

        #region Equality members

        /// <inheritdoc />
        public bool Equals(Money other)
        {
            return Amonut == other!.Amonut;
        }

        #endregion
    }
}