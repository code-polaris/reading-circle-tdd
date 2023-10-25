package org.codepolaris.tdd;

import org.codepolaris.tdd.utils.Currency;

import java.util.Objects;

public class Money implements Expression {
  protected int amount;
  protected String currency;

  Money(int amount, String currency) {
    this.amount = amount;
    this.currency = currency;
  }

  public Money times(int multiplier) {
    return new Money(amount * multiplier, currency());
  }

  public Expression plus(Money addeed) {
    return new Sum(this, addeed);
  }

  @Override
  public Money reduce(String to) {
    return this;
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
