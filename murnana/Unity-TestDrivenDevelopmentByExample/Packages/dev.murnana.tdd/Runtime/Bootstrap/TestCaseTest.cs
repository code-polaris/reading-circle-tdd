#nullable enable
using UnityEngine;

namespace TDD.BootStrap
{
    [ExcludeFromPreset]
    [ExcludeFromObjectFactory]
    [DisallowMultipleComponent]
    internal sealed class TestCaseTest : MonoBehaviour
    {
        private TestCase? m_Test;

        /// <summary>
        /// スクリプトが初めて有効化されたフレームで、Update関数が実行される前に呼ばれます
        /// </summary>
        /// <seealso href="https://docs.unity3d.com/ScriptReference/MonoBehaviour.Start.html" />
        /// <seealso href="https://docs.unity3d.com/Manual/ExecutionOrder.html" />
        private void Start()
        {
            Setup();
            Running();
        }

        /// <summary>
        /// テストを実行します
        /// </summary>
        private void Running()
        {
            Debug.AssertFormat(
                condition: m_Test != null,
                context: this,
                format: "{0} != null",
                nameof(m_Test)
            );
            m_Test!.Run();

            // print(test.wasRun)
            Debug.AssertFormat(
                condition: m_Test.IsRun != null,
                context: this,
                format: "{0} != null",
                nameof(m_Test.IsRun)
            );
        }

        private void Setup()
        {
            m_Test = new WasRun("TestMethod");
        }
    }
}
