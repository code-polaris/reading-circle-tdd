using System.Security.Cryptography;
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
                actual: Money.Franc (5).Equals (Money.Dollar (5)),
                expression: Is.False
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

        [Test]
        [Description("足し算を行うテスト")]
        public void SimpleAddition()
        {
            var five    = Money.Dollar(5);                      // 5ドルを意味するオブジェクトの生成
            var sum     = five.Plus(five);                      // 二つの Money の和は Expression (式) インスタンスになる
            var bank    = new Bank();                           // 通貨の式を解釈する Imposter、銀行を生成する
            var reduced = bank.Reduced(source: sum, to: "USD"); // 銀行が、Expression を解釈して結果を返す
            Assert.That(
                actual: reduced,
                expression: Is.EqualTo(Money.Dollar(10))
            );
        }

        [Test]
        [Description("TDD.Money.Plus の内部テスト")]
        public void PlusReturnSum()
        {
            var five   = Money.Dollar(5);
            var result = five.Plus(five);
            var sum    = (Sum)result;
            Assert.That(actual: five, expression: Is.EqualTo(sum.Augend));
            Assert.That(actual: five, expression: Is.EqualTo(sum.Addend));
        }

        [Test]
        [Description("Sum の結果は Bank で特定の通貨として変換される")]
        public void ReduceSum()
        {
            var sum    = new Sum(augend: Money.Dollar(3), addend: Money.Dollar(4));
            var bank   = new Bank();
            var result = bank.Reduced(source: sum, to: "USD");
            Assert.That(actual: Money.Dollar(7), expression: Is.EqualTo(result));
        }

        [Test]
        public void ReduceMoney()
        {
            var bank   = new Bank();
            var result = bank.Reduced(source: Money.Dollar(1), to: "USD");
            Assert.That(actual: Money.Dollar(1), expression: Is.EqualTo(result));
        }
    }
}
