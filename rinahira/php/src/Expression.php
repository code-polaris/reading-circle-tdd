<?php

declare(strict_types=1);

namespace app;

interface Expression
{
    public function reduce(string $to): Money;
}
