<?php
declare(strict_types=1);
namespace app;

class Franc extends Money
{
    public function __construct(protected int $amount)
    {
    }

    public function times(int $multiplier): ?Franc
    {
        return new Franc($this->amount * $multiplier);
    }
}
