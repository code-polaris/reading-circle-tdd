<?php

declare(strict_types=1);

namespace app;

/**
 * 銀行class
 */
class Bank
{
    private $rates = [];

    /**
     * 換算
     *
     * @param Expression $source
     * @param string $to
     * @return Money
     */
    public function reduce(Expression $source, string $to): Money
    {
        return $source->reduce($this, $to);
    }
    
    public function addRate(String $from, String $to, int $rate):void
    {
        // PHPでは連想配列のキーにオブジェクトは指定できないので、serializeしてセット
        $this->rates = [serialize(new Pair($from, $to)) => $rate];
    }

    public function rate(String $from, String $to) : int
    {
        if ($from === $to) {
            return 1;
        }
        // キーにオブジェクトは指定できないのでserializeする
        return $this->rates[serialize(new Pair($from, $to))];
    }
}
