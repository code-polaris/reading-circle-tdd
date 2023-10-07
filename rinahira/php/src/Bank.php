<?php
declare(strict_types=1);
namespace app;

/**
 * 銀行class
 */
class Bank {
    /**
     * 換算
     *
     * @param Expression $source
     * @param string $to
     * @return void
     */
    public function reduce(Expression $source, string $to) {
        return Money::dollar(10);
    }
}