package org.codepolaris.tdd.chapter2;

import lombok.val;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class XunitTest {

  @Test
  void testRunning() {
    val test = new WasRun("testMethod");
    assertThat(test.getWasRun()).isNull();
    test.run();
    assertThat(test.getWasRun()).isEqualTo(1);
  }
}
