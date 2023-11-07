<?php

declare(strict_types=1);

namespace app;

/**
 * 銀行class
 */
class Bank
{
    /**
     * 換算
     *
     * @param Expression $source
     * @param string $to
     * @return Money
     */
    public function reduce(Expression $source, string $to): Money
    {
        return $source->reduce($to);
    }
}
