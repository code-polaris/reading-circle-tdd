#nullable enable
namespace TDD.Tests
{
    /// <summary>
    /// 第18章「xUnitへ向かう小さな一歩」のサンプル
    /// </summary>
    internal sealed class CWasRun
    {
        private readonly string m_Name;

        public CWasRun(string name)
        {
            m_Name = name;
            WasRun = null;
        }

        public int? WasRun { get; private set; }

        public void TestMethod()
        {
            WasRun = 1;
        }

        public void Run()
        {
            var type       = typeof(CWasRun);
            var methodInfo = type.GetMethod(m_Name);
            methodInfo?.Invoke(obj: this, parameters: null);
        }
    }
}
