# Tests for the multiplier
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.result import TestFailure, TestSuccess, ReturnValue
import random

@cocotb.coroutine
def do_mul(dut, a, b, backend=0):
    dut.a = a
    dut.b = b
    dut.backend = backend
    yield RisingEdge(dut.clk)
    yield RisingEdge(dut.clk)
    raise ReturnValue(dut.x)

@cocotb.coroutine
def do_compare(dut, a, b):
    actual = (a * b) & 0xffffffff

    dut._log.info("{} * {}".format(a, b))
    for backend in range(2):
        result = yield do_mul(dut, a, b, backend)
        if not result.value.is_resolvable:
            raise TestFailure("{} is not resolvable".format(result))
        if result != actual:
            raise TestFailure("  backend {} - {} * {} = {} (should have been {})".format(backend, a, b, result, actual))
        else:
            dut._log.info("  backend {}: {} * {} = {}".format(backend, a, b, result))

@cocotb.test()
def basic_mul(dut):
    random.seed(1)
    cocotb.fork(Clock(dut.clk, 10).start())
    dut.backend = 0

    for tst in range(256):
        a = random.randint(0, 2**32-1)
        b = random.randint(0, 2**32-1)
        result = yield do_compare(dut, a, b)