#nullable enable
using UnityEngine;

namespace TDD.BootStrap
{
    [ExcludeFromPreset]
    [ExcludeFromObjectFactory]
    [DisallowMultipleComponent]
    internal sealed class TestCaseTest : MonoBehaviour
    {
        /// <summary>
        /// スクリプトが初めて有効化されたフレームで、Update関数が実行される前に呼ばれます
        /// </summary>
        /// <seealso href="https://docs.unity3d.com/ScriptReference/MonoBehaviour.Start.html" />
        /// <seealso href="https://docs.unity3d.com/Manual/ExecutionOrder.html" />
        private void Start()
        {
            TemplateMethod();
        }

        /// <summary>
        /// テストを実行します
        /// </summary>
        private void TemplateMethod()
        {
            var test = new WasRun("TestMethod");
            test.Run();
            Debug.AssertFormat(
                condition: test.Log == "Setup TestMethod TearDown ",
                context: this,
                format: "{0} == \"Setup TestMethod TearDown \" but '{1}'",
                nameof(test.Log),
                test.Log
            );
        }
    }
}
