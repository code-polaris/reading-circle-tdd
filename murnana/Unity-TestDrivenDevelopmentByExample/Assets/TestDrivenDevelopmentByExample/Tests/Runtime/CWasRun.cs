#nullable enable
namespace TDD.Tests
{
    /// <summary>
    /// 第18章「xUnitへ向かう小さな一歩」のサンプル
    /// </summary>
    internal sealed class CWasRun
    {
        public CWasRun(string name)
        {
            WasRun = null;
        }

        public int? WasRun { get; private set; }

        public void TestMethod()
        {
            WasRun = 1;
        }

        public void Run()
        {
            TestMethod();
        }
    }
}
