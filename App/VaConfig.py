from VaScript import getVaScript

def setup(va):

    ### The VAOP variables setting

    va.defineVariable('The sequential number of the v-agent jump...p10', 0)
    va.defineVariable('The max number of the v-agent jump. It is for prevent looping...p11', 1000)
    va.defineVariable('The default locale language code...p12_0', 'en-US')
    va.defineVariable('The locale language code...p12_1', 'en-US')
    va.defineVariable('VA script...va_script', getVaScript()) #14
    va.defineVariable('The previous Action...previous action', 'Unknown') #15
    va.defineVariable('The current Action...current action', 'Action_000') #16
    va.defineVariable('Direction...direction', 'Direction_10') #17

