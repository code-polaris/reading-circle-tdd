package org.codepolaris.tdd.chapter2;

import lombok.val;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class TestCaseTest {

  @Test
  void testRunning() {
    val test = new WasRun("testMethod");
    assertThat(test.getHasRun()).isFalse();
    test.run();
    assertThat(test.getHasRun()).isTrue();
  }
}
