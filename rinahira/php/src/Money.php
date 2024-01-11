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
    public function __construct(public int $amount, protected string $currency)
    {
    }

    public function times(int $multiplier): Expression
    {
        return new Money($this->amount * $multiplier, $this->currency);
    }

    public function plus(Expression $addend): Expression
    {
        return new Sum($this, $addend);
    }

    /**
     * 換算
     *
     * @param string $to
     * @return Money
     */
    public function reduce(Bank $bank, string $to): Money
    {
        $rate = $bank->rate($this->currency(), $to);
        return new Money($this->amount / $rate, $to);
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
