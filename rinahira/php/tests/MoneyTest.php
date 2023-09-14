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
        $five = Money::dollar(5);
        $this->assertEquals(Money::dollar(10), $five->times(2));
        $this->assertEquals(Money::dollar(15), $five->times(3));
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
        $this->assertTrue((Money::Franc(5))->equals(Money::Franc(5)));
        $this->assertFalse((Money::Franc(5))->equals(Money::Franc(6)));
        $this->assertFalse((Money::Franc(5))->equals(Money::dollar(5)));

    }

    public function testFrancMultiplication(): void
    {
        $five = Money::Franc(5);
        $this->assertEquals(Money::Franc(10), $five->times(2));
        $this->assertEquals(Money::Franc(15), $five->times(3));
    }

    public function testCurrency(): void
    {
        $this->assertEquals("USD", (Money::dollar(1))->currency());
        $this->assertEquals("CHF", (Money::franc(1))->currency());
    }
}
