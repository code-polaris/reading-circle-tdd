package org.codepolaris.tdd;

import java.util.Objects;

public class Dollar {
  int amount;

  public Dollar(int amount) {
    this.amount = amount;
  }

  public Dollar times(int multiplier) {
    return new Dollar(amount * multiplier);
  }

  /**
   * According to the book, equals method cast object directly, but this isn't good java
   * practice. In this method equals method is followed on the Java's manner.
   */
  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (o == null || getClass() != o.getClass()) return false;
    Dollar dollar = (Dollar) o;
    return amount == dollar.amount;
  }

  /**
   * According to the book, the class doesn't have the hashCode method. But this has to be implemented when
   * equals methods is override. So it's been added here.
   */
  @Override
  public int hashCode() {
    return Objects.hash(amount);
  }
}
