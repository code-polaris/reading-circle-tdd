<?php

declare(strict_types=1);

namespace app;

use Exception;

class Sum implements Expression
{
    public function __construct(public Money $augend, public Money $addend)
    {
    }

    /**
     * Javaと違って(Sum)でキャストできないのでキャストするメソッド作った
     *
     * @param Expression $obj
     * @return self
     */
    public static function cast(Expression $obj): self
    {
        if (!($obj instanceof self)) {
            throw new Exception("{$obj} is not instance of CastObject");
        }
        return $obj;
    }

    public function reduce(string $to): Money
    {
        $amount = $this->augend->amount + $this->addend->amount;
        return new Money($amount, $to);
    }
}
