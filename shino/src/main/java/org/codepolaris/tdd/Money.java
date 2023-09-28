package org.codepolaris.tdd;

import org.codepolaris.tdd.utils.Currency;

import java.util.Objects;

public class Money {
  protected int amount;
  protected String currency;

  Money(int amount, String currency) {
    this.amount = amount;
    this.currency = currency;
  }

  public Money times(int multiplier) {
    return new Money(amount * multiplier, currency());
  }

  public String currency() {
    return currency;
  }

  public static Dollar dollar(int amount) {
    return new Dollar(amount, Currency.USD);
  }

  public static Franc franc(int amount) {
    return new Franc(amount, Currency.CHF);
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
