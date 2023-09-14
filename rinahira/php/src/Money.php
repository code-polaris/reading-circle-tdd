<?php
declare(strict_types=1);
namespace app;

/**
 * Undocumented class
 */
abstract class Money
{
    /**
     * コンストラクタ
     *
     * @param integer $amount
     * @param string $currency
     */
    public function __construct(protected int $amount, protected string $currency)
    {
    }

    abstract function times(int $multiplier): ?Money;

    /**
     * 通貨取得
     * @return string
     */
    public function currency(): string
    {
        return $this->currency;
    }

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
     * Dollarクラスファクトリメソッド
     * @param integer $amount
     * @return Money
     */
    static function dollar(int $amount): Money
    {
        return new Dollar($amount, "USD");
    }

    /**
     * Francクラスファクトリメソッド
     *
     * @param integer $amount
     * @return Money
     */
    static function franc(int $amount): Money
    {
        return new Franc($amount, "CHF");
    }
}
