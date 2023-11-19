namespace TDD
{
    /// <summary>
    /// 銀行
    /// </summary>
    public class Bank
    {
        /// <summary>
        /// 式を解釈し、<paramref name="to" /> 通貨へ変換します
        /// </summary>
        /// <param name="source">式</param>
        /// <param name="to">変換後の通貨</param>
        /// <returns></returns>
        public Money Reduced(IExpression source, string to)
        {
            return source.Reduced(to);
        }
    }
}
