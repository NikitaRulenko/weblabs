describe("RecoveryPassword", function () {

  it("SMS recovery method", function () {
    assert.equal(resultSMS, true);
  });

  it("Email recovery method", function () {
    assert.equal(resultEmail, true);
  });

  it("Validate code method", function () {
    assert.equal(resultValidate, false);
  });

  it("SMS recovery method wrong number", function () {
    assert.equal(falseSMS, false);
  });

  it("Email recovery method wrong adress", function () {
    assert.equal(falseEmail, false);
  });

  it("Wrong recovery method", function () {
    assert.equal(wrongMethod, false);
  });

  it("Wrong data validation", function () {
    assert.equal(wrongRecData, false);
  });
});

describe("Code generator", function () {
  it("Generates code", function () {
    assert.equal(toString(cGcode).length, 18);
  });
});


