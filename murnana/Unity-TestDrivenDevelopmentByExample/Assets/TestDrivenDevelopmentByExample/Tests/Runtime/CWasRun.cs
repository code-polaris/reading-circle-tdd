#nullable enable
namespace TDD.Tests
{
    /// <summary>
    /// 第18章「xUnitへ向かう小さな一歩」のサンプル
    /// </summary>
    internal sealed class CWasRun : CTestCase
    {
        public CWasRun(string name) : base(name: name)
        {
            WasRun = null;
        }

        public int? WasRun { get; private set; }

        public void TestMethod()
        {
            WasRun = 1;
        }
    }
}
