namespace TDD
{
    /// <summary>
    /// 通貨同士の計算をおこなう、式のインターフェース
    /// </summary>
    public interface IExpression
    {
        /// <summary>
        /// 式を解釈し、<paramref name="to" /> 通貨へ変換します
        /// </summary>
        /// <param name="bank">変換レートの入った、銀行のインスタンス</param>
        /// <param name="to">変換後の通貨</param>
        /// <returns></returns>
        public Money Reduced(Bank bank, string to);
    }
}
