#nullable enable
using System.Reflection;

namespace TDD.Tests
{
    public class CTestCase
    {
        /// <summary>
        /// 呼び出すメソッド名
        /// </summary>
        private readonly MethodInfo? m_Method;

        public CTestCase(string name)
        {
            var type = GetType();
            m_Method = type.GetMethod(name);
        }

        public void Run()
        {
            m_Method?.Invoke(obj: this, parameters: null);
        }
    }
}
