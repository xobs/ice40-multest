# Tests for the multiplier
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.result import TestFailure, TestSuccess, ReturnValue

@cocotb.coroutine
def do_mul(dut, a, b, backend=0):
    dut.a = a
    dut.b = b
    yield RisingEdge(dut.clk)
    yield RisingEdge(dut.clk)
    raise ReturnValue(dut.x)

@cocotb.coroutine
def do_compare(dut, a, b):
    actual = (a * b) & 0xffffffff

    for backend in range(2):
        result = yield do_mul(dut, a, b, backend)
        if result != actual:
            raise TestFailure("backend {} - {} * {} = {} (should have been {})".format(backend, a, b, result, actual))
        else:
            dut._log.info("{} = {}".format(result, actual))

@cocotb.test()
def basic_mul(dut):
    cocotb.fork(Clock(dut.clk, 10).start())
    dut.backend = 0

    result = yield do_compare(dut, 2, 3)

    dut._log.info("Result of 2 * 3: {}".format(result))