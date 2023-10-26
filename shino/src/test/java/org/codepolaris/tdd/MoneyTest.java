package org.codepolaris.tdd;

import org.codepolaris.tdd.utils.Currency;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.codepolaris.tdd.Money.dollar;
import static org.codepolaris.tdd.utils.Currency.USD;

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
    assertThat(dollar(1).currency()).isEqualTo(USD);
    assertThat(Money.franc(1).currency()).isEqualTo(Currency.CHF);
  }

  @Test
  void testSimpleAddition() {
    Money five = dollar(5);
    Expression sum = five.plus(five);
    Bank bank = new Bank();
    Money reduced = bank.reduce(sum, USD);
    assertThat(reduced).isEqualTo(dollar(10));
  }

  @Test
  void testPlusReturnsSum() {
    Money five = dollar(5);
    Expression result = five.plus(five);
    Sum sum = (Sum) result;
    assertThat(sum.augend).isEqualTo(five);
    assertThat(sum.addend).isEqualTo(five);
  }

  @Test
  void testReduceSum() {
    Expression sum = new Sum(dollar(3), dollar(4));
    Bank bank = new Bank();
    Money result = bank.reduce(sum, USD);
    assertThat(result).isEqualTo(Money.dollar(7));
  }

  @Test
  void testReduceMoney() {
    Bank bank = new Bank();
    Money result = bank.reduce(Money.dollar(1), USD);
    assertThat(result).isEqualTo(Money.dollar(1));
  }

  @Test
  void testReduceMoneyDifferentCurrency() {
    Bank bank = new Bank();
    bank.addRate(Currency.CHF, USD, 2);
    Money result = bank.reduce(Money.franc(2), USD);
    assertThat(result).isEqualTo(Money.dollar(1));
  }

  @Test
  void testIdentityRate() {
    assertThat(new Bank().rate(USD, USD)).isEqualTo(1);
  }

}
