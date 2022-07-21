# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for inp12"""
    S=5'b01100
    inp0=00
    inp1=01
    inp2=11
    inp3=01
    inp4=01
    inp5=00
    inp6=11
    inp7=01
    inp8=11
    inp9=11
    inp10=01
    inp11=01
     inp12=00
    inp13=11
    inp14=00
    inp15=01
    inp16=11
    inp17=01
    inp18=01
    inp19=01
     inp20=11
        inp21=00
     inp22=01
    inp23=11
    inp24=01
    inp25=11
    inp26=11
    inp27=11
    inp28=11
    inp29=01
    inp30=00
    
    #input driving
    dut.sel.value=S
    
    await Timer(2, units='ns')
    
    assert dut.out.value == inp12, f"MUX output is incorrect: {dut.X.value} != inp12"

    cocotb.log.info('##### CTB: Develop your test here ########')
