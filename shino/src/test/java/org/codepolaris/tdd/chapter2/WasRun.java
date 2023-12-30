package org.codepolaris.tdd.chapter2;

import lombok.extern.slf4j.Slf4j;

import java.lang.reflect.Method;


@Slf4j
public class WasRun extends TestCase {

  private Integer wasRun;

  public WasRun(String testName) {
    super(testName);
    wasRun = null;
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

  public void testMethod() {
    wasRun = 1;
  }

  public Integer getWasRun() {
    return wasRun;
  }
}
