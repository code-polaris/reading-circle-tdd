using System;

namespace TDD
{
    /// <summary>
    /// 為替レートを保存するためのキー値
    /// </summary>
    public class Pair : IEquatable<Pair>
    {
        private readonly string m_From;
        private readonly string m_To;

        public Pair(string from, string to)
        {
            m_From = from;
            m_To   = to;
        }

        #region Equality members

        /// <inheritdoc />
        public bool Equals(Pair other)
        {
            if(ReferenceEquals(objA: null, objB: other))
            {
                return false;
            }

            if(ReferenceEquals(objA: this, objB: other))
            {
                return true;
            }

            return (m_From == other.m_From)
                && (m_To == other.m_To);
        }

        /// <inheritdoc />
        public override bool Equals(object obj)
        {
            if(ReferenceEquals(objA: null, objB: obj))
            {
                return false;
            }

            if(ReferenceEquals(objA: this, objB: obj))
            {
                return true;
            }

            if(obj.GetType() != GetType())
            {
                return false;
            }

            return Equals((Pair)obj);
        }

        /// <inheritdoc />
        public override int GetHashCode()
        {
            return 0;

            // Riderが生み出したコード。今回は教科書通り 0 を返却します
            // unchecked
            // {
            //     return ((m_From != null ? m_From.GetHashCode() : 0) * 397) ^ (m_To != null ? m_To.GetHashCode() : 0);
            // }
        }

        #endregion
    }
}
