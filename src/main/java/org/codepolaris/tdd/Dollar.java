package org.codepolaris.tdd;

public class Dollar {
  int amount;

  public Dollar(int amount) {
    this.amount = amount;
  }

  public void times(int multiplier) {
    amount = amount * multiplier;
  }
}
