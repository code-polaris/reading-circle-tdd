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

        public IExpression Times(int multiplier)
        {
            return new Money (amount: Amount * multiplier, currency: m_Currency);
        }

        public string Currency()
        {
            return m_Currency;
        }

        #region Implementation of IExpression

        /// <inheritdoc />
        public Money Reduced(Bank bank, string to)
        {
            var rate = bank.GetRate(from: m_Currency, to: to);
            return new Money(amount: Amount / rate, currency: to);
        }

        /// <inheritdoc />
        public IExpression Plus(IExpression added)
        {
            return new Sum(augend: this, addend: added);
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
