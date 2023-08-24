<?php
declare(strict_types=1);
namespace app;

class Money
{
    public function __construct(protected int $amount)
    {
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
}
