#nullable enable
using System;
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
            Running();
        }

        /// <summary>
        /// テストを実行します
        /// </summary>
        private void Running()
        {
            var testType = typeof(WasRun);
            var test     = Activator.CreateInstance(type: testType, "TestMethod");

            var isRun      = testType.GetProperty("IsRun");
            var testMethod = testType.GetMethod("Run");

            // print(test.wasRun)
            var testWasRun1 = isRun?.GetValue(test);
            Debug.LogFormat(
                logType: LogType.Log,
                logOptions: LogOption.None,
                context: this,
                format: "{0}",
                testWasRun1 ?? "<null>"
            );

            // test.testMethod
            testMethod?.Invoke(obj: test, parameters: null);

            // print(test.wasRun)
            var testWasRun2 = isRun?.GetValue(test);
            Debug.LogFormat(
                logType: LogType.Log,
                logOptions: LogOption.None,
                context: this,
                format: "{0}",
                testWasRun2 ?? "<null>"
            );
        }
    }
}
