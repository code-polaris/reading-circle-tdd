<?php

declare(strict_types=1);

namespace app;

class Pair
{

    public function __construct(private string $from, private string $to)
    {
        
    }

    public function equals(Pair $object) : Bool
    {
        return $this->from === $object->from && $this->to === ($object->to);
    }

    public function hashCode() : int
    {
        return 0;
    }
}
