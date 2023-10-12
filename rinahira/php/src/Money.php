<?php
declare(strict_types=1);
namespace app;

class Money implements Expression
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

    public function times(int $multiplier): ?Money {
        return new Money($this->amount * $multiplier, $this->currency);
    }

    public function plus(Money $addend) : Expression {
        return new Money($this->amount + $addend->amount, $this->currency());
    }

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
        return $this->amount === $money->amount && $this->currency() === $money->currency;
    }

    public function toString(): string
    {
        return $this->amount . " " . $this->currency();
    }
    /**
     * Dollarクラスファクトリメソッド
     * @param integer $amount
     * @return Money
     */
    static function dollar(int $amount): Money
    {
        return new Money($amount, "USD");
    }

    /**
     * Francクラスファクトリメソッド
     *
     * @param integer $amount
     * @return Money
     */
    static function franc(int $amount): Money
    {
        return new Money($amount, "CHF");
    }
}
