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
            Money five = Money.Dollar (5);
            Assert.That (
                actual: five.Times (2),
                expression: Is.EqualTo (Money.Dollar (10))
            );
            Assert.That (
                actual: five.Times (3),
                expression: Is.EqualTo (Money.Dollar (15))
            );
        }

        [Test]
        public void Equal()
        {
            Assert.That (
                actual: Money.Dollar (5).Equals (Money.Dollar (5)),
                expression: Is.True
            );
            Assert.That (
                actual: Money.Dollar (5).Equals (Money.Dollar (6)),
                expression: Is.False
            );
            Assert.That (
                actual: Money.Franc (5).Equals (Money.Franc (5)),
                expression: Is.True
            );
            Assert.That (
                actual: Money.Franc (5).Equals (Money.Franc (6)),
                expression: Is.False
            );
            Assert.That (
                actual: Money.Franc (5).Equals (Money.Dollar (5)),
                expression: Is.False
            );
        }

        [Test]
        public void FrancMultiplication()
        {
            Money five = Money.Franc (5);
            Assert.That (
                actual: five.Times (2),
                expression: Is.EqualTo (Money.Franc (10))
            );
            Assert.That (
                actual: five.Times (3),
                expression: Is.EqualTo (Money.Franc (15))
            );
        }

        [Test]
        public void Currency()
        {
            Assert.That (
                actual: Money.Dollar (1).Currency(),
                expression: Is.EqualTo ("USD")
            );
            Assert.That (
                actual: Money.Franc (1).Currency(),
                expression: Is.EqualTo ("CHF")
            );
        }
    }
}
