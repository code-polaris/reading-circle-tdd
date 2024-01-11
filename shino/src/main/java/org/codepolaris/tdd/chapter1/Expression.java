package org.codepolaris.tdd.chapter1;

public interface Expression {
  Money reduce(Bank bank, String to);

  Expression plus(Expression addend);

  Expression times(int multiplier);
}
