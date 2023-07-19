<?php

declare(strict_types=1);

class Dollar
{
    public function __construct(private int $amount)
    {
    }

    public function times(int $multiplier): ?Dollar
    {
        return new Dollar($this->amount * $multiplier);
    }

    public function equals(Object $object): bool
    {
        $dollar = $object;
        return $this->amount === $dollar->amount;
    }
}
