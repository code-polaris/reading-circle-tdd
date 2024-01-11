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
        public string? Log { get; protected set; }

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

            TearDown();
        }

        /// <summary>
        /// テスト前の前準備
        /// </summary>
        [RequiredMember]
        public virtual void SetUp()
        {
        }

        /// <summary>
        /// テスト後の後片付け
        /// </summary>
        [RequiredMember]
        public virtual void TearDown()
        {
        }
    }
}
