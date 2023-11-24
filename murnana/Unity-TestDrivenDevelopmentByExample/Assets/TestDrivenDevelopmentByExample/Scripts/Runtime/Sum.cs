namespace TDD
{
    /// <summary>
    /// 合計値
    /// </summary>
    public sealed class Sum : IExpression
    {
        /// <summary>
        /// 値を初期化しま
        /// </summary>
        /// <param name="augend">被加算数</param>
        /// <param name="addend">加算数</param>
        public Sum(Money augend, Money addend)
        {
            Augend = augend;
            Addend = addend;
        }

        /// <summary>
        /// 被加算数
        /// </summary>
        public Money Augend { get; }

        /// <summary>
        /// 加算数
        /// </summary>
        public Money Addend { get; }


        #region Implementation of IExpression

        /// <inheritdoc />
        public Money Reduced(Bank bank, string to)
        {
            var amount = Augend.Amount + Addend.Amount;
            return new Money(amount: amount, currency: to);
        }

        #endregion
    }
}
