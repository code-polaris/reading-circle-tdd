using System;

namespace TDD
{
    public class Money : IEquatable<Money>
    {
        protected readonly int m_Amount;
        protected readonly string m_Currency;


        public static Money Dollar(int amount)
        {
            return new Money (amount: amount, currency: "USD");
        }

        public static Money Franc(int amount)
        {
            return new Money (amount, "CHF");
        }


        public Money(int amount, string currency)
        {
            m_Amount   = amount;
            m_Currency = currency;
        }


        public Money Times(int multiplier)
        {
            return new Money (amount: m_Amount * multiplier, currency: m_Currency);
        }

        public string Currency()
        {
            return m_Currency;
        }

        /// <summary>
        /// 通貨を加算します
        /// </summary>
        /// <param name="added">加算する通貨</param>
        /// <returns>加算結果(新規インスタンス)</returns>
        /// <remarks>
        /// <para>インスタンス自身には何も影響を与えません</para>
        /// </remarks>
        public Money Plus(Money added)
        {
            return new Money(amount: m_Amount + added.m_Amount, currency: m_Currency);
        }

        #region Equality members

        /// <inheritdoc />
        public bool Equals(Money other)
        {
            if (other == null)
            {
                return false;
            }

            return (Currency() == other.Currency())
                && (m_Amount == other.m_Amount);
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
