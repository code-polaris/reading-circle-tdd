using NUnit.Framework;

namespace TDD.Tests
{
    public sealed class MultiCurrencyMoneyTests
    {
        /// <summary>
        ///     $5 * 2 = $10
        /// </summary>
        [Test]
        public void Multiplication()
        {
            var five = new Dollar (5);
            five.Times (2);
            Assert.That (actual: five.Amonut, expression: Is.EqualTo (10));
        }
    }
}
