package org.codepolaris.tdd.chapter2;

import lombok.Getter;

@Getter
public class WasRun extends TestCase {

  private boolean ran;

  public WasRun(String testName) {
    super(testName);
  }

  @Override
  public void setUp() {
    super.setUp();
    this.ran = false;
    this.setUp = true;
  }

  public void testMethod() {
    ran = true;
  }
}
