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
            Assert.That (
                actual: five.Times (2),
                expression: Is.EqualTo (new Dollar (10))
            );
            Assert.That (
                actual: five.Times (3),
                expression: Is.EqualTo (new Dollar (15))
            );
        }

        [Test]
        public void Equal()
        {
            Assert.That (
                actual: new Dollar (5).Equals (new Dollar (5)),
                expression: Is.True
            );
            Assert.That (
                actual: new Dollar (5).Equals (new Dollar (6)),
                expression: Is.False
            );
        }

        [Test]
        public void FrancMultiplication()
        {
            var five = new Franc (5);
            Assert.That (
                actual: five.Times (2),
                expression: Is.EqualTo (new Franc (10))
            );
            Assert.That (
                actual: five.Times (3),
                expression: Is.EqualTo (new Franc (15))
            );
        }

    }
}