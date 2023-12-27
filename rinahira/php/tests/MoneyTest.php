<?php

declare(strict_types=1);

namespace app;

use PHPUnit\Framework\TestCase;

class MoneyTest extends TestCase
{
    /**
     * $5 * 2 = $10
     *
     * @return void
     */
    public function testMultiplication(): void
    {
        /** Money $five */
        $five = Money::dollar(5);
        $this->assertTrue((Money::dollar(10))->equals($five->times(2)));
        $this->assertTrue((Money::dollar(15))->equals($five->times(3)));
    }

    /**
     * 5ドルは他の5ドルと等価
     *
     * @return void
     */
    public function testsEquality(): void
    {
        $this->assertTrue((Money::dollar(5))->equals(Money::dollar(5)));
        $this->assertFalse((Money::dollar(5))->equals(Money::dollar(6)));
        $this->assertFalse((Money::Franc(5))->equals(Money::dollar(5)));
    }

    /**
     * 通貨の確認
     *
     * @return void
     */
    public function testCurrency(): void
    {
        $this->assertEquals("USD", (Money::dollar(1))->currency());
        $this->assertEquals("CHF", (Money::franc(1))->currency());
    }

    /**
     * $5 + $5 = $10
     *
     * @return void
     */
    public function testSimpleAddition(): void
    {
        $five = Money::dollar(5);
        $sum =  $five->plus($five);
        $bank = new Bank();
        $reduced = $bank->reduce($sum, "USD");
        $this->assertEquals(Money::dollar(10), $reduced);
    }

    public function testPlusReturnsSum(): void
    {
        $five = Money::dollar(5);
        $result = $five->plus($five);
        /** @var sum $sum */
        $sum = Sum::cast($result);
        $this->assertEquals($five, $sum->augend);
        $this->assertEquals($five, $sum->addend);
    }

    public function testReduceSum(): void
    {
        $sum = new Sum(Money::dollar(3), Money::dollar(4));
        $bank = new Bank();
        $result = $bank->reduce($sum, "USD");
        $this->assertEquals(Money::dollar(7), $result);
    }

    public function testReduceMoney(): void
    {
        $bank = new Bank();
        $result = $bank->reduce(Money::dollar(1), "USD");
        $this->assertEquals(Money::dollar(1), $result);
    }

    public function testReduceMoneyDifferentCurrency(): void
    {
        $bank = new Bank();
        $bank->addRate("CHF", "USD", 2);
        $result = $bank->reduce(Money::franc(2), "USD");
        $this->assertEquals(Money::dollar(1), $result);
    }

    public function testIdentityRate(): void
    {
        $this->assertEquals(1, (new Bank())->rate("USD", "USD"));
    }

    public function testMixedAddition()
    {
        $fiveBucks = Money::dollar(5);
        $tenFrancs = Money::franc(10);
        $bank = new Bank();
        $bank->addRate("CHF", "USD", 2);
        $result = $bank->reduce($fiveBucks->plus($tenFrancs), "USD");
        $this->assertEquals(Money::dollar(10), $result);
    }

    public function testSumPlusMoney(): void
    {
        $fiveBucks = Money::dollar(5);
        $tenFrancs = Money::franc(10);
        $bank = new Bank();
        $bank->addRate("CHF", "USD", 2);
        $sum = (new Sum($fiveBucks, $tenFrancs))->plus($fiveBucks);
        $result = $bank->reduce($sum, "USD");
        $this->assertEquals(Money::dollar(15), $result);
    }

    public function testSumTimes(): void
    {
        $fiveBucks = Money::dollar(5);
        $tenFrancs = Money::franc(10);
        $bank = new Bank();
        $bank->addRate("CHF", "USD", 2);
        $sum = (new Sum($fiveBucks, $tenFrancs))->times(2);
        $result = $bank->reduce($sum, "USD");
        $this->assertEquals(Money::dollar(20), $result);
    }
}
