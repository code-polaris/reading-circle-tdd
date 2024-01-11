package org.codepolaris.tdd.chapter1;

import org.codepolaris.tdd.chapter1.utils.Currency;

import java.util.Objects;

public class Money implements Expression {
  protected int amount;
  protected String currency;

  Money(int amount, String currency) {
    this.amount = amount;
    this.currency = currency;
  }

  public Expression times(int multiplier) {
    return new Money(amount * multiplier, currency());
  }

  public Expression plus(Expression addend) {
    return new Sum(this, addend);
  }

  @Override
  public Money reduce(Bank bank, String to) {
    int rate =bank.rate(currency, to);
    return new Money(amount / rate, to);
  }

  public String currency() {
    return currency;
  }

  public static Money dollar(int amount) {
    return new Money(amount, Currency.USD);
  }

  public static Money franc(int amount) {
    return new Money(amount, Currency.CHF);
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o instanceof Money money) {
      return amount == money.amount && currency().equals(money.currency());
    }
    return false;
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount);
  }

  @Override
  public String toString() {
    return amount + " " + currency;
  }
}
