#nullable enable
using System;
using NUnit.Framework;

namespace TDD.Tests
{
    [Description("第18章「xUnitへ向かう小さな一歩」のサンプル")]
    public sealed class NUnitSample
    {
        [Test]
        [Description("C#な書き方")]
        public void Sample()
        {
            var test = new CWasRun("TestMethod");
            TestContext.WriteLine(test.WasRun);
            test.TestMethod();
            TestContext.WriteLine(test.WasRun);
        }

        [Test]
        [Description("Reflectionを使ったC#の書き方(IL2CPPだとアウト)")]
        public void SampleReflection()
        {
            var testType = typeof(CWasRun);
            var test     = Activator.CreateInstance(type: testType, "TestMethod");

            var wasRun     = testType.GetProperty("WasRun");
            var testMethod = testType.GetMethod("TestMethod");

            // print(test.wasRun)
            TestContext.WriteLine(wasRun?.GetValue(test));

            // test.testMethod
            testMethod?.Invoke(obj: test, parameters: null);

            // print(test.wasRun)
            TestContext.WriteLine(wasRun?.GetValue(test));
        }
    }
}
