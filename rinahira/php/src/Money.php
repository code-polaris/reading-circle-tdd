<?php
declare(strict_types=1);
namespace app;

abstract class Money
{
    public function __construct(protected int $amount)
    {
    }

    abstract function times(int $multiplier);

    /**
     * 等価性比較
     *
     * @param Object $object
     * @return boolean
     */
    public function equals(Object $object): bool
    {
        $money = $object;
        return $this->amount === $money->amount && get_class($this) === get_class($money);
    }

    /**
     * Dollarクラス返却
     * @param integer $amount
     * @return Money
     */
    static function dollar(int $amount): Money
    {
        return new Dollar($amount);

    }

    /**
     * Francクラス返却
     *
     * @param integer $amount
     * @return Money
     */
    static function franc(int $amount): Money
    {
        return new Franc($amount);
    }
}
