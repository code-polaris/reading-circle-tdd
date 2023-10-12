package org.codepolaris.tdd;

import org.codepolaris.tdd.utils.Currency;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.codepolaris.tdd.Money.dollar;

class MoneyTest {

  @Test
  void testMultiplication() {
    Money five = dollar(5);
    assertThat(five.times(2)).isEqualTo(dollar(10));
    assertThat(five.times(3)).isEqualTo(dollar(15));
  }

  @Test
  void testEquality() {
    assertThat(dollar(5).equals(dollar(5))).isTrue();
    assertThat(dollar(5).equals(dollar(6))).isFalse();
    assertThat(Money.franc(5).equals(dollar(5))).isFalse();
  }

  @Test
  void testCurrency() {
    assertThat(dollar(1).currency()).isEqualTo(Currency.USD);
    assertThat(Money.franc(1).currency()).isEqualTo(Currency.CHF);
  }

  @Test
  void testSimpleAddition() {
    Money five = dollar(5);
    Expression sum = five.plus(five);
    Bank bank = new Bank();
    Money reduced = bank.reduced(sum, Currency.USD);
    assertThat(reduced).isEqualTo(Money.dollar(10));
  }
}
