package org.codepolaris.tdd.chapter2;

import lombok.extern.slf4j.Slf4j;

import java.lang.reflect.Method;

@Slf4j
public class TestCase {
  protected String testName;

  public TestCase(String testName) {
    this.testName = testName;
  }

  public void run() {
    try {
      Method method = this.getClass().getDeclaredMethod(this.testName);
      method.invoke(this);
    } catch (NoSuchMethodException ex) {

      log.error("The provided method name " + this.testName + "not found");
    } catch (Exception ex) {
      log.error("Error during the method call of " + this.testName + ". The actual error is:" + ex.getMessage());
    }
  }
}
