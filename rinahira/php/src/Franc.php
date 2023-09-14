<?php
declare(strict_types=1);
namespace app;

class Franc extends Money
{
    /**
     * 金額に数値を掛け金額を得る
     * 
     * @param integer $multiplier
     * @return Money
     */
    public function times(int $multiplier): Money
    {
        return Money::franc($this->amount * $multiplier);
    }
}
