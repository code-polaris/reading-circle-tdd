package org.codepolaris.tdd;

import org.codepolaris.tdd.utils.Currency;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class MoneyTest {

  @Test
  void testMultiplication() {
    Dollar five = Money.dollar(5);
    assertThat(five.times(2)).isEqualTo(Money.dollar(10));
    assertThat(five.times(3)).isEqualTo(Money.dollar(15));
  }

  @Test
  void testEquality() {
    assertThat(Money.dollar(5).equals(Money.dollar(5))).isTrue();
    assertThat(Money.dollar(5).equals(Money.dollar(6))).isFalse();
    assertThat(Money.franc(5).equals(Money.franc(5))).isTrue();
    assertThat(Money.franc(5).equals(Money.franc(6))).isFalse();
    assertThat(Money.franc(5).equals(Money.dollar(5))).isFalse();
  }

  @Test
  void testFrancMultiplication() {
    Franc five = Money.franc(5);
    assertThat(five.times(2)).isEqualTo(Money.franc(10));
    assertThat(five.times(3)).isEqualTo(Money.franc(15));
  }

  @Test
  void testCurrency() {
    assertThat(Money.dollar(1).currency()).isEqualTo(Currency.USD);
    assertThat(Money.franc(1).currency()).isEqualTo(Currency.CHF);
  }

  @Test
  void testDifferentClassEquality() {
    assertThat( new Money( 10, Currency.CHF)).isEqualTo(new Franc( 10, Currency.CHF));
  }
}
