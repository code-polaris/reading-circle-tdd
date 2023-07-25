package org.codepolaris.tdd;

import java.util.Objects;

public abstract class Money {
  protected int amount;
  protected String currency;

  Money(int amount, String currency) {
    this.amount = amount;
    this.currency = currency;
  }

  abstract Money times(int multiplier);

  public String currency() {
    return currency;
  }

  public static Dollar dollar(int amount) {
    return new Dollar(amount, "USD");
  }

  public static Franc franc(int amount) {
    return new Franc(amount, "CHF");
  }

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Money money = (Money) o;
    return amount == money.amount;
  }

  @Override
  public int hashCode() {
    return Objects.hash(amount);
  }
}
