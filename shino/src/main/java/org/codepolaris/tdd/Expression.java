package org.codepolaris.tdd;

public interface Expression {
  Money reduce(Bank bank, String to);
}
