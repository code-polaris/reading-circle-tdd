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

        public TestCase(string name)
        {
            var type = GetType();
            m_Method = type.GetMethod(name);
        }

        [RequiredMember]
        public void Run()
        {
            m_Method?.Invoke(obj: this, parameters: null);
        }
    }
}
