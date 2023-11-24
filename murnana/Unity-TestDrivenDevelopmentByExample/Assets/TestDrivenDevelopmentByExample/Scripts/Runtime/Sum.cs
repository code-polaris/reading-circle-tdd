using System;

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
        public Sum(IExpression augend, IExpression addend)
        {
            Augend = augend;
            Addend = addend;
        }

        /// <summary>
        /// 被加算数
        /// </summary>
        public IExpression Augend { get; }

        /// <summary>
        /// 加算数
        /// </summary>
        public IExpression Addend { get; }


        #region Implementation of IExpression

        /// <inheritdoc />
        public Money Reduced(Bank bank, string to)
        {
            var amount = Augend.Reduced(bank: bank, to: to).Amount
                       + Addend.Reduced(bank: bank, to: to).Amount;
            return new Money(amount: amount, currency: to);
        }

        /// <inheritdoc />
        public IExpression Plus(IExpression added)
        {
            // 教科書では null を返却しているが、
            // 個人的には、未実装を占める「System.NotImplementedException」例外を飛ばすほうが明文化されると思う
            throw new NotImplementedException();
        }

        #endregion
    }
}
