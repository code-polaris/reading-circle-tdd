<?php

declare(strict_types=1);

namespace app;

use Exception;

class Sum implements Expression
{
    public function __construct(public Expression $augend, public Expression $addend)
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

    public function times(int $multiplier): Expression
    {
        return new Sum($this->augend->times($multiplier), $this->addend->times($multiplier));
    }

    public function plus(Expression $addend): Expression
    {
        return new Sum($this, $addend);
    }

    public function reduce(Bank $bank, string $to): Money
    {
        $amount = $this->augend->reduce($bank, $to)->amount + $this->addend->reduce($bank, $to)->amount;
        return new Money($amount, $to);
    }
}
