<?php
declare(strict_types=1);
namespace app;

class Franc
{
    public function __construct(private int $amount)
    {
    }

    public function times(int $multiplier): ?Franc
    {
        return new Franc($this->amount * $multiplier);
    }

    public function equals(Object $object): bool
    {
        $dollar = $object;
        return $this->amount === $dollar->amount;
    }
}
