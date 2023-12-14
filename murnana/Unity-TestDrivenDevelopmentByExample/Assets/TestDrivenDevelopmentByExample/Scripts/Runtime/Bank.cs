using System.Collections.Generic;

namespace TDD
{
    /// <summary>
    /// 銀行
    /// </summary>
    public class Bank
    {
        /// <summary>
        /// 為替レートの一覧
        /// </summary>
        private readonly Dictionary<Pair, int> m_Rates = new();

        /// <summary>
        /// 式を解釈し、<paramref name="to" /> 通貨へ変換します
        /// </summary>
        /// <param name="source">式</param>
        /// <param name="to">変換後の通貨</param>
        /// <returns></returns>
        public Money Reduced(IExpression source, string to)
        {
            return source.Reduced(bank: this, to: to);
        }

        /// <summary>
        /// 為替レートを追加、もしくは更新します
        /// </summary>
        /// <param name="from">元の通貨</param>
        /// <param name="to">変換先通貨</param>
        /// <param name="rate">レート</param>
        public void AddRate(string from, string to, int rate)
        {
            var key = new Pair(from: from, to: to);
            if(!m_Rates.TryAdd(key: key, value: rate))
            {
                // キーがすでにある場合は、上書きします
                m_Rates[key] = rate;
            }
        }

        /// <summary>
        /// 為替レートを取得します
        /// </summary>
        /// <param name="from">変換元通貨</param>
        /// <param name="to">変換先通貨</param>
        /// <returns></returns>
        public int GetRate(string from, string to)
        {
            if(from == to)
            {
                return 1;
            }

            var key = new Pair(from: from, to: to);
            return m_Rates[key];
        }
    }
}
