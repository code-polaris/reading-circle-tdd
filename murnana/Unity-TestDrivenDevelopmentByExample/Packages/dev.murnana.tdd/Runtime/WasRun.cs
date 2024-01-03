#nullable enable
using UnityEngine.Scripting;

namespace TDD
{
    /// <summary>
    /// 第18章「xUnitへ向かう小さな一歩」のサンプル
    /// </summary>
    [RequireDerived]
    internal class WasRun : TestCase
    {
        public WasRun(string name) : base(name: name)
        {
            IsRun = null;
        }

        [RequiredMember]
        public int? IsRun { get; private set; }

        [RequiredMember]
        public void TestMethod()
        {
            IsRun = 1;
        }
    }
}
