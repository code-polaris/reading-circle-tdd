<?php

declare(strict_types=1);

namespace app;

interface Expression
{
    public function times(int $multiplier): Expression;
    public function plus(Expression $addend): Expression;
    public function reduce(Bank $bank, string $to): Money;
}
