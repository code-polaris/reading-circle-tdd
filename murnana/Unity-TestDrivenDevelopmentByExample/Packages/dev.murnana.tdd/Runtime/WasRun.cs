#nullable enable
using UnityEngine.Scripting;

namespace TDD
{
    /// <summary>
    /// 第18章「xUnitへ向かう小さな一歩」のサンプル
    /// </summary>
    [RequireDerived]
    internal sealed class WasRun : TestCase
    {
        public WasRun(string name) : base(name: name)
        {
        }

        [RequiredMember]
        public void TestMethod()
        {
            IsRun = 1;
        }

        /// <inheritdoc />
        public override void SetUp()
        {
            IsRun   = null;
            IsSetUp = 1;
        }
    }
}
