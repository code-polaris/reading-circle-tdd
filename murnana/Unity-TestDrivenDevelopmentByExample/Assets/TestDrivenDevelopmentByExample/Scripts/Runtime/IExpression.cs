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

        /// <summary>
        /// 通貨を加算します
        /// </summary>
        /// <param name="added">加算する通貨</param>
        /// <returns>加算結果(新規インスタンス)</returns>
        /// <remarks>
        /// <para>インスタンス自身には何も影響を与えません</para>
        /// </remarks>
        public IExpression Plus(IExpression added);
    }
}
