<?php declare(strict_types=1);

require_once "Dollar.php";

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
        $five = new Dollar(5);
        $this->assertEquals(new Dollar(10), $five->times(2));
        $this->assertEquals(new Dollar(15), $five->times(3));
    }

    /**
     * 5ドルは他の5ドルと等価
     *
     * @return void
     */
    public function testsEquality(): void
    {
        $this->assertTrue((new Dollar(5))->equals(new Dollar(5)));
        $this->assertFalse((new Dollar(5))->equals(new Dollar(6)));

    }
}
