#nullable enable
using System.Reflection;
using UnityEngine.Scripting;

namespace TDD
{
    [RequireDerived]
    public class TestCase
    {
        /// <summary>
        /// 呼び出すメソッド名
        /// </summary>
        private readonly MethodInfo? m_Method;

        [RequiredMember]
        public int? IsRun { get; protected set; }

        public int? IsSetUp { get; protected set; }

        public TestCase(string name)
        {
            var type = GetType();
            m_Method = type.GetMethod(name);
        }

        [RequiredMember]
        public void Run()
        {
            SetUp();

            m_Method?.Invoke(obj: this, parameters: null);
        }

        /// <summary>
        /// テスト前のセットアップ
        /// </summary>
        [RequiredMember]
        public virtual void SetUp()
        {
        }
    }
}
