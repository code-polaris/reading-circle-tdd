using System;

namespace TDD
{
    public class Money : IEquatable<Money>
    {
        protected readonly int m_Amount;
        protected readonly string m_Currency;


        public static Money Dollar(int amount)
        {
            return new Dollar (amount: amount, currency: "USD");
        }

        public static Money Franc(int amount)
        {
            return new Franc (amount, "CHF");
        }


        public Money(int amount, string currency)
        {
            m_Amount   = amount;
            m_Currency = currency;
        }


        public virtual Money Times(int multiplier)
        {
            return null;
        }

        public string Currency()
        {
            return m_Currency;
        }

        #region Equality members

        /// <inheritdoc />
        public bool Equals(Money other)
        {
            if (GetType() != other!.GetType())
            {
                return false;
            }

            return m_Amount == other!.m_Amount;
        }

        #endregion

        #region Overrides of Object

        /// <inheritdoc />
        public override string ToString()
        {
            return $"{m_Amount} {m_Currency}";
        }

        #endregion
    }
}
