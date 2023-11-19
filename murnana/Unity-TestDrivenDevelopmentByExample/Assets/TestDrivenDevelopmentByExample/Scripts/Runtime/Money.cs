using System;

namespace TDD
{
    public class Money : IEquatable<Money>,
                         IExpression
    {
        /// <summary>
        /// 通貨
        /// </summary>
        private readonly string m_Currency;

        /// <summary>
        /// 通貨の数
        /// </summary>
        public int Amount { get; }

        public Money(int amount, string currency)
        {
            Amount     = amount;
            m_Currency = currency;
        }

        public static Money Dollar(int amount)
        {
            return new Money (amount: amount, currency: "USD");
        }

        public static Money Franc(int amount)
        {
            return new Money (amount, "CHF");
        }

        public Money Times(int multiplier)
        {
            return new Money (amount: Amount * multiplier, currency: m_Currency);
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
        public IExpression Plus(Money added)
        {
            return new Sum(augend: this, addend: added);
        }

        #region Implementation of IExpression

        /// <inheritdoc />
        public Money Reduced(string to)
        {
            return this;
        }

        #endregion

        #region Equality members

        /// <inheritdoc />
        public bool Equals(Money other)
        {
            if (other == null)
            {
                return false;
            }

            return (Currency() == other.Currency())
                && (Amount == other.Amount);
        }

        #endregion

        #region Overrides of Object

        /// <inheritdoc />
        public override string ToString()
        {
            return $"{Amount} {m_Currency}";
        }

        #endregion
    }
}
