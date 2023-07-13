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
            var five    = new Dollar (5);
            var product = five.Times (2);
            Assert.That (actual: product.Amonut, expression: Is.EqualTo (10));
            product = five.Times (3);
            Assert.That (actual: product.Amonut, expression: Is.EqualTo (15));
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
    }
}
