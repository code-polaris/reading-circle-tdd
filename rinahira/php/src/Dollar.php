<?php
declare(strict_types=1);
namespace app;

class Dollar extends Money
{
    public function __construct(protected int $amount)
    {
    }

    public function times(int $multiplier): ?Money
    {
        return new Dollar($this->amount * $multiplier);
    }
}
